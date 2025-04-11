from typing import Generic, TypeVar, Dict, Type, List
from lti.ltiregistration import ToolRegistration
import json
import requests
import re

T = TypeVar('T', bound=Dict)
link_anchor_re = re.compile(r"<([^\s]*)>")

def log_and_raise_for_status(res, payload=None):
    if res.status_code>=400:
        if payload:
            print(json.dumps(payload))
        print(res.text)
    res.raise_for_status()

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
    assertion = registration.encode({}, for_token=True)
    r = requests.post(registration.token_uri, data = {
        "grant_type": "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "scope": scope,
        "client_assertion": assertion
    })
    log_and_raise_for_status(r)
    t = json.loads(r.text)
    return t['access_token']

def ltiservice_get_array(registration: ToolRegistration, resource_class: Type[T], url: str, params: Dict = {}, load_all: bool = True) -> List[T]:
    if hasattr(resource_class, 'read_scope'):
        mime = resource_class.mime_collection if hasattr(resource_class, 'mime_collection') else 'application/json'
        r = ltiservice_getjson(registration, mime, resource_class.read_scope, url, params)
        response = list(map(lambda d: resource_class(d), r["response"]))
        if (load_all and r["next"]):
            remaining = ltiservice_get_array(registration, resource_class, r["next"] , params)
            response.extend(remaining)
        return response
    raise ValueError("No scope defined for read")

def ltiservice_get(registration: ToolRegistration, resource_class: Type[T], url: str, params: Dict = {}, load_all: bool = True) -> T:
    if hasattr(resource_class, 'read_scope'):
        mime = resource_class.mime if hasattr(resource_class, 'mime') else 'application/json'
        r = ltiservice_getjson(registration, mime, resource_class.read_scope, url, params)
        response = resource_class(r["response"])
        if (load_all and r["next"] and hasattr(resource_class, 'collection_attribute')):
            remaining = ltiservice_get(registration, resource_class, r["next"], params)
            response[resource_class.collection_attribute].extend(remaining[resource_class.collection_attribute])
        return response
    raise ValueError("No scope defined for read")

def ltiservice_getjson(registration: ToolRegistration, mime : str, scope: str,  url: str, params: Dict = {}):
    token = access_token( registration, scope )
    headers = {
        'Authorization': 'Bearer {token}'.format(token=token),
        'Accept': mime
    }
    r = requests.get(url, headers=headers, params=params)
    log_and_raise_for_status(r)
    return {
        "response": json.loads(r.text),
        "next": next(r.headers)
    }

def ltiservice_mut(registration: ToolRegistration, url: str, payload: T, isput: bool = False) -> T:
    resource_class = payload.__class__
    if hasattr(resource_class, 'path_suffix'):
        suffix = resource_class.path_suffix
        parts = url.split("?", 1)
        url = '{p}/{s}'.format(p=parts[0].rstrip('/'), s=suffix) if len(parts) == 1 else '/{s}?'.format(s=suffix).join([parts[0].rstrip('/'), parts[1]])
    if hasattr(resource_class, 'write_scope'):
        mime = resource_class.mime if hasattr(resource_class, 'mime') else 'application/json'
        token = access_token( registration, resource_class.write_scope )
        headers = {
            'Authorization': 'Bearer {token}'.format(token=token),
            'Content-Type': mime
        }
        r = (requests.put if isput else requests.post)(url, headers=headers, data=json.dumps(payload))
        log_and_raise_for_status(r, payload=payload)
        if r.text and r.headers['Content-Type'] and r.headers['Content-Type'].startswith(mime):
            response = resource_class(json.loads(r.text))
        else:
            response = None
        return response
    raise ValueError("No scope defined for write")

