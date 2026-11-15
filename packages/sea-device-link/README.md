# SEA device link

Browser-only TypeScript core for deliberate transfer of an existing identity.
It preserves an opaque complete SociACL keyring and delegates authority and
atomic encrypted storage to trusted owner adapters. It does not create accounts,
issue sessions, grant permissions or make copied keys independently revocable.

This private, unpublishable `0.0.0` development package is separate from the SDK's
Python wheel and generated REST clients. No release or public publication is
performed. Its only runtime dependency is browser WebCrypto in a secure context.
React components belong to controlplane-portal #130.

## Use

```ts
import { Receiver, Sender, encodeRequest, decodeRequest } from 'sea-device-link';

// Trusted configuration, not values copied out of an untrusted request.
const scope = {
  sourceOrigin: 'https://source.example',
  destinationOrigin: 'https://destination.example',
  application: 'example', tenant: 'tenant-a', audience: 'test',
};
const receiver = await Receiver.create(scope);
const publicText = encodeRequest(receiver.request); // QR or camera-free text
// On the source device, after local unlock:
const sender = await Sender.create({
  request: decodeRequest(publicText), expectedScope: scope,
  identity, keyring: completeKeyringBytes, authority,
});
// Exchange sender.offer as bounded PUBLIC data. Its presence is not consent.
await receiver.bind(sender.offer);
// The UI must compare all eight groups on BOTH devices over an independent
// trusted channel (in person, or an authenticated channel the user already has).
// Never automatically pass a session's own comparison back to confirm().
sender.confirm(comparisonReadFromReceivingDevice);
receiver.confirm(comparisonReadFromSendingDevice);
await sender.send(transport);
await receiver.receive(transport, authority, destinationStorage);
await sender.finish(transport);
```

The example spans two isolated clients; shared variable names illustrate adapter
roles, not shared browser memory. Obtain consent before releasing private data.
The full comparison is intentionally long: a short human code needs a separate
protocol with commitments/attempt controls. The camera-free fallback is the same
full public request text, not a password or an offline encryption secret.

Call `cancel()` when abandoning a screen, navigating away or on the UI's expiry
timer. Expiry is checked on operations and after asynchronous work, not by an
internal timer. Cancellation aborts pending storage via its signal; adapters must
honor it at commit. A transaction already committed cannot be undone by cancel.

## Owner adapters

`IdentityAdapter.validateKeyring` must call supported SociACL keyring APIs to
check private/public key consistency and complete history. The bytes are the
canonical `encodeKeyring` output (v2/v3), **not JSON containing only a SEA pair**.
The adapter must preserve signing/encryption keys, retired encryption keys,
genesis binding, content/rotation epochs, lane history and contact-lane secrets.
`AccountKeyring.import`/current-key resolution must use authenticated complete
history. A plaintext buffer is a borrowed value: do not retain or persist it.

`IdentityAdapter.current` contacts the current-key owner, validates authenticated
state and returns a scoped checkpoint valid no later than session expiry. It
checks the offered identity's principal/current pub/current epub/sequence and
current revocation against trusted history. The transfer does not carry a trusted
freshness floor. Failure to reach authority must fail closed.

`StorageAdapter.commit` owns destination protection and atomicity. It prepares
local wrapping, locks the destination, calls `beforeCommit`, rechecks expiry and
the abort signal after asynchronous work, and atomically stores protected keyring,
binding, checkpoint and completion. Exact-transcript duplicates are idempotent;
different identities or newer local keys cannot be overwritten. Import and its
completion must never be separate transactions. This interface cannot make a
remote authority and local database one distributed transaction: the adapter must
honor the owner's checkpoint validity/fencing contract and report any unavailable
fence. A later owner rotation still applies to a previously imported key.

After an uncertain response, retry `receive` while the session is active. After
reload or expiry, call `reconcile(savedBinding, storage, transport)` to republish
only a previously durable completion. This neither imports keys nor revalidates
an application session. Sender `finish` authenticates the completion. No fresh
import is permitted after expiry. Persist only the public binding for recovery;
receiver ephemeral private keys never need to be persisted. If no import happened,
start a new pairing session after reload.

`Transport` carries ciphertext/public data only. Its implementations must provide
immutable session writes, bounded polling/size/rates, cancellation/expiry and
scope-aware capabilities. Never translate relay success into account authority.
Transport failures are retryable; send retries reuse identical ciphertext.

## Dependencies and boundaries

- Parent: https://github.com/hyperme-sh/spanopticon/issues/85
- Authority implementation: https://github.com/hyperme-sh/acl-service/issues/163
- Relay: https://github.com/hyperme-sh/auth-service/issues/60
- Supported browser keyring codec/import:
  https://github.com/FyberLabs/SociACL/issues/204
- Consumers: FyberLabs/s3r.ch #519 and controlplane-portal #131.

SociACL's current account-keyring implementation imports Node crypto and its
browser export map does not expose this codec. #204 is a production consumer
prerequisite. This library deliberately injects its public owner adapter rather
than copying a verifier or weakening checks. The synthetic contract adapter in
`test/support.mjs` is **not** a production implementation, a complete SociACL
validation test, or a storage protection implementation. No production default
adapter ships here.

## Validation

PR CI builds ESM/declarations, executes unit/contract tests and independent
interoperability vectors, and checks an isolated packed package's exports/types.
There are no browser/network/shared-resource tests in this suite. Product browser
scenarios belong to Infra #1559 in the nightly batch. No deployment is claimed.
See [PROTOCOL.md](PROTOCOL.md), `src/types.ts` and `vectors/v1.json` for the contract.
