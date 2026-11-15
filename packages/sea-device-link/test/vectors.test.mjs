import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { canonical, hash, comparison, unb64 } from '../dist/wire.js';
import { keys, open, completion, checkCompletion } from '../dist/crypto.js';
import { encodeRequest, decodeRequest } from '../dist/index.js';
const v = JSON.parse(await readFile(new URL('../vectors/v1.json', import.meta.url), 'utf8'));
test('v1 canonical transcript, full comparison and public text match independent vector', async () => {
  assert.equal(new TextDecoder().decode(canonical(v.offer)), v.canonical);
  assert.equal(await hash(canonical(v.offer)), v.transcript);
  assert.equal(comparison(v.transcript), v.comparison);
  assert.equal(encodeRequest(v.offer.request), v.requestText);
  assert.deepEqual(decodeRequest(v.requestText), v.offer.request);
});
test('v1 ECDH/HKDF/AES-GCM/HMAC match independent vector', async () => {
  const [x, y] = v.offer.request.receiverKey.split('.');
  const privateKey = await crypto.subtle.importKey('jwk', {kty: 'EC', crv: 'P-256', x, y, d: v.receiverScalar}, {name: 'ECDH', namedCurve: 'P-256'}, false, ['deriveBits']);
  const k = await keys(privateKey, v.offer.senderKey, v.transcript);
  assert.deepEqual(await open(k.encryption, v.offer, v.envelope), unb64(v.payload, 1, 100));
  assert.deepEqual(await completion(k.authentication, v.transcript), v.completion);
  await checkCompletion(k.authentication, v.transcript, v.completion);
});
