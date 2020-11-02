# 
import sys
import os
sys.path.extend([
        os.path.abspath('../')])
base_url = os.environ['ROBOTEST_WWW'] if 'ROBOTEST_WWW' in os.environ else 'https://robotest.theedtech.dev'

import json
import random
import traceback
from fastapi import FastAPI, Form
from starlette.responses import PlainTextResponse, RedirectResponse
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from urllib.parse import quote_plus, urlparse, urlunparse, urlencode, parse_qsl

from typing import List, Dict
from datetime import datetime

from lti import LineItem, ToolRegistration, LTIMessage, LTIResourceLink, DeeplinkResponse, DLIFrame, DLWindow
from lti import Members, DeeplinkSettings,get_public_keyset, get_publickey_pem, const, registration, ltiservice_get
from lti import get_platform_config, register_tool, base_tool_oidc_conf

from robotest.test_results import TestCategory, TestResult

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="templates")

context_sub_variables = {
    'context_id_history': '$Context.id.history',
    'context_start_date': '$CourseSection.timeFrame.begin',
    'context_end_date': '$CourseSection.timeFrame.end'
}

link_sub_variables = {
    'resource_link_history': '$ResourceLink.id.history',
    'resource_available_start':'$ResourceLink.available.startDateTime',
    'resource_available_end':'$ResourceLink.available.endDateTime',
    'resource_submission_start':'$ResourceLink.submission.startDateTime',
    'resource_submission_end':'$ResourceLink.submission.endDateTime'
}

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("moodleinstructions.html", {"request": request, "base_url": base_url, "custom_params": {**context_sub_variables, **link_sub_variables}})

@app.get("/broken")
def read_broken(request: Request):
    return templates.TemplateResponse("broken.html", {"request": request})

@app.get("/results")
def read_results(request: Request,
                 success: bool = True):
    cat1 = TestCategory(name='category 1')
    cat1.results.append(TestResult('res1 blah blah blllla', True, True, 'You passed this easily'))
    cat1.results.append(TestResult('res2 is required to pass this', True, True, 'You passed this but not so easily'))
    cat1.results.append(TestResult('res3 cannot be failed even if you want', success, True, 'How did you not pass this test?'))
    cat2 = TestCategory(name='category 2')
    cat2.results.append(TestResult('res1 blah blah blllla', True, True, 'You passed this easily'))
    cat2.results.append(TestResult('res2 is required to pass this', True, True, 'You passed this but not so easily'))
    cat2.results.append(TestResult('res3 cannot be failed even if you want', success, True, 'https://moodle.zeedeeyou.com/mod/lti/services.php/CourseSection/2/bindings/3/memberships'))
    print( cat1.success )

    return templates.TemplateResponse("results.html", {"request": request, "results": [cat1, cat2], "success": cat1.success, "showClose": True})

