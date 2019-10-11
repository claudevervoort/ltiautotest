from jose import jwt
from lti.jwks import get_keyset, get_webkey

class LTIPlatform(object):

    def __init__(self, iss: str, client_id: str, token_uri: str, jwks_uri: str):
        self.iss = iss
        self.client_id = client_id
        self.token_uri = token_uri
        self.jwks_uri = jwks_uri

    def decode(self, token:str) -> dict:
        return jwt.decode(token, get_keyset(self.jwks_uri))

    def encode(self, claims: dict) -> str:
        print(get_webkey())
        return jwt.encode(claims, get_webkey(), algorithm='RS256')
        