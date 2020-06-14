# ltiautotest

http://localhost:8000/oidc/init?iss=https://test&target_link_uri=http://ttt&login_hint=hint&auth_endpoint=http://localhost:8001?t=1&token_endpoint=http://token&jwks_uri=http://jwks

http://localhost:8000/test/jwks?jwks_uri=https%3A%2F%2Fqa-gateway.cengage.com%2F.well-known%2Fjwks.json&kid=4b1e2d0e-6596-4ea0-ba9b-e9d5b1c868ee

              target_link_uri: str, 
              login_hint: str,
              auth_endpoint: str,
              token_endpoint: str,
              jwks_uri: str,


uvicorn main:app --reload --port 8001 