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

from lti import LineItem, ToolRegistration, LTIMessage, LTIResourceLink, DeeplinkResponse, DeeplinkSettings,get_public_keyset, get_publickey_pem, const, registration, ltiservice_get

from robotest.test_results import TestCategory, TestResult

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("moodleinstructions.html", {"request": request, "base_url": base_url})

@app.get("/broken")
def read_broken(request: Request):
    return templates.TemplateResponse("broken.html", {"request": request})

@app.get("/results")
def read_results(request: Request,
                 success: bool = True):
    cat1 = TestCategory(name='category 1')
    cat1.results.append(TestResult('res1', True, True, 'You passed this easily'))
    cat1.results.append(TestResult('res2', True, True, 'You passed this easily'))
    cat1.results.append(TestResult('res3', success, True, 'You passed this easily'))
    print( cat1.success )

    return templates.TemplateResponse("results.html", {"request": request, "results": [cat1], "success": cat1.success})

@app.get("/register")
def register(request: Request, openid_configuration: str, registration_token: str):
    return templates.TemplateResponse("registration_completed.html", {"request": request})

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
              client_id: str = None,
              lms: str = 'moodle',
              target_link_uri:str = Form(...),
              login_hint: str = Form(...),
              lti_message_hint: str = Form(...)):
    return oidc_init(request, iss, login_hint, lti_message_hint, client_id, lms, target_link_uri)

@app.post("/oidc/launch")
def oidc_launch(request: Request, state: str = Form(...), id_token: str = Form(...)):
    reg = ToolRegistration(**json.loads(state)['r'])
    message = LTIMessage(**reg.decode(id_token))
    if message.message_type == const.dl.request_msg_type:
        return deeplinking(request, reg, message)
    return test_and_show_results(request, reg, message)

def resource_link(name: str, message: LTIMessage, multiple: bool, points: float = None):
    rl = LTIResourceLink()
    rl.title = name
    resource_id = 'rl' + str(random.randint(0, 99999))
    rl.url = '{base_url}/deeplink?p1={rid}'.format(base_url=base_url, rid=resource_id)
    rl.custom['resource_id'] = resource_id
    rl.custom['multiple'] = str(message.deep_linking_settings.accept_multiple and multiple)
    rl.custom['lineitems_dl'] = message.grade_service.lineitems
    if ( points ):
        rl.custom['max_points'] = str(rl.max_points)
        rl.max_points= 10.0
        rl.resource_id = resource_id
    return rl

def deeplinking(request: Request, reg: ToolRegistration, message: LTIMessage):
    dlresp0 = DeeplinkResponse()
    dlresp0.data = message.deep_linking_settings.data
    dlresp0.deployment_id = message.deployment_id
    dlresp1 = DeeplinkResponse()
    dlresp1.content_items.append( resource_link( "Not graded", message, False ) )
    dlresp1.data = message.deep_linking_settings.data
    dlresp1.deployment_id = message.deployment_id
    dlresp2 = DeeplinkResponse()
    dlresp2.content_items.append( resource_link( "Graded", message, False, 10.0 ) )
    dlresp2.deployment_id = message.deployment_id
    dlresp3 = DeeplinkResponse()
    dlresp3.content_items.append( resource_link( "Graded", message, True, 10.0 ) )
    dlresp3.content_items.append( resource_link( "Not graded", message, True ) )
    dlresp3.deployment_id = message.deployment_id

    return templates.TemplateResponse("deeplink_autopost.html", {
        "request": request,
        "return_url": message.deep_linking_settings.return_url,
        "jwt_empty": reg.encode(dlresp0),
        "jwt_single": reg.encode(dlresp1),
        "jwt_single_graded": reg.encode(dlresp2),
        "jwt_multiple": reg.encode(dlresp3),
        })

@app.get('/dl')
def testdl(request: Request):
    return templates.TemplateResponse("deeplink_autopost.html", {
        "request": request,
        "return_url": '',
        "jwt_single": ''})

def test_deeplinking(request: Request, message: LTIMessage) -> TestCategory:
    res = TestCategory(name='Deep Linking')
    res.results.append(TestResult('URL contains deep link param',
                                    'rl' in request.query_params,
                                    True,
                                    ''))
    if message.custom:
        res.results.append(TestResult('Custom parameter passed',
                                        'resource_id' in message.custom,
                                        True,
                                        'resource_id: ' + message.custom.get('resource_id')))
        res.results.append(TestResult('Supports Multiple',
                                        'multiple' in message.custom and message.custom['multiple'] == 'True',
                                        False,
                                        'Launch from Multiple return'))
    else:
        res.results.append(TestResult('Custom parameter passed',
                                        False,
                                        True,
                                        'no custom parameters passed back'))

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
                                     ''))
    else:
        res.results.append(TestResult('Line items present',
                                     False,
                                     True,
                                     ''))

    if message.custom and 'max_points' in message.custom:
        res.results.append(TestResult('Line item present',
                                      message.grade_service.lineitem,
                                     True,
                                     ''))
    if message.grade_service.lineitem:
        try:
            lineitem = ltiservice_get(reg, LineItem, message.grade_service.lineitem)
            res.results.append(TestResult('Line item loaded',
                                     True,
                                     True,
                                     lineitem.id))
        except Exception as e:
            print(traceback.format_exc())
            res.results.append(TestResult('Line item loaded',
                                     False,
                                     True,
                                     str(e)))

    return res

def test_and_show_results(request: Request, reg: ToolRegistration, message: dict):
    results = []
    results.append(test_deeplinking(request, message))
    results.append(test_ags(reg, message))
    success = all((map(lambda r: r.success, results)))
    return templates.TemplateResponse("results.html", {"request": request, "results": results, "success": success})

@app.get("/test")
def test():
    return const.dl.request_msg_type
