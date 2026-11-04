# (s)panopticon naming migration

Audit scope: all 28 repositories in hyperme-sh. Product prose uses `(s)panopticon`;
owned package, namespace, claim, environment-variable and path identifiers use
`spanopticon`. Twenty-six repositories have source/tooling/documentation changes.
The organization profile already used Hypermesh naming; verification only contains
an existing external documentation link. Twenty-two repository descriptions were
updated directly.

## Contract changes

- `spanopticon-models` 0.2.0 exports `spanopticon_models`; consumers and exact pins move together.
- `controlplane-proto` 0.2.0 uses `spanopticon.v1`. Generated Python, type stubs and gRPC paths were regenerated from the renamed protocol source. Message field numbers remain unchanged; RPC method names change.
- `controlplane-identity` 0.15.0 emits and requires `spanopticon_auth`, uses the `https://spanopticon.internal/` issuer namespace and the `https://spanopticon.dev/tenant_id` claim URI, and exports `SPANOPTICON_AUTH`.
- API configuration, service auth readers, reserved smoke claims, consumer tests and compatibility re-exports use the new identity contract.
- Operator/test configuration and image telemetry use the `SPANOPTICON_` environment prefix. Keycloak tooling uses the `spanopticon-test-*` secret names and `spanopticon-connect-browser-v1` flow; the native redirect scheme is `com.fyberlabs.spanopticon`.
- API titles, email subjects, wallet-binding prose, comments, package resources and owned integration-source identifiers use the new naming.

## Rollout

These PRs do not deploy services, reconcile Keycloak or copy/rotate secrets.
Merge in the order below. Retain reviewed dependency commits; if a merge squashes
or rebases them, refresh downstream immutable pins, assertions and locks and rerun
package checks before deploying. A Git branch name is never a dependency pin.

Prepare the deployment configuration and the newly named secrets through the
existing owner-controlled secret pipeline without printing their values. Update
operator settings, native clients and the matching Keycloak redirect/Connect flow
as one change. Provision configured application endpoints before relying on them;
JWT issuer and claim URIs are identifiers, not a request to create public DNS.
The external smoke OIDC caller keeps its existing repository identity.

Cut over all identity issuers and consumers together and require reauthentication
or API-key token re-exchange. This is not a rolling mixed-namespace protocol:
old internal session issuers are not translated or silently accepted. The edge
retains the legacy tenant-claim URI for tokens accepted by its existing bearer
validator (including Keycloak); all supplied tenant aliases must be valid and
agree. Forwarded tenant headers are reconstructed from policy state, and a
validated JWT without a tenant cannot forward a caller-supplied tenant header. Move gRPC
clients and servers together. Rollback must restore the whole reviewed dependency
and configuration set, not one consumer package.

The retained owner integration sources still require their external owner test
harness. Standalone package checks do not establish a deployed container, Keycloak
realm, native-client redirect, live provider or complete monorepo integration.

## Audit and validation

All 26 changed executable repositories passed their prescribed package/tooling
checks, including source/fresh-wheel/rebuilt-source checks where supplied. The SDK now includes the merged client implementation and generation helpers;
version 0.2.0 exports `spanopticon_sdk_gen`. Its 16 tests passed from source,
a fresh wheel and a rebuilt source distribution. Its protocol source and flat
generated bindings match the protocol package byte-for-byte; the namespaced
gRPC import and wire-roundtrip check passed. The explicit models gRPC-extra tests
also passed. A digest-pinned, disposable PostgreSQL 17 instance was used for the
database/tenancy/operator-ban checks. Tracked Python source was syntax-checked across the coordinated repositories.

Run the organization audit against sibling checkouts of these PR heads:

```sh
python3 controlplane-sdk/scripts/audit-naming.py /path/to/hyperme-sh-checkouts
```

`naming-exceptions.json` records 48 distinct reviewed source-line fingerprints.
They are existing external repository/OIDC/document targets, external owner test
harness references, signed historical interoperability evidence, the frozen migration registry, and the edge tenant-claim compatibility constant. Renaming them
without migrating their owners or regenerating the evidence would break links,
authority checks, imports or signature verification. The audit rejects new legacy
references, legacy owned paths, missing repositories and stale exceptions.

