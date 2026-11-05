# Control plane SDK

Generated REST clients, protocol snapshots, and auth examples for the [Hypermesh](https://github.com/hyperme-sh) control plane. The Python distribution is [`controlplane-sdk`](pyproject.toml) **0.2.0**. It installs `openapi_client` (the generated REST client) and `spanopticon_sdk_gen` (export, generation, and structural diff helpers).

## Why

Hosts and renters reach Hypermesh through one HTTP control plane: identity, tenancy, marketplace listings, and the USDC lease payment. That contract is an OpenAPI document merged from the edge and the services behind it. This repository keeps the generated clients and the snapshot they were built from, so an integrator can call a known document instead of discovering routes from a running server. OpenAPI does not describe Keycloak or the gateway API-key headers, so those calls live here as small hand-written examples.

## How it works

The snapshot is [`sdk/openapi/v1/openapi.json`](sdk/openapi/v1/openapi.json). Its title is `spanopticon Control Plane API`, document version `1.0.0`. The document's `x-sdk-meta.sources` list is `controlplane-edge`, `auth`, `user`, `payment`, `acl`, `marketplace`, `ai`, and `api_keys`. Bearer schemes in the document are `HTTPBearer`, `BearerAuth`, and `BearerKeycloak` (Keycloak access token, realm name `controlplane` in the scheme description).

[OpenAPI Generator](https://openapi-generator.tech) **7.10.0** produces four REST trees from that snapshot:

| Language | Path | In the `controlplane-sdk` wheel |
| --- | --- | --- |
| Python | [`sdk/rest/python`](sdk/rest/python) | Yes (`openapi_client`) |
| TypeScript | [`sdk/rest/typescript-fetch`](sdk/rest/typescript-fetch) | No |
| Kotlin | [`sdk/rest/kotlin`](sdk/rest/kotlin) | No |
| Swift | [`sdk/rest/swift5`](sdk/rest/swift5) | No |

`AIApi` is the inference and session client (`/api/v1/ai/ask`, `/api/v1/ai/inference`, `/api/v1/ai/complete`, sessions). `AIUsageApi` is usage history and summary (`/api/v1/ai/usage/history`, `/api/v1/ai/usage/summary`). `AiApi` is a compatibility alias of `AIUsageApi`. Details are in [AI client names](docs/ai-usage-adoption.md).

The protobuf snapshot is [`sdk/proto/spanopticon/v1/contractecho.proto`](sdk/proto/spanopticon/v1/contractecho.proto), package `spanopticon.v1`. `ContractEcho` echoes `ListingWire`, `TokenUsageWire`, and `UserWire`. Python stubs sit next to the proto and under [`sdk/grpc/python`](sdk/grpc/python). Embedded C notes are in [`sdk/grpc/c-nanopb-README.md`](sdk/grpc/c-nanopb-README.md).

Auth examples are hand-written under [`sdk/auth`](sdk/auth): PKCE, the device authorization grant, client credentials, and gateway headers `X-Api-Key` plus `X-Tenant-ID`. The `controlplane-sdk` wheel contains `openapi_client` and `spanopticon_sdk_gen`. The other language trees, the protobuf stubs, and the auth examples stay in the source tree.

Install `controlplane-sdk` in an environment where `openapi_client` comes from this distribution. Another distribution that publishes the same top-level package name occupies the same import.

Generated language trees still carry upstream placeholder metadata (including `GIT_USER_ID` install lines and a placeholder `openapi_client` version of `1.0.0`). Use the root `controlplane-sdk` **0.2.0** build.

## Practical use

Python **3.13**. The package requires `>=3.13`. CI installs [uv](https://docs.astral.sh/uv/) **0.11.26**.

Install the client into a project:

```sh
uv venv --python 3.13
uv pip install "controlplane-sdk @ git+https://github.com/hyperme-sh/controlplane-sdk.git"
```

`pip install` with the same URL works. The checkout you build from is package version **0.2.0**.

Point the client at a control plane origin and a bearer token. The client default host is `http://localhost` when `host` is omitted.

```python
import os

from openapi_client import (
    ApiClient,
    Configuration,
    HealthApi,
    MarketplaceApi,
    PaymentsApi,
    UsdcLeasePaymentCreate,
)

configuration = Configuration(
    host=os.environ["CONTROL_PLANE_URL"],
    access_token=os.environ["CONTROL_PLANE_TOKEN"],
)

with ApiClient(configuration) as api:
    health = HealthApi(api).health_check_api_v1_health_get()
    listings = MarketplaceApi(api).list_listings_api_v1_marketplace_listings_get(
        public_only=True
    )
    payment = PaymentsApi(api).create_usdc_lease_payment_route_api_v1_payments_usdc_lease_payments_post(
        UsdcLeasePaymentCreate(amount_cents=2500, listing_id="lst_example")
    )
```

`GET /api/v1/health/` returns `HealthCheckResponseDto`. `GET /api/v1/marketplace/listings` takes optional `public_only`. `POST /api/v1/payments/usdc/lease-payments` takes `amount_cents` (integer USD cents, at most `99999999`) and an optional `listing_id`. The server converts cents 1:1 into USDC atoms (6 decimals).

Token and API-key helpers are the files in [`sdk/auth`](sdk/auth/README.md). From a checkout of this repo:

```python
import asyncio
import base64
import hashlib
import os
import sys

sys.path.insert(0, "sdk/auth/python")
from keycloak_auth import (
    api_key_headers,
    build_authorize_url,
    client_credentials_token,
    fetch_well_known,
    pkce_verifier,
)


async def main() -> None:
    document = await fetch_well_known(os.environ["KEYCLOAK_URL"], "controlplane")
    machine = await client_credentials_token(
        token_endpoint=document["token_endpoint"],
        client_id=os.environ["KEYCLOAK_CLIENT_ID"],
        client_secret=os.environ["KEYCLOAK_CLIENT_SECRET"],
    )
    verifier = pkce_verifier()
    challenge = base64.urlsafe_b64encode(
        hashlib.sha256(verifier.encode("ascii")).digest()
    ).decode("ascii").rstrip("=")
    authorize_url = build_authorize_url(
        authorization_endpoint=document["authorization_endpoint"],
        client_id=os.environ["KEYCLOAK_CLIENT_ID"],
        redirect_uri=os.environ["OIDC_REDIRECT_URI"],
        state=os.environ["OIDC_STATE"],
        code_challenge=challenge,
    )
    gateway_headers = api_key_headers(
        api_key=os.environ["API_KEY"],
        tenant_id=os.environ["TENANT_ID"],
    )
    print(machine["access_token"])
    print(authorize_url)
    print(gateway_headers)


asyncio.run(main())
```

`KEYCLOAK_URL` is the Keycloak origin, with no `/realms/...` suffix. The Python helper returns the PKCE verifier; the caller supplies the S256 `code_challenge`. The TypeScript copy of the same flow, including `pkceChallengeS256`, is [`sdk/auth/typescript/keycloakAuth.ts`](sdk/auth/typescript/keycloakAuth.ts). `api_key_headers` returns `X-Api-Key` and `X-Tenant-ID` for the gateway. Generated REST methods send the bearer token from `Configuration.access_token`.

Set `CONTROL_PLANE_TOKEN` to a tenant-session access token, or to the JWT the gateway minted from a service key or a renter key. A Keycloak token that has no `tenant_id` is rejected on the lease-payment route.

## How Hypermesh uses it

Hypermesh leases run through this control-plane HTTP API. The callers are host and renter clients, the control plane portal, and services that present a gateway-exchanged JWT.

- A host, or an operator acting for a host, creates and updates a marketplace listing with `MarketplaceApi` at `/api/v1/marketplace/listings`. The body is `ListingCreateBody`: `title`, `listing_type`, `price_type`, optional `price_amount`, `metadata`, and `is_public`. The call sends a tenant-session bearer token.
- A renter lists public listings with `public_only=true` and buys one with `POST /api/v1/marketplace/listings/{listing_id}/purchase`.
- The renter, or a worker that holds a renter key, opens the lease payment with `PaymentsApi` at `POST /api/v1/payments/usdc/lease-payments`. The route accepts a tenant-session JWT after switch-tenant, or a gateway exchange JWT from a `purpose=service` key or a renter key minted by the org-admin API. No card is charged. The renter pays the amount in USDC on Base. Where the deployment is Base Sepolia with Stripe test mode and `PAYMENTS_USDC_TEST_CREDIT_ENABLED`, `POST /api/v1/payments/usdc/lease-payments/{billing_record_id}/test-credit` settles that pending payment from test-network credit.
- Gateway callers that still hold an API key send `X-Api-Key` and `X-Tenant-ID` from the auth helpers. The lease-payment route itself is bearer-token traffic after that exchange.
- The same snapshot also carries tenant, user, ACL, and AI inference/usage calls that the control plane edge fronts for those same sessions.

`ContractEcho` (`spanopticon.v1`) is the protobuf snapshot of listing, token-usage, and user messages. Each RPC returns the request unchanged. Lease payment traffic stays on the REST client above.

## Develop and test

From a checkout, with Python 3.13 and uv 0.11.26:

```sh
uv sync --frozen
bash scripts/check-package.sh
```

`uv sync` installs the dev group, including `controlplane-edge` pinned at `ae3ec5c91cec7755e3553ab5fb24d292e30c2543`. `scripts/check-package.sh` runs the pytest suite from the source tree, from a fresh wheel, and from a wheel rebuilt from the sdist, and compares those packaged-byte contracts. Generator stub tests under `sdk/rest/python/test` are outside that suite. Behavioral tests are in [`tests`](tests).

Regenerate the REST trees with the pinned OpenAPI Generator image, then rerun the package check. Commands and the structural path/schema diff are in [`scripts/sdk-gen/README.md`](scripts/sdk-gen/README.md). Auth files under `sdk/auth` stay as written; regeneration does not replace them.

`tests/test_edge_export_integration.py` runs offline OpenAPI export through the installed `controlplane-edge` package. The test process has no upstream base URLs, and an unexpected HTTP call fails the test. That covers offline export of the committed snapshot.

[`.github/workflows/package.yml`](.github/workflows/package.yml) runs on pushes to `main` and on manual dispatch, on `ubuntu-24.04`, with read-only `contents` permission. It uploads the tested distribution as the `tested-dist` artifact and the JUnit files as `test-results` (90-day retention).

## Release and versioning

The Python package in this checkout is `controlplane-sdk` **0.2.0** (`pyproject.toml`). The OpenAPI document version is **1.0.0**. `release-policy.json` and the tag publisher declare release line **0.2**. Main package CI stores the tested wheel as an Actions artifact. Stable tags, `test-<commit>` snapshots, and the recorded `v0.24.0` GitHub release are described in [Releasing](docs/releasing.md).

## License

The repository and the `controlplane-sdk` distribution are [Apache License 2.0](LICENSE). Dependencies keep their own licenses.
