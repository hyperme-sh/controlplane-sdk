# Build a compatible operator

A fork supplies an identity issuer, admits hosts into its own organizations, and ships its settlement adapter as a separate process. The Cedar example runs this flow with a one-use enrollment token, a CPU job and a local TEST ledger. From a Spanopticon checkout, run the following command with a fresh receipt path. [Cedar source and prerequisites](https://github.com/hyperme-sh/spanopticon/tree/034b45c4458c6c25db33bcb8500ceecf2c6e8534/examples/operator)

```sh
python3 -m examples.operator.check_sample --receipt /tmp/cedar-receipt.json
```

## Bind the caller to the tenant

Validate the session signature, issuer, audience and expiry before accepting its subject. Match the requested tenant to the signed tenant and check the subject's organization membership for the requested operation. Cedar requires host-management permission to register a host and self-use permission in that host's organization to reserve it. A tenant header alone supplies no authority.

On the native Plane, human lease requests use the tenant session obtained after login and tenant selection. A service integration exchanges its scoped API key at the gateway. Host operations use the enrolled device credential. Keep each credential at its intended endpoint. [Control plane credentials](../README.md#practical-use)

## Enroll a native host and apply its tunnel

All paths in this table start with `/api/v1/hypermesh/agent`. Send the tenant in `X-Tenant-ID`. After enrollment, authenticate agent calls with `Authorization: Bearer <device_secret>`.

| Call | Host behavior |
|---|---|
| `POST /enroll` | Submit the one-use enrollment token. Supply the host name and its WireGuard public key together when binding the peer at enrollment. Persist the returned device credential. |
| `POST /heartbeat` | Report device liveness using the enrolled credential. |
| `GET /tunnel` | Read the assigned tunnel. HTTP 204 means no assignment. HTTP 409 for a missing peer key means the host needs to register its public key. |
| `POST /tunnel/peer` | Send `peer_public_key`. The private key stays on the host. Changing an enrolled key requires retiring and registering the host again. |
| `POST /tunnel/ack` | After applying the configuration locally, send `{"applied":true}`. |
| `GET /jobs` and `POST /jobs/{id}/result` | Pull assigned work and report its result with the device credential. |

One WireGuard peer belongs to the enrollment. Renters reach the workload through the gateway using lease credentials. The native agent's API and the Cedar reference API have distinct request models. In particular, Cedar prepares its device credential locally before enrollment so the same host can recover after a lost acknowledgment. Use the deployed Plane's OpenAPI for native request bodies.

## Consume a lease event

On `controlplane.events.v1`, read the envelope's `schema_version`, `event_type`, `service`, `tenant_id`, `occurred_at` and `payload`. An optional `correlation_id` connects related operations. Authenticate the producer, select the registered schema by event type and version, validate the payload, and check its tenant against the envelope before applying policy. [Public schema registry](https://github.com/hyperme-sh/controlplane-events/blob/main/src/controlplane_events/schemas/registry.json)

For a completed self-use job, consume `hypermesh.lease.ended.v1`. Its payload can carry `billing_record_id: null` and `gross_cents: 0`. For a billed execution outcome, `hypermesh.lease.outcome.v1` carries the billing record, host identity, execution outcome, certification and delivered cents. Delivered cents describe the lease. The fork chooses whether an event authorizes a policy decision and separately obtains signing authority for the wallet. [Lease-ended schema](https://github.com/hyperme-sh/controlplane-events/blob/main/src/controlplane_events/schemas/hypermesh.lease.ended.v1.json) · [Billed outcome schema](https://github.com/hyperme-sh/controlplane-events/blob/main/src/controlplane_events/schemas/hypermesh.lease.outcome.v1.json)

## Submit a signed settlement intent

Implement `SettlementPort.settle` in the adapter. The public HTTP example accepts `POST /settlements` with `wallet`, `amount`, `asset`, `network`, `idempotency_key`, `signer` and `signature_hex`. Express the positive integer amount in atomic units of the named asset and network. Use `SettlementIntent.signing_bytes()` for the domain-separated canonical bytes. The adapter verifies both the signature and the signer's authority for that wallet. [Reference contract and signing bytes](https://github.com/hyperme-sh/spanopticon/blob/034b45c4458c6c25db33bcb8500ceecf2c6e8534/examples/settlement/contract.py)

Persist the signer and idempotency key with the canonical intent. After a lost reply, retry the same operation with identical bytes. Reject a changed intent for that key. The response carries a status of `accepted`, `refused` or `pending` and an opaque `processor_reference`. Reconcile pending or ambiguous external operations with the processor before retrying an effect. In Cedar, one accepted TEST unit records a local grant for the completed job. The self-use lease retains zero gross cents. [Adapter and replay example](https://github.com/hyperme-sh/spanopticon/tree/034b45c4458c6c25db33bcb8500ceecf2c6e8534/examples/settlement)
