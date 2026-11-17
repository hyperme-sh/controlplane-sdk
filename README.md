# Control plane SDK

Generated REST clients, protocol snapshots, and auth examples for the [Hypermesh](https://github.com/hyperme-sh) control plane. The Python distribution is [`controlplane-sdk`](pyproject.toml) **0.2.0**. It installs `openapi_client` (the generated REST client) and `spanopticon_sdk_gen` (export, generation, and structural diff helpers).

## Why

Hosts and renters reach Hypermesh through one HTTP control plane: identity, tenancy, and marketplace listings. That contract is an OpenAPI document merged from the edge and the services behind it. This repository keeps the generated clients and the snapshot they were built from, so an integrator can call a known document instead of discovering routes from a running server. OpenAPI does not describe Keycloak or the gateway API-key headers, so those calls live here as small hand-written examples.

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

Generated template names and versions (including `openapi_client` 1.0.0) remain recorded template metadata, not separate releases. Repository URLs and Apache-2.0 licensing are applied during generation. Use the root `controlplane-sdk` **0.2.0** Python build. See [consumer qualification and distribution scope](docs/sdk-consumer-qualification.md).

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
```

`GET /api/v1/health/` returns `HealthCheckResponseDto`. `GET /api/v1/marketplace/listings` takes optional `public_only`. These examples use retained public endpoints; provider-specific payment APIs are outside this SDK.

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

For tenant identity, native host enrollment and tunnel calls, lease events, and a separate settlement adapter, see [Build a compatible operator](docs/operator-protocol.md).

## How Hypermesh uses it

Hypermesh leases run through this control-plane HTTP API. The callers are host and renter clients, the control plane portal, and services that present a gateway-exchanged JWT.

- A host, or an operator acting for a host, creates and updates a marketplace listing with `MarketplaceApi` at `/api/v1/marketplace/listings`. The body is `ListingCreateBody`: `title`, `listing_type`, `price_type`, optional `price_amount`, `metadata`, and `is_public`. The call sends a tenant-session bearer token.
- A renter lists public listings with `public_only=true` and buys one with `POST /api/v1/marketplace/listings/{listing_id}/purchase`.
- `PaymentsApi` currently exposes public-key crypto budget operations under `/api/v1/budgets`. Budget allocation is not a wallet transfer, a confirmed payment, or an enterprise quota grant.
- `WalletPaymentsApi` exposes the registered provider-neutral sandbox owner contract under `/api/v1/payments/wallet`, plus purpose-specific payout-address proofs. Discover `wallet-payments/v1` capabilities first; production activation remains separate. Historical custody/test-credit endpoints are not generated.
- `WalletAuthApi` exposes Auth SIWE nonce, bind and current-binding operations. Wallet control does not authorize spending, another owner's payout destination, or settlement. Use the server-issued message unchanged; see [wallet clients](docs/wallet-clients.md).
- Gateway callers use the documented auth helpers and the credentials required by each supported endpoint. A gateway credential does not create a missing payment API or confer wallet spending authority.
- The same snapshot also carries tenant, user, ACL, and AI inference/usage calls that the control plane edge fronts for those same sessions.

`ContractEcho` (`spanopticon.v1`) is the protobuf snapshot of listing, token-usage, and user messages. Each RPC returns the request unchanged. Hosted payment operations are separate from this echo contract and are exposed only when the owning service and generated snapshot support them.

## Wallets, hosted payments and enterprise accounting

These are separate contracts:

- Public crypto clients and settlement adapters use wallet/public-key identifiers,
  explicit asset/network quantities and signed intents. Keep these interfaces
  usable without Stripe credentials or private hosted payment code. The
  [operator protocol](docs/operator-protocol.md#submit-a-signed-settlement-intent)
  describes the separate settlement adapter; an example adapter does not mean a
  hosted production payment rail is enabled.
- Hosted Stripe and future USDC payments own provider confirmation, refunds,
  fees, currency conversion and payouts. Existing wallet and sandbox components
  are building blocks; complete wallet-funded USDC delivery is unfinished.
  Retirement of an older custody implementation does not remove this planned
  capability or SIWE support.
- Enterprise accounting uses integer quota units such as tokens and time.
  Those units are not crypto assets, money balances or implicitly redeemable
  claims. A capacity release does not execute a payment refund.

The neutral accounting library has been extracted and has internal/none/HTTP
backends, but independent public consumption still needs source and dependency
preparation. This README does not promise that package is already publicly
installable. The service-container distribution policy and the public library
boundary are distinct. See [#47](https://github.com/hyperme-sh/controlplane-sdk/issues/47)
for consumer dependencies and completion criteria. Existing public crypto
budget and settlement interfaces are retained while those gaps are completed.

## Develop and test

From a checkout, with Python 3.13 and uv 0.11.26:

```sh
uv sync --frozen
bash scripts/check-package.sh
```

`uv sync` installs the dev group, including `controlplane-edge` pinned at `ae3ec5c91cec7755e3553ab5fb24d292e30c2543`. `scripts/check-package.sh` runs the pytest suite from the source tree, from a fresh wheel, and from a wheel rebuilt from the sdist, and compares those packaged-byte contracts. Generator stub tests under `sdk/rest/python/test` are outside that suite. Behavioral tests are in [`tests`](tests).

Regenerate the REST trees with the pinned OpenAPI Generator image, then rerun the package check. Commands and the structural path/schema diff are in [`scripts/sdk-gen/README.md`](scripts/sdk-gen/README.md). Auth files under `sdk/auth` stay as written; regeneration does not replace them.

`tests/test_edge_export_integration.py` runs only in the central scheduled
`sdk-consumers` nightly adapter, across source, wheel and rebuilt sdist. Ordinary
PR and main package checks exclude this case and retain the unit and contract
suite. The nightly adapter exercises offline OpenAPI export through the installed `controlplane-edge` package. The test process has no upstream base URLs, and an unexpected HTTP call fails the test. That covers offline export of the committed snapshot.

[`.github/workflows/package.yml`](.github/workflows/package.yml) validates main, while
[isolated consumer CI](.github/workflows/consumer-qualification.yml) validates pull
requests. Public jobs use `ubuntu-24.04`; private jobs use debrunners. Both keep
read-only `contents` permission. Package checks compare the executed test inventories
across source, wheel and rebuilt sdist and report the result in the job log.
Their temporary build archives and JUnit files are not uploaded as Actions artifacts
or wrapped in source-bundle containers.

## Release and versioning

The Python package in this checkout is `controlplane-sdk` **0.2.0** (`pyproject.toml`).
The OpenAPI document version is **1.0.0**, and `release-policy.json` declares release
line **0.2**. The package release publisher is retired; tag-time admission does not
publish. This library has no standalone runtime image or TEST channel. Consuming
services publish their own GHCR containers and follow moving TEST channels.
Historical tags and releases remain unchanged. See [Releasing](docs/releasing.md).

## License

The repository and the `controlplane-sdk` distribution are [Apache License 2.0](LICENSE). Dependencies keep their own licenses.

Nullable Python update fields distinguish omission from an explicit `None`.
For example, `ListingUpdateBody()` omits `description`, while
`ListingUpdateBody(description=None)` sends `"description": null`. This also
applies to `from_dict`, `from_json`, and assignment after construction. The
generator installs the same schema-derived handling for every nullable update
model, including branding, users, roles, SSO settings and tenants.

Multipart logo and profile-picture uploads accept a file path string, raw bytes,
or a `(filename, bytes)` tuple. Paths are read as binary files; named uploads
infer the part's media type from the filename, and raw bytes use
`application/octet-stream`. The generator normalizes multipart binary schemas
without altering the published OpenAPI snapshot.

## Browser identity transfer

[packages/sea-device-link](packages/sea-device-link/README.md) is a separate,
private browser ESM/TypeScript package for encrypted existing-identity transfer.
It defines explicit transport, authority and destination-storage adapters and
ships unit/contract vectors. It is not included in the Python wheel or generated
REST clients. Production adapter dependencies and protocol boundaries are listed
in the package README.
