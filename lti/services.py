from typing import Generic, TypeVar, Dict, Type
from lti.ltiregistration import ToolRegistration
import json
import requests

T = TypeVar('T', bound=Dict)

def access_token(registration: ToolRegistration, scope: str, force: bool = False):
    assertion = registration.encode({
        "sub": registration.client_id
    })
    r = requests.get(registration.token_uri, params={
        "grant_type": "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "scope": scope,
        "client_assertion": assertion
    })
    t = json.loads(r.text)
    return 

def get(registration: ToolRegistration, resource_class: Type[T]) -> T:
    print(resource_class.mime)
    return resource_class({})


#class RESTService(Generic[T]):
#
#    def __init__(self, resource_class: T, read_scope: str = None, full_scope: str = None):
#    def get(self, endpoint: str) -> T:
#        return T.