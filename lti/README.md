# `lti`

`lti` is the reusable library portion of this repository. It provides:

- typed dict-like LTI message and service models
- helpers for tool registration and platform configuration
- helpers for AGS/NRPS/deep-linking service calls
- JWKS and signing-key utilities

## Installation

```bash
pip install ltirobotest-lti
```

## Key management

The library no longer creates or writes `private.pem` during import.

Applications should configure signing explicitly:

```python
from lti import load_private_key, get_public_keyset

load_private_key("private.pem")
jwks = get_public_keyset()
```

If no key is configured, the library generates an in-memory key the first time a signing operation needs one. That is convenient for tests, but real deployments should load a persistent private key so the published JWKS stays stable across restarts.

## Development

Run the library tests from the repository root:

```bash
python -m unittest discover lti/tests
```
