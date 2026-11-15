export * from './types.js';
export { encodeRequest, decodeRequest, MAX_KEYRING_BYTES, MAX_SESSION_MS } from './wire.js';
import { LinkError, type Binding, type Checkpoint, type Completion, type Envelope, type Identity, type IdentityAdapter, type Offer, type Options, type Request, type Scope, type StorageAdapter, type Transport } from './types.js';
import { alive, b64, binding, canonical, comparison, fail, hash, identity, integer, MAX_KEYRING_BYTES, offer, record, request, sameScope, scope, text, unb64 } from './wire.js';
import { checkCompletion, completion, ephemeral, keys, open, seal } from './crypto.js';

type SessionKeys = Awaited<ReturnType<typeof keys>>;
export type State = 'created' | 'bound' | 'confirmed' | 'sent' | 'committed' | 'cancelled' | 'expired';
async function adapter<T>(code: 'identity' | 'authority' | 'storage' | 'transport', run: () => Promise<T>): Promise<T> {
  try { return await run(); } catch { return fail(code); }
}
function done(value: unknown): Completion {
  const d = record(value, ['transcript', 'mac']);
  unb64(d.transcript, 32); unb64(d.mac, 32);
  return { transcript: d.transcript as string, mac: d.mac as string };
}
function envelope(value: unknown): Envelope {
  const e = record(value, ['transcript', 'iv', 'ciphertext']);
  unb64(e.transcript, 32); unb64(e.iv, 12); unb64(e.ciphertext, 17, MAX_KEYRING_BYTES + 16);
  return { transcript: e.transcript as string, iv: e.iv as string, ciphertext: e.ciphertext as string };
}
abstract class Session {
  protected stateValue: State = 'created';
  protected busy = false;
  protected readonly abort = new AbortController();
  protected readonly now: () => number;
  readonly #plaintext = new Set<Uint8Array<ArrayBuffer>>();
  protected track(bytes: Uint8Array<ArrayBuffer>): Uint8Array<ArrayBuffer> { this.#plaintext.add(bytes); return bytes; }
  protected release(bytes: Uint8Array<ArrayBuffer>): void { bytes.fill(0); this.#plaintext.delete(bytes); }
  protected wipe(): void { for (const bytes of this.#plaintext) bytes.fill(0); this.#plaintext.clear(); }
  protected constructor(options: Options) { this.now = options.now ?? Date.now; }
  get state(): State { return this.stateValue; }
  protected abstract clear(): void;
  cancel(): void { if (this.stateValue === 'committed') return; this.stateValue = 'cancelled'; this.abort.abort(); this.clear(); }
  protected live(expiresAt: number): void {
    if (this.abort.signal.aborted || this.stateValue === 'cancelled' || this.stateValue === 'expired') fail('state');
    try { alive(expiresAt, this.now()); }
    catch { this.stateValue = 'expired'; this.abort.abort(); this.clear(); fail('expired'); }
  }
  protected async exclusive<T>(run: () => Promise<T>): Promise<T> {
    if (this.busy) return fail('state');
    this.busy = true;
    try { return await run(); }
    catch (e) { if (e instanceof LinkError) throw e; return fail('crypto'); }
    finally { this.busy = false; }
  }
}
async function validate(authority: IdentityAdapter, payload: Uint8Array<ArrayBuffer>, id: Identity, track: (b: Uint8Array<ArrayBuffer>) => Uint8Array<ArrayBuffer> = b => b, release: (b: Uint8Array<ArrayBuffer>) => void = b => { b.fill(0); }): Promise<void> {
  const copy = track(payload.slice());
  try { await adapter('identity', () => authority.validateKeyring(copy, structuredClone(id))); }
  finally { release(copy); }
}
async function current(authority: IdentityAdapter, b: Binding, now: () => number): Promise<Checkpoint> {
  const c = await adapter('authority', () => authority.current(structuredClone(b)));
  // A decision may never outlive the pairing session and must be fresh now.
  try {
    const row = record(c, ['revision', 'validUntil']);
    const checkpoint = { revision: text(row.revision), validUntil: integer(row.validUntil) };
    if (checkpoint.validUntil <= now() || checkpoint.validUntil > b.expiresAt) return fail('authority');
    return checkpoint;
  } catch { return fail('authority'); }
}

export class Sender extends Session {
  #offer: Offer;
  #binding: Binding;
  #keys: SessionKeys | undefined;
  #payload: Uint8Array<ArrayBuffer> | undefined;
  #envelope: Envelope | undefined;
  #authority: IdentityAdapter;
  #completionKey: CryptoKey | undefined;
  private constructor(o: Offer, b: Binding, k: SessionKeys, payload: Uint8Array<ArrayBuffer>, authority: IdentityAdapter, options: Options) {
    super(options); this.#offer = o; this.#binding = b; this.#keys = k; this.#completionKey = k.authentication; this.#payload = payload; this.#authority = authority; this.stateValue = 'bound';
  }
  static async create(input: { request: Request; expectedScope: Scope; identity: Identity; keyring: Uint8Array; authority: IdentityAdapter }, options: Options = {}): Promise<Sender> {
    const r = request(input.request), id = identity(input.identity);
    sameScope(r.scope, input.expectedScope);
    const now = options.now ?? Date.now;
    alive(r.expiresAt, now());
    if (!(input.keyring instanceof Uint8Array) || !input.keyring.length || input.keyring.length > MAX_KEYRING_BYTES) return fail('invalid');
    const payload = new Uint8Array(input.keyring);
    try {
      await validate(input.authority, payload, id);
      const pair = await ephemeral();
      const o: Offer = { request: r, senderKey: pair.publicKey, identity: id, payloadHash: await hash(payload) };
      const transcript = await hash(canonical(o)), b = binding(o, transcript);
      await current(input.authority, b, now);
      const k = await keys(pair.privateKey, r.receiverKey, transcript);
      alive(r.expiresAt, now());
      return new Sender(o, b, k, payload, input.authority, options);
    } catch (e) { payload.fill(0); if (e instanceof LinkError) throw e; return fail('crypto'); }
  }
  get offer(): Offer { return structuredClone(this.#offer); }
  get comparison(): string { return comparison(this.#binding.transcript); }
  get binding(): Binding { return structuredClone(this.#binding); }
  protected clear(): void { this.#payload?.fill(0); this.#payload = undefined; this.#keys = undefined; this.#completionKey = undefined; this.#envelope = undefined; }
  /** Pass the exact full comparison read from the receiving device over a
   * trusted independent channel. Never obtain it from the transport. */
  confirm(peerComparison: string): void {
    if (this.stateValue !== 'bound' || this.busy) return fail('state');
    this.live(this.#binding.expiresAt);
    if (peerComparison !== this.comparison) { this.cancel(); return fail('comparison'); }
    this.stateValue = 'confirmed';
  }
  private canSend(): void {
    if (this.stateValue !== 'sent') { this.live(this.#binding.expiresAt); return; }
    if (this.abort.signal.aborted) return fail('state');
    try { alive(this.#binding.expiresAt, this.now()); }
    catch {
      // Import deadline ends uploads, not authentication of a durable completion.
      this.#keys = undefined; this.#envelope = undefined;
      return fail('expired');
    }
  }
  async send(transport: Transport): Promise<void> {
    return this.exclusive(async () => {
      if (this.stateValue !== 'confirmed' && this.stateValue !== 'sent') return fail('state');
      this.canSend();
      await current(this.#authority, this.#binding, this.now);
      this.canSend();
      if (!this.#envelope) {
        const sealed = await seal(this.#keys!.encryption, this.#offer, this.#binding.transcript, this.#payload!);
        this.canSend();
        this.#envelope = sealed; this.#payload?.fill(0); this.#payload = undefined;
      }
      // Enter the completion-waiting state BEFORE handing off to an untrusted
      // transport: a rejected response does not prove that upload failed.
      this.stateValue = 'sent';
      await adapter('transport', () => transport.send(this.#binding.session, structuredClone(this.#envelope!)));
      if (this.abort.signal.aborted) return fail('state');
    });
  }
  async finish(transport: Transport): Promise<void> {
    return this.exclusive(async () => {
      if (this.stateValue !== 'sent') return fail('state');
      const value = await adapter('transport', () => transport.completed(this.#binding.session));
      if (this.abort.signal.aborted) return fail('state');
      if (!value) return fail('pending');
      await checkCompletion(this.#completionKey!, this.#binding.transcript, done(value));
      if (this.abort.signal.aborted) return fail('state');
      this.stateValue = 'committed'; this.clear();
    });
  }
}

export class Receiver extends Session {
  #request: Request;
  #privateKey: CryptoKey | undefined;
  #offer: Offer | undefined;
  #binding: Binding | undefined;
  #keys: SessionKeys | undefined;
  private constructor(r: Request, privateKey: CryptoKey, options: Options) { super(options); this.#request = r; this.#privateKey = privateKey; }
  static async create(expectedScope: Scope, options: Options & { ttlMs?: number } = {}): Promise<Receiver> {
    const s = scope(expectedScope), now = options.now ?? Date.now;
    const start = integer(now()), ttl = integer(options.ttlMs ?? 120000);
    alive(start + ttl, start);
    const pair = await ephemeral();
    const r: Request = { v: 1, session: b64(crypto.getRandomValues(new Uint8Array(32))), receiverKey: pair.publicKey, expiresAt: start + ttl, scope: s };
    alive(r.expiresAt, now());
    return new Receiver(r, pair.privateKey, options);
  }
  get request(): Request { return structuredClone(this.#request); }
  get comparison(): string { if (!this.#binding) return fail('state'); return comparison(this.#binding.transcript); }
  get binding(): Binding { if (!this.#binding) return fail('state'); return structuredClone(this.#binding); }
  protected clear(): void { this.#privateKey = undefined; this.#keys = undefined; this.wipe(); }
  async bind(value: Offer): Promise<void> {
    return this.exclusive(async () => {
      this.live(this.#request.expiresAt);
      if (this.stateValue !== 'created') return fail('state');
      const o = offer(value);
      if (JSON.stringify(o.request) !== JSON.stringify(this.#request)) return fail('scope');
      const transcript = await hash(canonical(o));
      const k = await keys(this.#privateKey!, o.senderKey, transcript);
      this.live(this.#request.expiresAt);
      this.#offer = o; this.#binding = binding(o, transcript); this.#keys = k; this.#privateKey = undefined; this.stateValue = 'bound';
    });
  }
  confirm(peerComparison: string): void {
    this.live(this.#request.expiresAt);
    if (this.stateValue !== 'bound' || this.busy) return fail('state');
    if (peerComparison !== this.comparison) { this.cancel(); return fail('comparison'); }
    this.stateValue = 'confirmed';
  }
  async receive(transport: Transport, authority: IdentityAdapter, storage: StorageAdapter): Promise<void> {
    return this.exclusive(async () => {
      if (this.stateValue !== 'confirmed') return fail('state');
      this.live(this.#request.expiresAt);
      const b = this.#binding!, k = this.#keys!;
      const previous = await adapter('storage', () => storage.lookup(structuredClone(b)));
      this.live(b.expiresAt);
      if (previous) {
        const d = done(previous);
        await checkCompletion(k.authentication, b.transcript, d);
        this.live(b.expiresAt);
        await adapter('transport', () => transport.complete(b.session, structuredClone(d)));
        this.live(b.expiresAt);
        this.stateValue = 'committed'; this.clear(); return;
      }
      const raw = await adapter('transport', () => transport.receive(b.session));
      this.live(b.expiresAt);
      if (!raw) return fail('pending');
      const e = envelope(raw);
      if (e.transcript !== b.transcript) return fail('crypto');
      const payload = this.track(await open(k.encryption, this.#offer!, e));
      try {
        this.live(b.expiresAt);
        if (await hash(payload) !== this.#offer!.payloadHash) return fail('crypto');
        this.live(b.expiresAt);
        await validate(authority, payload, b.identity, bytes => this.track(bytes), bytes => this.release(bytes));
        this.live(b.expiresAt);
        const initial = await current(authority, b, this.now);
        this.live(b.expiresAt);
        const d = await completion(k.authentication, b.transcript);
        this.live(b.expiresAt);
        const copy = this.track(payload.slice());
        let guarded = false;
        try {
          await adapter('storage', () => storage.commit({ binding: structuredClone(b), keyring: copy, completion: structuredClone(d), signal: this.abort.signal,
            beforeCommit: async () => {
              this.live(b.expiresAt);
              const fresh = await current(authority, b, this.now);
              this.live(b.expiresAt);
              if (fresh.revision !== initial.revision) return fail('authority');
              guarded = true;
              return fresh;
            } }));
        } finally { this.release(copy); }
        // Correctness of atomic persistence and callback timing belongs to the
        // trusted storage adapter. Refuse to report success if it skipped guard.
        if (!guarded) return fail('storage');
        const saved = await adapter('storage', () => storage.lookup(structuredClone(b)));
        this.live(b.expiresAt);
        if (!saved) return fail('storage');
        await checkCompletion(k.authentication, b.transcript, done(saved));
        this.live(b.expiresAt);
        await adapter('transport', () => transport.complete(b.session, structuredClone(d)));
        this.live(b.expiresAt);
        this.stateValue = 'committed'; this.clear();
      } finally { this.release(payload); }
    });
  }
}

/** After a reload or an uncertain commit, publish ONLY the stored completion.
 * This never imports keys or authenticates a new application session. It may
 * run after transfer expiry, because no new import occurs. Storage must verify
 * the entire binding before returning a durable completion. */
export async function reconcile(bindingValue: Binding, storage: StorageAdapter, transport: Transport): Promise<boolean> {
  const r = record(bindingValue, ['session', 'transcript', 'expiresAt', 'scope', 'identity']);
  unb64(r.session, 32); unb64(r.transcript, 32);
  const b: Binding = { session: r.session as string, transcript: r.transcript as string, expiresAt: integer(r.expiresAt), scope: scope(r.scope), identity: identity(r.identity) };
  const value = await adapter('storage', () => storage.lookup(structuredClone(b)));
  if (!value) return false;
  const d = done(value);
  if (d.transcript !== b.transcript) return fail('storage');
  await adapter('transport', () => transport.complete(b.session, d));
  return true;
}
