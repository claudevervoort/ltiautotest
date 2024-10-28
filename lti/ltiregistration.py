from jose import jwt
from datetime import datetime
from lti.jwks import get_remote_keyset, get_webkey
from lti.spi import log
from lti.gen_model import PlatformOIDCConfig, ToolOIDCConfig, MessageDef, Oauth11Consumer
import requests
import json
import hashlib
from .const import const
import uuid
from urllib.parse import urlencode

TOKEN_TTL = 300

class ToolRegistration(object):

    def __init__(self, iss: str, client_id: str, auth_endpoint:str, token_uri: str, jwks_uri: str, audience: str = None):
        self.iss = iss
        self.client_id = client_id
        self.auth_endpoint = auth_endpoint
        self.token_uri = token_uri
        self.jwks_uri = jwks_uri
        self.audience = audience
        log("Registration: {0}", str(self.__dict__))

    def decode(self, token:str) -> dict:
        return jwt.decode(token, 
                          get_remote_keyset(self.jwks_uri),
                          audience = self.client_id,
                          issuer = self.iss)

    def encode(self, claims: dict, from_client: bool = True, for_token: bool = False) -> str:
        if from_client:
            claims['iss'] = self.client_id
            claims['sub'] = self.client_id
            claims['jti'] = str(uuid.uuid4())
            if for_token:
                claims['aud'] = self.audience if self.audience else self.iss
            else:
                claims['nonce'] = str(uuid.uuid4())
                claims['aud'] = self.iss
                claims['nonce'] = claims['jti']
        else:
            claims['iss'] = self.iss
            claims['aud'] = self.client_id
        if not 'iat' in claims:
            claims['iat'] = int(datetime.now().timestamp())
        if not 'exp' in claims:
            claims['exp'] = int(datetime.now().timestamp()) + TOKEN_TTL
        return jwt.encode(claims, get_webkey(), algorithm='RS256', headers={'kid': get_webkey()['kid']})

def concat(base: str, path: str) -> str:
    if path.startswith('http'):
        return path
    return base + path

def registration( lms: str, iss: str, client_id: str, oidc_auth : str = None, token_url: str = None, keyset_url: str = None) -> ToolRegistration:
    if lms.lower() == 'moodle':
        return ToolRegistration(iss, client_id, iss+'/mod/lti/auth.php', iss+'/mod/lti/token.php', iss+'/mod/lti/certs.php')
    if lms.lower() == 'd2l':
        return ToolRegistration(iss, client_id, iss+'/d2l/lti/authenticate', 'https://auth.brightspace.com/core/connect/token', iss+'/d2l/.well-known/jwks', audience="https://api.brightspace.com/auth/token")
    if lms.lower().startswith('sakai') and token_url:
        return ToolRegistration(iss, client_id, iss+'/imsoidc/lti13/oidc_auth', iss+'/imsblis/lti13/token/'+token_url, iss+'/imsblis/lti13/keyset')
    if iss and token_url and oidc_auth and keyset_url:
        return ToolRegistration(iss, client_id, concat(iss, oidc_auth), concat(iss, token_url), concat(iss, keyset_url))
    if iss == 'https://schoology.schoology.com':
        return ToolRegistration(iss, client_id, 'https://lti-service.svc.schoology.com/lti-service/authorize-redirect', 'https://lti-service.svc.schoology.com/lti-service/access-token', 'https://lti-service.svc.schoology.com/lti-service/.well-known/jwks')
    return None


def trim(iss: str, url: str):
    if url.startswith(iss):
        return url[len(iss):]
    return url

def append_regextra( login_uri: str, lms: str, platform_config: PlatformOIDCConfig) -> str:
    """Append bits to login reg to be able to reconstruct the registration (since this app has no db)"""
    if lms.lower().startswith('sakai'):
        return f"{login_uri}&lms=sakai&token_url={platform_config.token_endpoint.split('/')[-1]}"
    elif lms.lower() == 'generic':
        iss = platform_config.issuer
        return f"{login_uri}&lms=generic&oidc_auth={urlencode(trim(iss, platform_config.authorization_endpoint))}&token_url={urlencode(trim(iss, platform_config.token_endpoint))}&keyset_url={urlencode(trim(iss, platform_config.jwks_uri))}"
    return f"{login_uri}&lms={lms}"

