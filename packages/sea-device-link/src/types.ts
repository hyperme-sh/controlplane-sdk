/** All adapters are trusted local code; remote JSON is never an adapter. */
export interface Scope {
  sourceOrigin: string;
  destinationOrigin: string;
  application: string;
  tenant: string;
  audience: string;
}
export interface Identity {
  principal: string;
  pub: string;
  epub: string;
  rotationSeq: number;
}
export interface Request {
  v: 1;
  session: string;
  receiverKey: string;
  expiresAt: number;
  scope: Scope;
}
export interface Offer {
  request: Request;
  senderKey: string;
  identity: Identity;
  payloadHash: string;
}
export interface Envelope {
  transcript: string;
  iv: string;
  ciphertext: string;
}
export interface Completion {
  transcript: string;
  mac: string;
}
export interface Binding {
  session: string;
  transcript: string;
  expiresAt: number;
  scope: Scope;
  identity: Identity;
}
export interface Checkpoint {
  /** Authenticated opaque owner checkpoint. Never derived from the transfer. */
  revision: string;
  validUntil: number;
}
export interface IdentityAdapter {
  /** Use SociACL encodeKeyring/AccountKeyring.import, never a four-field pair.
   * Check key consistency and COMPLETE history; throw on any refusal.
   * This adapter must not persist or retain the supplied plaintext buffer. */
  validateKeyring(bytes: Uint8Array, identity: Identity): Promise<void>;
  /** Fetch current authenticated owner state; check current pub/epub, principal,
   * revocation, history completeness, scope and rotation sequence. No cached or
   * sender-provided freshness floor is sufficient. Never receive private keys. */
  current(binding: Binding): Promise<Checkpoint>;
}
export interface CommitInput {
  binding: Binding;
  keyring: Uint8Array;
  completion: Completion;
  signal: AbortSignal;
  /** Call after acquiring the destination write lock, immediately before the
   * atomic import. Recheck signal/expiry after all asynchronous protection work.
   * Store the returned checkpoint alongside the wrapped keyring and completion.
   * Do not commit after this callback rejects. */
  beforeCommit(): Promise<Checkpoint>;
}
export interface StorageAdapter {
  /** Atomically wrap/store the FULL keyring, binding, checkpoint and completion.
   * CAS the destination identity: refuse conflicting identities; idempotence is
   * exact transcript only. No plaintext persistence. A duplicate transcript must
   * match stored bytes/identity; never replace newer keys. One transaction owns
   * the import and completion so lookup can reconcile an uncertain response. */
  commit(input: CommitInput): Promise<void>;
  /** Only return a matching durable commit; no key material. */
  lookup(binding: Binding): Promise<Completion | null>;
}
export interface Transport {
  /** Immutable compare-and-set by session; repeated exact bytes are allowed. */
  send(session: string, envelope: Envelope): Promise<void>;
  receive(session: string): Promise<Envelope | null>;
  complete(session: string, completion: Completion): Promise<void>;
  completed(session: string): Promise<Completion | null>;
}
export interface Options {
  /** Trusted clock, milliseconds since epoch. Defaults to Date.now. */
  now?: () => number;
}
export type ErrorCode = 'invalid' | 'scope' | 'expired' | 'state' | 'comparison'
  | 'crypto' | 'identity' | 'authority' | 'storage' | 'transport' | 'pending';
export class LinkError extends Error {
  constructor(public readonly code: ErrorCode) { super(code); this.name = 'LinkError'; }
}
