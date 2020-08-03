from typing import Generic, TypeVar, Dict, Type
from lti.ltiregistration import ToolRegistration
import json
import requests
import re

T = TypeVar('T', bound=Dict)
link_anchor_re = re.compile(r"<([^\s]*)>")

def merge(a:dict, b:dict):
    m = {**a, **b}
    for attr, value in m.items():
        if (type(value)==list and attr in a):
            m[attr] = a[attr][:]
            m[attr][len(a):] = b[attr]
    return m

def next(headers: Dict):
    if ('Link' in headers):
        links = headers['Link'].split(',')
        print(links)
        nexts = list(filter(lambda l: 'rel=next' in l or 'rel=\"next\"' in l, links))
        if len(nexts)>0:
            match = link_anchor_re.search(nexts[0])
            if match:
                return match.group(1)
    return None

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

def ltiservice_get(registration: ToolRegistration, resource_class: Type[T], url: str, params: Dict = {}, load_all: bool = True) -> T:
    if resource_class.read_scope:
        mime = resource_class.mime if resource_class.mime else 'application/json'
        token = access_token( registration, resource_class.read_scope )
        headers = {
            'Authorization': 'Bearer {token}'.format(token=token),
            'Accept': mime
        }
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        response = resource_class(json.loads(r.text))
        if (load_all and next(r.headers)):
            remaining = ltiservice_get(registration, resource_class, next(r.headers), params)
            if type(response) is list:
                response.extend(remaining)
            else:
                response[resource_class.collection_attribute].extend(remaining)
        return response
    raise ValueError("No scope defined for read")