def get_platform_config( url: str) -> PlatformOIDCConfig:
    headers = {
        'Accept': 'application/json'
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return PlatformOIDCConfig(json.loads(r.text))

def register_tool( url: str, config: ToolOIDCConfig, token:str = None) -> ToolOIDCConfig:
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json'
    }
    if token:
        headers['Authorization'] = 'Bearer {token}'.format(token=token)
    r = requests.post(url, headers=headers, json=config)
    r.raise_for_status()
    return ToolOIDCConfig(json.loads(r.text))

def get_tool_configuration( url: str, token: str = None) -> ToolOIDCConfig:
    headers = {
        'Accept': 'application/json',
    }
    if token:
        headers['Authorization'] = 'Bearer {token}'.format(token=token)
    r = requests.get(url, headers=headers)
    print('Res get conf '+r.text)
    if r.status_code==404:
        return None
    r.raise_for_status()
    return ToolOIDCConfig(json.loads(r.text))

        
def base_tool_oidc_conf(*,name:str, 
                        domain:str, 
                        login_uri: str, 
                        redirect_uri: str,  
                        jwks_uri: str = None,
                        dl_label: str = None,
                        dl_url: str = None, 
                        base_url:str = None, 
                        pii_name: bool = False, 
                        pii_email: bool = False, 
                        ags: bool = False, 
                        nrps: bool = False,
                        dls: bool = False) -> ToolOIDCConfig:
    if not jwks_uri:
        jwks_uri = 'https://{domain}/.well-known/jwks.json'.format(domain=domain)
    if not base_url:
        base_url = 'https://{domain}'.format(domain=domain)
    tool_conf_json = """
    {{
        "application_type": "web",
        "response_types": ["id_token"],
        "grant_types": ["implicit", "client_credentials"],
        "initiate_login_uri": "{login_uri}",
        "redirect_uris": ["{redirect_uri}"],
        "client_name": "{name}",
        "jwks_uri": "{jwks_uri}",
        "token_endpoint_auth_method": "private_key_jwt",
        "id_token_signed_response_alg": "RS256",
        "https://purl.imsglobal.org/spec/lti-tool-configuration": {{
            "domain": "{domain}",
            "target_link_uri": "{base_url}",
            "custom_parameters": {{
            }},
            "claims": ["iss", "sub"],
            "messages": [
            ]
        }}
    }}
    """.format(name=name, jwks_uri=jwks_uri, login_uri=login_uri, 
               redirect_uri=redirect_uri, domain=domain, base_url=base_url)
    tool_conf = ToolOIDCConfig(**json.loads(tool_conf_json))
    scopes = ['openid']
    if dl_label:
        if not dl_url:
            dl_url = base_url
        dl_message = '''
                {{
                    "type": "LtiDeepLinkingRequest",
                    "target_link_uri": "{dl_url}",
                    "label": "{dl_label}",
                    "placements": ["ContentArea", "RichTextEditor"]
                }}
        '''.format(dl_label=dl_label, dl_url=dl_url)
        tool_conf.lti_config.messages.append(MessageDef(**json.loads(dl_message)))
    if pii_email:
        tool_conf.lti_config.claims.append('email')
    if pii_name:
        tool_conf.lti_config.claims.extend(["name", "given_name", "family_name"])
    if ags:
        scopes.extend([
            "https://purl.imsglobal.org/spec/lti-ags/scope/lineitem",
            "https://purl.imsglobal.org/spec/lti-ags/scope/result.readonly",
            "https://purl.imsglobal.org/spec/lti-ags/scope/score"])
    if nrps:
        scopes.append('https://purl.imsglobal.org/spec/lti-nrps/scope/contextmembership.readonly')
    if dls:
        scopes.extend([
            "https://purl.imsglobal.org/spec/lti-dl/scope/contentitem.read",
            "https://purl.imsglobal.org/spec/lti-dl/scope/contentitem.update"])
    tool_conf.scope = " ".join(scopes)
    return tool_conf

def add_coursenav_message(registration: ToolOIDCConfig, label: str, 
                          url: str = None, allowLearners: bool = True, params: dict = {}):
    coursenav = MessageDef()
    coursenav.type = const.cnav.msg_type
    coursenav.label = label
    if url:
        coursenav.target_link_uri = url
    if not allowLearners:
        coursenav.roles = ['http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor']
    coursenav.custom_parameters = params
    registration.lti_config.messages.append(coursenav)

def verify_11_oauth(consumer:Oauth11Consumer, secret:str) -> bool:
    s = hashlib.sha256()
    s.update(consumer.key.encode('utf-8'))
    s.update(secret.encode('utf-8'))
    s.update(consumer.nonce.encode('utf-8'))
    print(s.hexdigest())
    print(consumer.sign)
    return consumer.sign == s.hexdigest()
