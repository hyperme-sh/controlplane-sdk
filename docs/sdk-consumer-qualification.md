# SDK consumer scope and qualification

The public root distribution remains `controlplane-sdk` 0.2.0, Apache-2.0.
Generated template names and versions remain unchanged. Placeholder repository
URLs and the Python template's `NoLicense` marker are corrected during generation;
every generated language tree includes the root license and a distribution notice.
The templates are not separately published packages or a new release line.

| Surface | Qualification | Distribution |
|---|---|---|
| Python REST and generation helpers | Source, wheel and rebuilt-sdist unit/contract checks; full module inventory and metadata verified | Root wheel |
| TypeScript REST | Full compilation, wallet wire contracts | Source tree and sdist |
| Kotlin REST | Full compilation, wallet wire and bearer-scheme contracts | Source tree and sdist |
| Swift REST | Full Linux package build with locked dependencies, wallet and server-error contracts | Source tree and sdist; no mobile application or Apple-platform qualification claimed |
| Python gRPC | Pinned real generation twice; byte comparison; flat and namespaced isolated import/serialization/RPC-path contracts | Source tree and sdist, outside root REST wheel |
| Python and TypeScript auth examples | RFC 7636 S256 vector, grant form encoding, API-key tenant headers and failure handling with mocked transports | Source tree and sdist; not complete login applications |
| Embedded C / nanopb | Protocol source only; target and bounds unselected | No generated C package |

## Protocol source and generator

The snapshot is byte-identical to `hyperme-sh/controlplane-proto` revision
`b91c1a7885c8fbffeab11651d39bce89f39a1da0`; path and SHA-256 are recorded in
`sdk/proto/provenance.json`. CI compares that immutable owner source before running
the generator. `tools/grpc/uv.lock` isolates grpcio-tools 1.80.0, grpcio 1.80.0 and
protobuf 6.33.6 from root REST dependencies. Generated versions and protocol field
numbers are unchanged. The generated flat imports and `spanopticon.v1` imports
are tested in separate Python processes because they define the same messages.

From the repository root, unit/contract qualification is:

```sh
uv sync --directory tools/grpc --frozen
tools/grpc/.venv/bin/python scripts/sdk-gen/check_grpc.py --verify-owner
```

This runs no server, wallet, payment or deployed-service scenario. The three RPC
contracts only echo listing, token-usage and user messages; they are not public
payment settlement APIs. REST wallet clients remain provider-neutral and internal
quota accounting remains separate from money.

To intentionally regenerate after reviewing an owner snapshot change, use the
`spanopticon_sdk_gen.grpc_codegen.generate_python_grpc` helper with the repository
root and its `sdk` output directory. It reads the standalone snapshot under
`sdk/proto`; no ancestor monorepo or private source fetch is needed. Review source,
provenance and generated changes together. The check itself writes only temporary
output and rejects byte or generated-file inventory drift.

## Auth application responsibilities

The examples do one request at a time. The caller owns trusted endpoint
configuration, callback state validation, secure token storage, device expiry,
poll intervals and `slow_down` backoff. A failed token response is an error, never
an authenticated session. Python exposes `httpx.HTTPStatusError`; TypeScript
rejects the promise. Interpret the OAuth error without logging tokens or secrets.
Client credentials belong only in a confidential server process, never a browser
bundle. The TypeScript file is shared example source, not permission to put its
server-only helper into a public client. SIWE and payout-address proof contracts
remain separate from these OAuth helpers.

Installed-owner exporter composition stays in scheduled CI. No deployed realm,
live provider, C target, mobile app, package publication or production activation
is claimed by these unit/contract checks.
