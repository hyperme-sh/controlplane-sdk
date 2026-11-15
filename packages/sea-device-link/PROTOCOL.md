# Protocol v1

## Trust and authentication

The rendezvous and every network message are untrusted. The application obtains
scope/origin policy from trusted configuration. Both users compare the entire
256-bit transcript digest via a trusted independent channel before confirming.
A QR scan by itself does not authenticate the sender: an attacker can replace
public pairing data. Never fetch the peer comparison through the relay or
implicitly confirm a local digest. A compromised client/UI or owner adapter is
outside this protocol's protection. Full-digest comparison is the authentication
bootstrap; there is no claim that unauthenticated ECDH alone defeats interception.

An attacker may substitute either ephemeral key or identity metadata, reorder or
replay messages, inject malformed/large ciphertext, suppress completion, or race
expiry/rotation. Transcript comparison, transcript-bound authenticated encryption,
owner validation, expiry and atomic destination storage address these cases.
Denial of service remains possible. No raw keys or recovery secrets belong in
URLs, public graphs, telemetry, logs, clipboard helpers or captured UI traces.

## Wire shapes and canonical bytes

`src/types.ts` defines public request, offer, envelope and completion shapes.
Unknown fields, unsupported versions, noncanonical base64url, unsafe integer
values, excessive lifetimes and non-HTTPS origins are refused. Origin strings
must equal their URL origin, without slash/path/credentials. Public points are
P-256 SEA `base64url(x).base64url(y)`; each coordinate is exactly 32 bytes. Native
WebCrypto validates ECDH points; the keyring adapter validates account keys.

Request: v=1, random 32-byte session nonce, receiver ephemeral ECDH public key,
absolute millisecond expiry, and scope. Lifetime is at most 300000 ms (default
120000). Request text is `sea-link-v1:` followed by unpadded base64url UTF-8 JSON
in the field order produced by `encodeRequest`. Camera and camera-free inputs use
that same bounded public encoding. Decode does not establish authority or expiry;
session operations check both against trusted configuration/clock.

Offer adds sender ephemeral ECDH public key, identity metadata and SHA-256 of the
complete opaque keyring payload. The canonical transcript is UTF-8 JSON of this
array, with no whitespace, exactly in this order:

```
["sea-device-link/v1", session, receiverKey, expiresAt,
 sourceOrigin, destinationOrigin, application, tenant, audience,
 senderKey, principal, pub, epub, rotationSeq, payloadHash]
```

The transcript id is unpadded base64url SHA-256 of those bytes. The comparison is
that digest in lowercase hex, eight groups of eight digits separated by `-`.
The payload hash is public: complete keyring bytes contain high-entropy private
keys, not low-entropy user input. Metadata (including principal and scope) is
visible to the relay; this protocol does not promise identity unlinkability.

ECDH P-256 produces a 32-byte shared secret. HKDF-SHA-256 salt is the raw transcript
digest. Separate info strings `sea-device-link/v1/payload` and
`sea-device-link/v1/completion` derive 256-bit AES-GCM and HMAC-SHA-256 keys.
Encryption uses a random 12-byte IV, 128-bit tag, and the canonical transcript as
additional authenticated data. Ciphertext includes the GCM tag. A key is used for
one immutable envelope; retries never re-encrypt or alter the offer. Max keyring
size is 524288 bytes; envelope decode is bounded before WebCrypto.

After atomic destination commit, the completion MAC is HMAC-SHA-256 over UTF-8
`sea-device-link/v1/committed\n` followed by the base64url transcript id. It is
stored in the same transaction as the protected keyring, then sent. It proves
possession of the agreed channel key; only a correct trusted receiver/storage
adapter makes it a statement about durable import. A relay cannot forge it.

## State transitions

Receiver: created -> bound -> confirmed -> committed.
Sender: bound -> confirmed -> sent -> committed.
Cancellation is terminal. Import expiry is terminal on the receiver and on a
sender that has not attempted upload. An attempted upload enters `sent` before
the transport call; an uncertain response can therefore recover completion.
After expiry, `send` refuses further uploads but preserves the authentication key,
and `finish` can stay pending until completion arrives or the user cancels.
Conflicting concurrent operations refuse
with `state`. Repeated sends are immutable retries. Failed receives retry from
confirmed and first query durable storage. No duplicate import after committed.
A lost completion is recovered from stored public binding/completion after reload,
without retaining ephemeral private keys. Sender accepts a valid delayed
completion even after the import deadline; fresh imports always check expiry.

Validation occurs before source preparation and after destination decryption.
Current-key authority is checked before send, before storage, and again through
the storage precommit callback; a changed checkpoint refuses commit. Decision
expiry may not exceed session expiry. The trusted store must honor the callback,
abort signal and owner fencing contract at its atomic boundary. This does not
freeze future rotations or create a distributed transaction with the authority.

Native crypto failures become `crypto`; adapters expose only `identity`,
`authority`, `storage` or `transport`, never their underlying messages. Other
stable codes: `invalid`, `scope`, `expired`, `state`, `comparison`, `pending`.
Abort pending operations by cancelling the session. After a failed/uncertain
commit, reconcile durable storage rather than generating a replacement identity.

Transient byte arrays owned by the library are overwritten on terminal paths;
nonextractable key handles are released. JavaScript strings, WebCrypto internals,
caller-owned buffers and garbage-collector copies cannot be guaranteed zeroized.
Owners must clear their own unlocked keyring buffers and abandon idle sessions.

`vectors/v1.json` contains independently generated synthetic P-256/HKDF/GCM/HMAC
values and canonical encodings. Its fixed private scalar is test-only.
