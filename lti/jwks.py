import requests
import json
from uuid import uuid4
from jose import jwk
from jose.backends.base import Key

from Crypto.PublicKey import RSA
from base64 import b64encode, urlsafe_b64encode

key = RSA.generate(2048)
kid = str(uuid4())

def base64urlUInt_encode(val):
    bytes = val.to_bytes((val.bit_length() +7) // 8, byteorder='big')
    return urlsafe_b64encode(bytes).decode()

public_keyset = {'keys':[
    {
        'kty': 'RSA',
        'alg': 'RS256',
        'kid': kid,
        'use': 'sig',
        'e':  base64urlUInt_encode(key.publickey().e),
        'n':  base64urlUInt_encode(key.publickey().n)
    }
]}

webkey = {
    'kty': 'RSA',
    'alg': 'RS256',
    'use': 'sig',
    'kid': kid,
    'e': base64urlUInt_encode(key.e),
    'd': base64urlUInt_encode(key.d),
    'n': base64urlUInt_encode(key.n)
}


def get_public_keyset() -> dict:
    return public_keyset

def get_webkey() -> dict:
    return webkey


def get_remote_keyset(jwks_uri:str) -> dict:
    keyset = json.loads(requests.get(jwks_uri).text)
    for k in keyset[ 'keys' ]:
        if not 'alg' in k:
            k['alg'] = 'RS256'
    return keyset


def get_remote_public_key(jwks_uri: str, kid: str) -> Key:
    keyset = get_keyset(jwks_uri)
    keys = [ k for k in keyset[ 'keys' ] if k['kid'] == kid ]
    if len(keys) == 1:
        return jwk.construct( keys[ 0 ] )
    return None