@app.get("/register")
def register(request: Request, openid_configuration: str, registration_token: str):
    res = TestCategory(name='Dynamic Registration')
    res.results.append(TestResult('OpenId Config URL',
                                   openid_configuration or False,
                                   True,
                                   'OpenId config URL is required to get the platform info'))
    if openid_configuration:
        try:
            platform_config = get_platform_config(openid_configuration)
            res.results.append(TestResult('Config retrieved from Platform',
                                        platform_config or False,
                                        True,
                                        "",
                                        json.dumps(platform_config, indent=2) if platform_config else 'No config'));
            if platform_config and platform_config.registration_endpoint:
                res.results.append(TestResult('Registration end point found',
                                            True,
                                            True,
                                            platform_config.registration_endpoint))
                res.results.append(TestResult('JWKS end point found',
                                            platform_config.jwks_uri or False,
                                            True,
                                            platform_config.jwks_uri))
                res.results.append(TestResult('Authorization end point found',
                                            platform_config.authorization_endpoint or False,
                                            True,
                                            platform_config.authorization_endpoint))
                res.results.append(TestResult('Token end point found',
                                            platform_config.token_endpoint or False,
                                            True,
                                            platform_config.token_endpoint))
                lms_type = platform_config.lti_config.product_family_code
                res.results.append(TestResult('Platform product found',
                                            lms_type or False,
                                            True,
                                            lms_type))
                reg = registration(lms_type, platform_config.issuer, "verif")
                if reg:
                    # For now we only support LMS - to be added to stored the endpoints
                    # as custom parameters to support any LMS. For now verifying moodle endpoints.
                    res.results.append(TestResult('Endpoints match',
                                                platform_config.jwks_uri==reg.jwks_uri and platform_config.token_endpoint==reg.token_uri
                                                and platform_config.authorization_endpoint==reg.auth_endpoint,
                                                True,
                                                ""))

                init_login = str(request.url.replace(path='/oidc/init', query='dynreg=true', scheme='https'))
                redirect_uri = str(request.url.replace(path='/oidc/launch', query='', scheme='https'))
                tool_conf = base_tool_oidc_conf(name='Robotest', 
                        domain = request.url.hostname,
                        login_uri = init_login,
                        redirect_uri = redirect_uri,
                        ags=True,
                        nrps=True,
                        pii_name=True,
                        dl_label='Add Robotest')
                tool_conf.lti_config.description = "Less clicks, more tests, this is the LTI Robotest!"
                tool_conf.logo_uri =  str(request.url.replace(path='/assets/robotest_logo.png', query='', scheme='https'))
                tool_conf.lti_config.custom_parameters.update({**context_sub_variables, **link_sub_variables})

                res.results.append(TestResult('Tool Config to Register',
                                   True,
                                   True,
                                   "", 
                                   json.dumps(tool_conf, indent=2)))
                registered = register_tool(platform_config.registration_endpoint, tool_conf, registration_token)
                res.results.append(TestResult('Successful registration',
                                   True if registered.client_id else False,
                                   True, 
                                   'Client Id: {client_id}'.format( client_id=registered.client_id ),
                                   json.dumps(registered, indent=2)))
            else:
                res.results.append(TestResult('Registration end point found',
                                            False,
                                            True,
                                            'Cannot register tool without registration endpoint'))

        except:
            res.results.append(TestResult('Error during registration',
                                        False,
                                        True,
                                        traceback.format_exc()))
    return templates.TemplateResponse("results.html", {"request": request, "results": [res], "success": res.success, "showClose": True})

@app.get("/.well-known/jwks.json")
def jwks():
    return get_public_keyset()

@app.get("/.well-known/publickey.pem", response_class=PlainTextResponse)
def jwk_public():
    return get_publickey_pem()

@app.get("/oidc/init")
def oidc_init(request: Request,
              iss:str,
              login_hint: str = None,
              lti_message_hint: str = None,
              client_id: str = None,
              lms: str = 'moodle',
              target_link_uri: str = None):
    cookie = "LTI-" + str(random.randint(0,9999))
    reg = registration(lms, iss, client_id)
    state = {
        'r': reg.__dict__,
        'cookie': cookie
    }
    auth_url = urlparse(reg.auth_endpoint)
    query_params = parse_qsl(auth_url.query)
    query_params.append(('state', json.dumps(state,  separators=(',', ':'))))
    query_params.append(('redirect_uri', str(request.url.replace(path='/oidc/launch', query='', scheme='https'))))
    query_params.append(('scope','openid'))
    query_params.append(('response_type','id_token'))
    query_params.append(('client_id', client_id))
    query_params.append(('response_mode', 'form_post'))
    query_params.append(('nonce',  datetime.now().strftime('%y%m%d%H%M%S')))
    if (login_hint):
        query_params.append(('login_hint', login_hint))
    if (lti_message_hint):
        query_params.append(('lti_message_hint', lti_message_hint))
    redirect_url=urlunparse((auth_url.scheme,
                             auth_url.netloc,
                             auth_url.path,
                             auth_url.params,
                             urlencode(query_params),
                             auth_url.fragment))
    return RedirectResponse(url=redirect_url)

@app.post("/oidc/init")
def oidc_init_post(request: Request,
              iss:str = Form(...),
              clientid: str = None,
              client_id: str = Form(None),
              lms: str = 'moodle',
              target_link_uri:str = Form(...),
              login_hint: str = Form(...),
              lti_message_hint: str = Form(...)):
    return oidc_init(request, iss, login_hint, lti_message_hint, client_id or clientid, lms, target_link_uri)

