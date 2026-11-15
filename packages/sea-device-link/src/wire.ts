import { LinkError, type Binding, type Identity, type Offer, type Request, type Scope } from './types.js';
export const MAX_KEYRING_BYTES = 524288;
export const MAX_SESSION_MS = 300000;
const encoder = new TextEncoder();
export const utf8 = (value: string): Uint8Array<ArrayBuffer> => encoder.encode(value);
export const fail = (code: ConstructorParameters<typeof LinkError>[0]): never => { throw new LinkError(code); };
export function record(value: unknown, keys: string[]): Record<string, unknown> {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return fail('invalid');
  const row = value as Record<string, unknown>;
  if (Object.keys(row).sort().join(',') !== [...keys].sort().join(',')) return fail('invalid');
  return row;
}
export function text(value: unknown, max = 256): string {
  if (typeof value !== 'string' || !value.length || value.length > max || /[\x00-\x1f\x7f]/.test(value)) return fail('invalid');
  return value;
}
export function integer(value: unknown): number {
  if (typeof value !== 'number' || !Number.isSafeInteger(value) || value < 0) return fail('invalid');
  return value;
}
export function b64(bytes: Uint8Array): string {
  let out = '';
  for (const byte of bytes) out += String.fromCharCode(byte);
  return btoa(out).replaceAll('+', '-').replaceAll('/', '_').replace(/=+$/, '');
}
export function unb64(value: unknown, min: number, max = min): Uint8Array<ArrayBuffer> {
  if (typeof value !== 'string' || value.length > Math.ceil(max * 4 / 3) || !/^[A-Za-z0-9_-]+$/.test(value)) return fail('invalid');
  let raw: string;
  try { raw = atob(value.replaceAll('-', '+').replaceAll('_', '/')); } catch { return fail('invalid'); }
  const bytes = Uint8Array.from(raw, c => c.charCodeAt(0));
  if (bytes.length < min || bytes.length > max || b64(bytes) !== value) return fail('invalid');
  return bytes;
}
export function point(value: unknown): string {
  const s = text(value, 87);
  const parts = s.split('.');
  if (parts.length !== 2) return fail('invalid');
  unb64(parts[0], 32); unb64(parts[1], 32);
  return s;
}
function origin(value: unknown): string {
  const s = text(value);
  let u: URL;
  try { u = new URL(s); } catch { return fail('invalid'); }
  if (u.protocol !== 'https:' || u.origin !== s) return fail('invalid');
  return s;
}
export function scope(value: unknown): Scope {
  const r = record(value, ['sourceOrigin', 'destinationOrigin', 'application', 'tenant', 'audience']);
  return { sourceOrigin: origin(r.sourceOrigin), destinationOrigin: origin(r.destinationOrigin),
    application: text(r.application), tenant: text(r.tenant), audience: text(r.audience) };
}
export function identity(value: unknown): Identity {
  const r = record(value, ['principal', 'pub', 'epub', 'rotationSeq']);
  const seq = integer(r.rotationSeq);
  if (seq > 1024) return fail('invalid');
  return { principal: point(r.principal), pub: point(r.pub), epub: point(r.epub), rotationSeq: seq };
}
export function request(value: unknown): Request {
  const r = record(value, ['v', 'session', 'receiverKey', 'expiresAt', 'scope']);
  if (r.v !== 1) return fail('invalid');
  unb64(r.session, 32);
  return { v: 1, session: r.session as string, receiverKey: point(r.receiverKey), expiresAt: integer(r.expiresAt), scope: scope(r.scope) };
}
export function offer(value: unknown): Offer {
  const r = record(value, ['request', 'senderKey', 'identity', 'payloadHash']);
  unb64(r.payloadHash, 32);
  return { request: request(r.request), senderKey: point(r.senderKey), identity: identity(r.identity), payloadHash: r.payloadHash as string };
}
export function alive(expiresAt: number, now: number): void {
  integer(now);
  if (expiresAt <= now || expiresAt - now > MAX_SESSION_MS) fail('expired');
}
export function sameScope(a: Scope, b: Scope): void {
  if (JSON.stringify(scope(a)) !== JSON.stringify(scope(b))) fail('scope');
}
export function canonical(value: Offer): Uint8Array<ArrayBuffer> {
  const o = offer(value), r = o.request, s = r.scope, i = o.identity;
  return utf8(JSON.stringify(['sea-device-link/v1', r.session, r.receiverKey, r.expiresAt,
    s.sourceOrigin, s.destinationOrigin, s.application, s.tenant, s.audience,
    o.senderKey, i.principal, i.pub, i.epub, i.rotationSeq, o.payloadHash]));
}
export async function hash(bytes: Uint8Array<ArrayBuffer>): Promise<string> {
  return b64(new Uint8Array(await crypto.subtle.digest('SHA-256', bytes)));
}
export function binding(o: Offer, transcript: string): Binding {
  return { session: o.request.session, transcript, expiresAt: o.request.expiresAt, scope: structuredClone(o.request.scope), identity: structuredClone(o.identity) };
}
/** Public data only. QR and camera-free text carry the SAME full request. */
export function encodeRequest(value: Request): string { return 'sea-link-v1:' + b64(utf8(JSON.stringify(request(value)))); }
export function decodeRequest(value: string): Request {
  if (typeof value !== 'string' || !value.startsWith('sea-link-v1:')) return fail('invalid');
  try { return request(JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(unb64(value.slice(12), 1, 4096)))); }
  catch { return fail('invalid'); }
}
/** Compare all 256 bits on a trusted out-of-band channel, never via the relay. */
export function comparison(transcript: string): string {
  return Array.from(unb64(transcript, 32), b => b.toString(16).padStart(2, '0')).join('').match(/.{8}/g)!.join('-');
}
