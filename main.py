import json
import random
from fastapi import FastAPI, Form
from starlette.responses import PlainTextResponse, RedirectResponse
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from urllib.parse import quote_plus, urlparse, urlunparse, urlencode, parse_qsl

from typing import List
from datetime import datetime

from lti import ToolRegistration, LTIMessage, LTIResourceLink, DeeplinkResponse, DeeplinkSettings, get_public_keyset, get_publickey_pem, const, registration
from robotest import TestCategory, TestResult

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/broken")
def read_root(request: Request):
    return templates.TemplateResponse("broken.html", {"request": request})

@app.get("/results")
def read_root(request: Request):
    cat1 = TestCategory(name='category 1')
    cat1.results.append(TestResult('res1', True, True, 'You passed this easily'))
    cat1.results.append(TestResult('res2', True, True, 'You passed this easily'))
    cat1.results.append(TestResult('res3', True, True, 'You passed this easily'))
    return templates.TemplateResponse("results.html", {"request": request, "results": [cat1]})

@app.get("/.well-known/jwks.json")
def jwks():
    return get_public_keyset()

@app.get("/.well-known/publickey.pem", response_class=PlainTextResponse)
def jwks():
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
    print(query_params)
    print(auth_url)
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
    return test_and_show_results(request, message)

def resource_link(name: str, deep_linking_settings: DeeplinkSettings, points: float = None):
    rl = LTIResourceLink()
    rl.title = name
    resource_id = 'rl1'
    rl.url = 'https://robotest.theedtech.dev/deeplink?p1=' + resource_id
    rl.custom['resource_id'] = resource_id
    rl.custom['multiple'] = deep_linking_settings.accept_multiple
    if ( points ):
        rl.custom['maxPoints'] = str(rl.max_points)
        rl.max_points= 10.0
        rl.resource_id = resource_id
    return rl

def deeplinking(request: Request, reg: ToolRegistration, message: LTIMessage):
    dlresp0 = DeeplinkResponse()
    dlresp0.data = message.deep_linking_settings.data
    dlresp0.deployment_id = message.deployment_id
    dlresp1 = DeeplinkResponse()
    dlresp1.content_items.append( resource_link( "Not graded", message.deep_linking_settings ) )
    dlresp1.data = message.deep_linking_settings.data
    dlresp1.deployment_id = message.deployment_id
    dlresp2 = DeeplinkResponse()
    dlresp2.content_items.append( resource_link( "Graded", message.deep_linking_settings, 10.0 ) )
    dlresp2.deployment_id = message.deployment_id
    dlresp3 = DeeplinkResponse()
    dlresp3.content_items.append( resource_link( "Graded", message.deep_linking_settings, 10.0 ) )
    dlresp3.content_items.append( resource_link( "Not graded", message.deep_linking_settings ) )
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

def test_and_show_results(request: Request, message: dict):
    return templates.TemplateResponse("results.html", {"request": request})

@app.get("/test")
def test():
    return const.dl.request_msg_type