@app.post("/oidc/launch")
def oidc_launch(request: Request, state: str = Form(...), id_token: str = Form(...)):
    reg = ToolRegistration(**json.loads(state)['r'])
    message = LTIMessage(**reg.decode(id_token))
    if message.message_type == const.dl.request_msg_type:
        return deeplinking(request, reg, message)
    return test_and_show_results(request, reg, message)

def resource_link(name: str, message: LTIMessage, multiple: bool, iframe: bool = False, window: bool = False, points: float = None):
    rl = LTIResourceLink()
    rl.title = name
    rl.text = 'This is a description for {name}'.format(name=name)
    resource_id = 'rl' + str(random.randint(0, 99999))
    rl.url = '{base_url}/deeplink?p1={rid}'.format(base_url=base_url, rid=resource_id)
    rl.custom['resource_id'] = resource_id
    rl.custom['multiple'] = str(message.deep_linking_settings.accept_multiple and multiple)
    rl.custom['lineitems_dl'] = message.grade_service.lineitems
    rl.custom['membership_dl'] = message.membership_service.context_memberships_url if 'membership_service' in message and 'context_memberships_url' in message.membership_service else ''
    if points:
        rl.custom['max_points'] = str(rl.max_points)
        rl.max_points= 10.0
        rl.resource_id = resource_id
    if iframe:
        rl.iframe = DLIFrame()
        rl.iframe.height = 800
    if window:
        rl.window = DLWindow()
        rl.window.targetName = 'robotest-win'

    return rl

def deeplinking(request: Request, reg: ToolRegistration, message: LTIMessage):
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    dlresp0 = DeeplinkResponse()
    dlresp0.data = message.deep_linking_settings.data
    dlresp0.deployment_id = message.deployment_id
    dlresp1 = DeeplinkResponse()
    dlresp1.content_items.append( resource_link( "Not graded (new win) " + today, message, False, False, True ) )
    dlresp1.data = message.deep_linking_settings.data
    dlresp1.deployment_id = message.deployment_id
    dlresp2 = DeeplinkResponse()
    dlresp2.content_items.append( resource_link( "Graded (IFrame) " + today, message, False, True, True, 10.0 ) )
    dlresp2.deployment_id = message.deployment_id
    dlresp3 = DeeplinkResponse()
    dlresp3.content_items.append( resource_link( "Graded (IFrame) " + today, message, True, True, True, 10.0 ) )
    dlresp3.content_items.append( resource_link( "Not graded (new win) " + today, message, True, False, True ) )
    dlresp3.deployment_id = message.deployment_id

    return templates.TemplateResponse("deeplink_autopost.html", {
        "request": request,
        "return_url": message.deep_linking_settings.return_url,
        "jwt_empty": reg.encode(dlresp0),
        "jwt_single": reg.encode(dlresp1),
        "jwt_single_graded": reg.encode(dlresp2),
        "jwt_multiple": reg.encode(dlresp3),
        "name": message.name or 'No name!',
        'multiple': message.deep_linking_settings.accept_multiple
    })

@app.get('/dl')
def testdl(request: Request):
    return templates.TemplateResponse("deeplink_autopost.html", {
        "request": request,
        "name": 'Saul Tigh',
        "return_url": '',
        "jwt_single": ''})

def test_deeplinking(request: Request, message: LTIMessage) -> TestCategory:
    res = TestCategory(name='Deep Linking')
    res.results.append(TestResult('Target link present and with param',
                                    message.target_link_uri and "p1=" in message.target_link_uri,
                                    True,
                                    ''))
    if message.custom:
        res.results.append(TestResult('Custom parameter passed',
                                        'resource_id' in message.custom,
                                        True,
                                        'resource_id: ' + message.custom.get('resource_id', 'None')))
        res.results.append(TestResult('Supports Multiple',
                                        'multiple' in message.custom and message.custom['multiple'] == 'True',
                                        False,
                                        'True if this link was added as part of multiple return.'))
    else:
        res.results.append(TestResult('Custom parameter passed',
                                        False,
                                        True,
                                        'no custom parameters passed back'))

    return res


