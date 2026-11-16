# Auth helpers (non-generated)

OpenAPI does not describe Keycloak’s OAuth2 endpoints. These thin wrappers call `/.well-known/openid-configuration` and token endpoints for:

- **PKCE** (web + mobile public clients)
- **Device Authorization Grant** (CLI / embedded)
- **Client Credentials** (M2M)
- **API key** headers for the gateway (`X-Api-Key` + `X-Tenant-ID`)

| Language | Path |
|----------|------|
| TypeScript | [typescript/keycloakAuth.ts](typescript/keycloakAuth.ts) |
| Python | [python/keycloak_auth.py](python/keycloak_auth.py) |

Regenerate REST clients separately with `scripts/sdk-gen/generate_rest_sdks.py`; these files are maintained by hand.

Both languages have mocked wire contracts, including PKCE and failed device polls.
These are one-request examples, not complete login clients. Callers validate state,
apply the device polling interval/backoff and expiry, and securely store tokens.
Python raises `httpx.HTTPStatusError` on failed polls; TypeScript rejects. Client
credentials are server-only and must never be embedded in a browser bundle.
See [qualification scope](../../docs/sdk-consumer-qualification.md).
