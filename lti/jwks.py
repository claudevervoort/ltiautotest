import requests
import json
from jose import jwk
from jose.backends.base import Key

def get_keyset(jwks_uri:str) -> dict:
    keyset = json.loads(requests.get(jwks_uri).text)
    for k in keyset[ 'keys' ]:
        if not 'alg' in k:
            k['alg'] = 'RS256'
    return keyset


def get_public_key(jwks_uri: str, kid: str) -> Key:
    keyset = get_keyset(jwks_uri)
    keys = [ k for k in keyset[ 'keys' ] if k['kid'] == kid ]
    if len(keys) == 1:
        return jwk.construct( keys[ 0 ] )
    return None

