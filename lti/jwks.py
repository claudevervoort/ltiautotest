import hashlib
import json
import os
from base64 import urlsafe_b64encode
from pathlib import Path

import requests
from Crypto.PublicKey import RSA
from jose import jwk
from jose.backends.base import Key

DEFAULT_PRIVATE_KEY_PATH = "private.pem"

_key = None
_kid = None
_public_keyset = None
_webkey = None

def base64urlUInt_encode(val):
    bytes = val.to_bytes((val.bit_length() +7) // 8, byteorder='big')
    return urlsafe_b64encode(bytes).decode()

def _clear_cached_views():
    global _kid, _public_keyset, _webkey
    _kid = None
    _public_keyset = None
    _webkey = None


def _set_key(private_key: RSA.RsaKey):
    global _key
    _key = private_key
    _clear_cached_views()
    return _key


def _resolve_private_key_path(private_key_path: str = None) -> Path:
    env_override = os.environ.get("LTI_PRIVATE_KEY_PATH")
    key_path = private_key_path or env_override or DEFAULT_PRIVATE_KEY_PATH
    return Path(key_path)


def _build_kid(private_key: RSA.RsaKey) -> str:
    keyhash = hashlib.sha256()
    keyhash.update(private_key.exportKey("PEM"))
    return keyhash.hexdigest()


def configure_private_key(private_key_pem: str):
    if isinstance(private_key_pem, str):
        private_key_pem = private_key_pem.encode()
    return _set_key(RSA.import_key(private_key_pem))


def load_private_key(private_key_path: str = None):
    key_path = _resolve_private_key_path(private_key_path)
    with key_path.open("rb") as handle:
        return configure_private_key(handle.read())


def generate_private_key(bits: int = 2048):
    return _set_key(RSA.generate(bits))


def save_private_key(private_key_path: str = None):
    private_key = get_private_key()
    key_path = _resolve_private_key_path(private_key_path)
    key_path.write_bytes(private_key.exportKey("PEM"))
    return str(key_path)


def get_private_key():
    global _key
    if _key is not None:
        return _key

    default_path = _resolve_private_key_path()
    if default_path.exists():
        return load_private_key(str(default_path))

    return generate_private_key()


def get_key_id() -> str:
    global _kid
    if _kid is None:
        _kid = _build_kid(get_private_key())
    return _kid


def _get_public_keyset():
    global _public_keyset
    if _public_keyset is None:
        private_key = get_private_key()
        _public_keyset = {"keys": [
            {
                "kty": "RSA",
                "alg": "RS256",
                "kid": get_key_id(),
                "use": "sig",
                "e": base64urlUInt_encode(private_key.publickey().e),
                "n": base64urlUInt_encode(private_key.publickey().n),
            }
        ]}
    return _public_keyset


def _get_webkey():
    global _webkey
    if _webkey is None:
        private_key = get_private_key()
        _webkey = {
            "kty": "RSA",
            "alg": "RS256",
            "use": "sig",
            "kid": get_key_id(),
            "e": base64urlUInt_encode(private_key.e),
            "d": base64urlUInt_encode(private_key.d),
            "n": base64urlUInt_encode(private_key.n),
        }
    return _webkey


def get_public_keyset() -> dict:
    return _get_public_keyset()

def get_publickey_pem() -> str:
    return get_private_key().publickey().exportKey('PEM')

def get_webkey() -> dict:
    return _get_webkey()


def get_remote_keyset(jwks_uri:str) -> dict:
    keyset = json.loads(requests.get(jwks_uri).text)
    for k in keyset[ 'keys' ]:
        if not 'alg' in k:
            k['alg'] = 'RS256'
    return keyset


def get_remote_public_key(jwks_uri: str, kid: str) -> Key:
    keyset = get_remote_keyset(jwks_uri)
    keys = [ k for k in keyset[ 'keys' ] if k['kid'] == kid ]
    if len(keys) == 1:
        return jwk.construct( keys[ 0 ] )
    return None
