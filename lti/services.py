from typing import Generic, TypeVar, Dict, Type
from lti.ltiregistration import ToolRegistration
import json
import requests

T = TypeVar('T', bound=Dict)

def access_token(registration: ToolRegistration, scope: str, force: bool = False):
    assertion = registration.encode({
        "sub": registration.client_id
    })
    r = requests.post(registration.token_uri, data = {
        "grant_type": "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "scope": scope,
        "client_assertion": assertion
    })
    t = json.loads(r.text)
    return t['access_token']

def ltiservice_get(registration: ToolRegistration, resource_class: Type[T], url: str, params: Dict = {}) -> T:
    if resource_class.read_scope:
        mime = resource_class.mime if resource_class.mime else 'application/json'
        token = access_token( registration, resource_class.read_scope )
        headers = {
            'Authorization': 'Bearer {token}'.format(token=token),
            'Content-Type': mime
        }
        r = requests.get(url, headers=headers, params=params)
        return resource_class(json.loads(r.text))
    raise ValueError("No scope defined for read")