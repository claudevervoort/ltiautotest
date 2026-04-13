from importlib import import_module

from ._version import __version__
from .const import const
from . import gen_model as _gen_model

_LAZY_EXPORTS = {
    "ToolRegistration": ".ltiregistration",
    "add_coursenav_message": ".ltiregistration",
    "append_regextra": ".ltiregistration",
    "base_tool_oidc_conf": ".ltiregistration",
    "get_platform_config": ".ltiregistration",
    "get_tool_configuration": ".ltiregistration",
    "register_tool": ".ltiregistration",
    "registration": ".ltiregistration",
    "verify_11_oauth": ".ltiregistration",
    "configure_private_key": ".jwks",
    "generate_private_key": ".jwks",
    "get_public_keyset": ".jwks",
    "get_publickey_pem": ".jwks",
    "get_webkey": ".jwks",
    "load_private_key": ".jwks",
    "save_private_key": ".jwks",
    "access_token": ".services",
    "ltiservice_get": ".services",
    "ltiservice_get_array": ".services",
    "ltiservice_getjson": ".services",
    "ltiservice_mut": ".services",
    "log_and_raise_for_status": ".services",
    "merge": ".services",
    "next": ".services",
}

for _name in dir(_gen_model):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_gen_model, _name)

__all__ = ["__version__", "const", *_LAZY_EXPORTS.keys()]
__all__.extend(name for name in dir(_gen_model) if not name.startswith("_"))


def __getattr__(name):
    module_name = _LAZY_EXPORTS.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module = import_module(module_name, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value