def test_nrps(reg: ToolRegistration, message: LTIMessage) -> TestCategory:
    res = TestCategory('Names and Role Service (aka Roster)')
    nrps_in_dl = message.custom and 'membership_dl' in message.custom and len(message.custom['membership_dl'])>6,
    res.results.append(TestResult('Service in Deep Linking',
                                     nrps_in_dl,
                                     False,
                                     'Yeah! roster can be queried in deep linking' if nrps_in_dl else 'cannot query roster in deep linking'))
    if message.membership_service and message.membership_service.context_memberships_url:
        res.results.append(TestResult('Service url present',
                                     True,
                                     True,
                                     message.membership_service.context_memberships_url))
        try:
            # we linit to 5 to test limit and paging
            nrps_url = urlparse(message.membership_service.context_memberships_url)
            query_params = parse_qsl(nrps_url.query)
            query_params.append(('limit', 5))
            nrps_limited_url=urlunparse((*nrps_url[0:4],
                                    urlencode(query_params),
                                    nrps_url.fragment))
            print(message.membership_service.context_memberships_url)
            print(nrps_limited_url)
            members = ltiservice_get(reg, Members, nrps_limited_url)
            # members = ltiservice_get(reg, Members, message.membership_service.context_memberships_url)
            # instructors = list(filter(lambda m: )) util to get role from enum
            res.results.append(TestResult('Members loaded',
                                    len(members.members)>0 and not len(members.members) == 5,
                                    True,
                                    '{m} members - 5 is paging boundary so ideally have more than 5 members'.format(m=len(members.members))))
        except Exception as e:
            print(traceback.format_exc())
            res.results.append(TestResult('Members loaded',
                                    False,
                                    True,
                                    str(e)))
    else:
        res.results.append(TestResult('Service Url present',
                                     False,
                                     True,
                                     'Roster service is not available'))
    return res


def test_ags(reg: ToolRegistration, message: LTIMessage) -> TestCategory:
    res = TestCategory('Assignment and Grade Services')
    res.results.append(TestResult('Line items in Deep Linking',
                                     message.custom and 'lineitems_dl' in message.custom and len(message.custom['lineitems_dl'])>6,
                                     False,
                                     ''))
    if message.grade_service.lineitems:
        res.results.append(TestResult('Line items present',
                                     True,
                                     True,
                                     'Can query existing grade book columns for this tool and add new ones'))
    else:
        res.results.append(TestResult('Line items present',
                                     False,
                                     True,
                                     'Cannot query existing grade book columns for this tool nor add new ones'))

    if message.custom and 'max_points' in message.custom:
        res.results.append(TestResult('Line item present',
                                      message.grade_service.lineitem,
                                     True,
                                     ''))
    if message.grade_service.lineitem:
        try:
            lineitem = ltiservice_get(reg, LineItem, message.grade_service.lineitem)
            res.results.append(TestResult('Line item present and queried',
                                     True,
                                     True,
                                     'This link is graded and the line item url can be used to post score for it'))
        except Exception as e:
            print(traceback.format_exc())
            res.results.append(TestResult('Line item loaded',
                                     False,
                                     True,
                                     str(e)))

    return res

def test_substitution_variables(category: str, sub_variables: Dict[str, str], custom_params: Dict[str, str]):
    res = TestCategory(category)
    for key in sub_variables:
        if key in custom_params:
            if custom_params[key]:
                if custom_params[key] == sub_variables[key]:
                    res.results.append(TestResult(sub_variables[key],
                                     False,
                                     False,
                                     'Not substituted'))
                else:
                    res.results.append(TestResult(sub_variables[key],
                                     True,
                                     False,
                                     custom_params[key]))
            else:
                res.results.append(TestResult(sub_variables[key],
                                    True,
                                    False,
                                    'blank means supported but no value'))
        else:
            res.results.append(TestResult(sub_variables[key],
                                False,
                                True,
                                'Missing custom parameter, tool properly configured?'))
    return res


def test_and_show_results(request: Request, reg: ToolRegistration, message: dict):
    results = []
    results.append(test_deeplinking(request, message))
    results.append(test_ags(reg, message))
    results.append(test_nrps(reg, message))
    results.append(test_substitution_variables('Subsitution Variables (resourcelink)', {**context_sub_variables, **link_sub_variables}, message.custom))
    success = all((map(lambda r: r.success, results)))
    return templates.TemplateResponse("results.html", {"request": request, "results": results, "success": success})

@app.get("/test")
def test():
    return const.dl.request_msg_type
