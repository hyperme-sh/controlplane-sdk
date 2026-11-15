import { b64, canonical, fail, unb64, utf8 } from './wire.js';
import type { Completion, Envelope, Offer } from './types.js';
export async function ephemeral(): Promise<{ privateKey: CryptoKey; publicKey: string }> {
  const pair = await crypto.subtle.generateKey({ name: 'ECDH', namedCurve: 'P-256' }, false, ['deriveBits']);
  const jwk = await crypto.subtle.exportKey('jwk', pair.publicKey);
  return { privateKey: pair.privateKey, publicKey: `${jwk.x}.${jwk.y}` };
}
export async function keys(privateKey: CryptoKey, peer: string, transcript: string): Promise<{ encryption: CryptoKey; authentication: CryptoKey }> {
  const [x, y] = peer.split('.');
  const publicKey = await crypto.subtle.importKey('jwk', { kty: 'EC', crv: 'P-256', x, y }, { name: 'ECDH', namedCurve: 'P-256' }, false, []);
  const raw = new Uint8Array(await crypto.subtle.deriveBits({ name: 'ECDH', public: publicKey }, privateKey, 256));
  try {
    const base = await crypto.subtle.importKey('raw', raw, 'HKDF', false, ['deriveKey']);
    const params = (purpose: string) => ({ name: 'HKDF', hash: 'SHA-256', salt: unb64(transcript, 32), info: utf8(`sea-device-link/v1/${purpose}`) });
    return {
      encryption: await crypto.subtle.deriveKey(params('payload'), base, { name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']),
      authentication: await crypto.subtle.deriveKey(params('completion'), base, { name: 'HMAC', hash: 'SHA-256', length: 256 }, false, ['sign', 'verify']),
    };
  } finally { raw.fill(0); }
}
export async function seal(key: CryptoKey, o: Offer, transcript: string, payload: Uint8Array<ArrayBuffer>): Promise<Envelope> {
  const iv = crypto.getRandomValues(new Uint8Array(12));
  return { transcript, iv: b64(iv), ciphertext: b64(new Uint8Array(await crypto.subtle.encrypt({ name: 'AES-GCM', iv, additionalData: canonical(o), tagLength: 128 }, key, payload))) };
}
export async function open(key: CryptoKey, o: Offer, envelope: Envelope): Promise<Uint8Array<ArrayBuffer>> {
  return new Uint8Array(await crypto.subtle.decrypt({ name: 'AES-GCM', iv: unb64(envelope.iv, 12), additionalData: canonical(o), tagLength: 128 }, key, unb64(envelope.ciphertext, 17, 524304)));
}
const doneBytes = (transcript: string) => utf8(`sea-device-link/v1/committed\n${transcript}`);
export async function completion(key: CryptoKey, transcript: string): Promise<Completion> {
  return { transcript, mac: b64(new Uint8Array(await crypto.subtle.sign('HMAC', key, doneBytes(transcript)))) };
}
export async function checkCompletion(key: CryptoKey, transcript: string, done: Completion): Promise<void> {
  if (done.transcript !== transcript || !await crypto.subtle.verify('HMAC', key, unb64(done.mac, 32), doneBytes(transcript))) fail('crypto');
}