## Pull requests in dependency order

| Repository | PR | Local validation |
| --- | --- | --- |
| controlplane-billing | [#3](https://github.com/hyperme-sh/controlplane-billing/pull/3) | Passed |
| controlplane-db | [#3](https://github.com/hyperme-sh/controlplane-db/pull/3) | Passed |
| controlplane-events | [#2](https://github.com/hyperme-sh/controlplane-events/pull/2) | Passed |
| controlplane-identity | [#3](https://github.com/hyperme-sh/controlplane-identity/pull/3) | Passed |
| controlplane-keycloak | [#2](https://github.com/hyperme-sh/controlplane-keycloak/pull/2) | Passed |
| controlplane-proto | [#2](https://github.com/hyperme-sh/controlplane-proto/pull/2) | Passed |
| controlplane-sdk | [#10](https://github.com/hyperme-sh/controlplane-sdk/pull/10) | Passed |
| hypermesh-orchestrator | [#2](https://github.com/hyperme-sh/hypermesh-orchestrator/pull/2) | Passed |
| turn | [#3](https://github.com/hyperme-sh/turn/pull/3) | Passed |
| controlplane-api | [#5](https://github.com/hyperme-sh/controlplane-api/pull/5) | Passed |
| controlplane-models | [#2](https://github.com/hyperme-sh/controlplane-models/pull/2) | Passed |
| controlplane-tenancy | [#4](https://github.com/hyperme-sh/controlplane-tenancy/pull/4) | Passed |
| hypermesh-ticket | [#6](https://github.com/hyperme-sh/hypermesh-ticket/pull/6) | Passed |
| user-service | [#10](https://github.com/hyperme-sh/user-service/pull/10) | Passed |
| controlplane-core | [#5](https://github.com/hyperme-sh/controlplane-core/pull/5) | Passed |
| aiuditor | [#15](https://github.com/hyperme-sh/aiuditor/pull/15) | Passed |
| auth-service | [#5](https://github.com/hyperme-sh/auth-service/pull/5) | Passed |
| controlplane-edge | [#8](https://github.com/hyperme-sh/controlplane-edge/pull/8) | Passed |
| hypermesh-gateway | [#11](https://github.com/hyperme-sh/hypermesh-gateway/pull/11) | Passed |
| oracles | [#6](https://github.com/hyperme-sh/oracles/pull/6) | Passed |
| payments-access | [#5](https://github.com/hyperme-sh/payments-access/pull/5) | Passed |
| product-template | [#5](https://github.com/hyperme-sh/product-template/pull/5) | Passed |
| acl-service | [#10](https://github.com/hyperme-sh/acl-service/pull/10) | Passed |
| ai-service | [#4](https://github.com/hyperme-sh/ai-service/pull/4) | Passed |
| api-keys-service | [#6](https://github.com/hyperme-sh/api-keys-service/pull/6) | Passed |
| marketplace-service | [#4](https://github.com/hyperme-sh/marketplace-service/pull/4) | Passed |

Coordination: https://github.com/hyperme-sh/controlplane-sdk/issues/9

## Review follow-up

The frozen database migration registry was restored byte-for-byte to its base
version. Its two historical naming lines are explicit audit exceptions. All
affected consumers were repinned and their package checks rerun. The SDK PR
incorporates the newly merged client implementation and resolves its README
conflict while retaining the implementation and applying the canonical rename.

## Additional extracted repositories

The audit now covers payment-service, controlplane-portal, and controlplane-tests
as well, bringing coverage to 31 repositories. Portal schema imports, SDK aliases,
branding, and browser storage use the canonical name. Old browser credentials
are deleted rather than migrated; tenant selection must be re-established.
The test helper is spanopticon-tests 0.2.0 with spanopticon_tests imports and
SPANOPTICON_TEST_ALEMBIC_INI configuration. Update its consumers together.
The retained owner integration suites remain separately unqualified.

The payment-service import landed during final review. Its package imports and
private pins now use the canonical models and test-helper packages, while the
actual external smoke caller repository remains unchanged.
