import json
from fastapi import FastAPI, Form
from starlette.responses import PlainTextResponse, RedirectResponse
from starlette.requests import Request

from urllib.parse import quote_plus, urlparse, urlunparse, urlencode, parse_qsl

from typing import List
from datetime import datetime

from lti import LTIPlatform, LTIMessage, get_public_keyset, const

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/.well-known/jwks.json")
def jwks():
    return get_public_keyset()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/oidc/init")
def oidc_init(request: Request,
              iss:str,
              client_id: str,
              target_link_uri: str, 
              auth_endpoint: str,
              token_endpoint: str,
              jwks_uri: str,
              login_hint: str = None,
              lti_message_hint: str = None):
    print(request.url)
    state = {
        'iss': iss,
        'client_id': client_id,
        'jwks_uri': jwks_uri,
        'token_uri': token_endpoint
    }
    auth_url = urlparse(auth_endpoint)
    query_params = parse_qsl(auth_url.query)
    query_params.append(('state', json.dumps(state,  separators=(',', ':'))))
    query_params.append(('redirect_uri', str(request.url.replace(path='/oidc/launch', query=''))))
    query_params.append(('scope','openid'))
    query_params.append(('response_type','id_token'))
    query_params.append(('client_id', client_id))
    query_params.append(('response_mode', 'form_post'))
    query_params.append(('nonce',  datetime.now().strftime('%y%m%d%H%M%S')))
    if (login_hint):
        query_params.append(('login_hint', login_hint))
    if (lti_message_hint):
        query_params.append(('lti_message_hint', lti_message_hint))

    redirect_url=urlunparse((auth_url.scheme, auth_url.netloc, auth_url.path, auth_url.params, urlencode(query_params), auth_url.fragment))
    return RedirectResponse(url=redirect_url)

@app.post("/oidc/launch")
def oidc_launch(state: str = Form(...), id_token: str = Form(...)):
    platform = LTIPlatform(**json.loads(state))
    message = LTIMessage(platform.decode(id_token))
    if message.message_type == const.dl.request_msg_type:
        return deeplinking_automatic(message)
    return test_and_show_results(message)

def deeplinking_automatic(message: LTIMessage):
    
    pass

def test_and_show_results(message: dict):
    pass

@app.get("/test")
def test():
    return const.dl.request_msg_type
