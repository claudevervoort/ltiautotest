from jose import jwt
from datetime import datetime
from lti.jwks import get_remote_keyset, get_webkey
from lti.spi import log

TOKEN_TTL = 300

class ToolRegistration(object):

    def __init__(self, iss: str, client_id: str, auth_endpoint:str, token_uri: str, jwks_uri: str):
        self.iss = iss
        self.client_id = client_id
        self.auth_endpoint = auth_endpoint
        self.token_uri = token_uri
        self.jwks_uri = jwks_uri
        log("Registration: {0}", str(self.__dict__))
        

    def decode(self, token:str) -> dict:
        return jwt.decode(token, 
                          get_remote_keyset(self.jwks_uri),
                          audience = self.client_id,
                          issuer = self.iss)

    def encode(self, claims: dict, from_client: bool = True) -> str:
        if from_client:
            claims['iss'] = self.client_id
        else:
            claims['iss'] = self.iss
            claims['aud'] = self.client_id
        if not 'iat' in claims:
            claims['iat'] = int(datetime.now().timestamp())
        if not 'exp' in claims:
            claims['exp'] = int(datetime.now().timestamp()) + TOKEN_TTL
        return jwt.encode(claims, get_webkey(), algorithm='RS256', headers={'kid': get_webkey()['kid']})


def registration( lms: str, iss: str, client_id: str) -> ToolRegistration:
    if (lms.lower() == 'moodle'):
        return ToolRegistration(iss, client_id, iss+'/mod/lti/auth.php', iss+'/mod/lti/token.php', iss+'/mod/lti/certs.php')
    return None