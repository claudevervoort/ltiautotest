from jose import jwt
from lti.jwks import get_remote_keyset, get_webkey

class ToolRegistration(object):

    def __init__(self, iss: str, client_id: str, token_uri: str, jwks_uri: str):
        self.iss = iss
        self.client_id = client_id
        self.token_uri = token_uri
        self.jwks_uri = jwks_uri

    def decode(self, token:str) -> dict:
        return jwt.decode(token, get_remote_keyset(self.jwks_uri))

    def encode(self, claims: dict, from_client: bool = True) -> str:
        print(get_webkey())
        if from_client:
            claims['iss'] = self.client_id
        else:
            claims['iss'] = self.iss
            claims['aud'] = self.client_id
        return jwt.encode(claims, get_webkey(), algorithm='RS256')
        