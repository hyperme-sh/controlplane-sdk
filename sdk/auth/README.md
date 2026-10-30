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

Regenerate REST clients separately (`make sdk-gen`); these files are maintained by hand.
