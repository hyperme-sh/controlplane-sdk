import test from 'node:test';
import assert from 'node:assert/strict';
import { Receiver, Sender, encodeRequest, decodeRequest, reconcile } from '../dist/index.js';
import { fixture, scope, refuses } from './support.mjs';

test('two clients preserve the full opaque keyring and authenticate durable completion', async () => {
  const f = await fixture(); f.confirm();
  await f.sender.send(f.transport); await f.receiver.receive(f.transport, f.authority, f.storage); await f.sender.finish(f.transport);
  assert.equal(f.sender.state, 'committed'); assert.equal(f.receiver.state, 'committed'); assert.equal(f.commits, 1);
  assert.deepEqual(f.imported, f.bytes);
  const restored = JSON.parse(new TextDecoder().decode(f.imported));
  assert.equal(restored.retired.length, 1); assert.equal(restored.contactSecrets.length, 2);
  // An actual retired ECDH private key remains usable after transfer.
  const old = restored.retired[0];
  const privateKey = await crypto.subtle.importKey('jwk', old, { name: 'ECDH', namedCurve: 'P-256' }, false, ['deriveBits']);
  const peer = await crypto.subtle.generateKey({ name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveBits']);
  const oldPub = await crypto.subtle.importKey('jwk', {kty: 'EC', crv: 'P-256', x: old.x, y: old.y}, { name: 'ECDH', namedCurve: 'P-256' }, false, []);
  assert.deepEqual(new Uint8Array(await crypto.subtle.deriveBits({name: 'ECDH', public: peer.publicKey}, privateKey, 256)),
    new Uint8Array(await crypto.subtle.deriveBits({name: 'ECDH', public: oldPub}, peer.privateKey, 256)));
  assert.equal(JSON.stringify([...f.transfer.values()]).includes('current-secret'), false);
});
test('QR and camera-free representation are identical public-only request bytes', async () => {
  const f = await fixture(), encoded = encodeRequest(f.receiver.request);
  assert.deepEqual(decodeRequest(encoded), f.receiver.request);
  assert.equal(encoded.includes('priv'), false);
  for (const input of ['', encoded + '=', 'https://wrong.example', 'sea-link-v1:!!!!', 'sea-link-v1:' + 'a'.repeat(6000)]) assert.throws(() => decodeRequest(input), refuses('invalid'));
  assert.throws(() => encodeRequest({...f.receiver.request, extra: true}), refuses('invalid'));
});
test('both endpoints require complete independent comparison before transfer', async () => {
  const f = await fixture();
  await assert.rejects(f.sender.send(f.transport), refuses('state'));
  await assert.rejects(f.receiver.receive(f.transport, f.authority, f.storage), refuses('state'));
  assert.throws(() => f.sender.confirm(f.receiver.comparison.slice(0, 8)), refuses('comparison'));
  assert.equal(f.sender.state, 'cancelled');
  const g = await fixture(); assert.throws(() => g.receiver.confirm('wrong'), refuses('comparison'));
});
test('scope, request substitution and malformed points fail closed', async () => {
  const f = await fixture();
  await assert.rejects(Sender.create({request: f.receiver.request, expectedScope: {...scope, tenant: 'other'}, identity: f.id, keyring: f.bytes, authority: f.authority}, f.options), refuses('scope'));
  const r = await Receiver.create(scope, f.options);
  await assert.rejects(r.bind(f.sender.offer), refuses('scope'));
  await assert.rejects(Sender.create({request: {...f.receiver.request, receiverKey: 'bad'}, expectedScope: scope, identity: f.id, keyring: f.bytes, authority: f.authority}, f.options), refuses('invalid'));
  await assert.rejects(Receiver.create({...scope, destinationOrigin: 'http://unsafe.example'}, f.options), refuses('invalid'));
});
test('adapter rejects mismatched keyring before an offer exists', async () => {
  const f = await fixture();
  await assert.rejects(Sender.create({request: f.receiver.request, expectedScope: scope, identity: f.id, keyring: new Uint8Array([1]), authority: f.authority}, f.options), refuses('identity'));
});
test('offers and requests are immutable snapshots', async () => {
  const f = await fixture();
  const o = f.sender.offer; o.identity.pub = 'bad'; o.request.scope.tenant = 'other';
  const r = f.receiver.request; r.scope.tenant = 'other';
  f.confirm(); await f.sender.send(f.transport); await f.receiver.receive(f.transport, f.authority, f.storage);
  assert.equal(f.commits, 1);
});
for (const field of ['ciphertext', 'iv', 'transcript']) test(`tampered ${field} cannot import`, async () => {
  const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
  const e = f.transfer.get(f.receiver.request.session); e[field] = (e[field][0] === 'A' ? 'B' : 'A') + e[field].slice(1);
  await assert.rejects(f.receiver.receive(f.transport, f.authority, f.storage)); assert.equal(f.commits, 0);
});
test('unsupported version, overlarge payload and unbounded session TTL refuse', async () => {
  const f = await fixture();
  assert.throws(() => encodeRequest({...f.receiver.request, v: 2}), refuses('invalid'));
  await assert.rejects(Receiver.create(scope, {...f.options, ttlMs: 300001}), refuses('expired'));
  await assert.rejects(Sender.create({request: f.receiver.request, expectedScope: scope, identity: f.id, keyring: new Uint8Array(524289), authority: f.authority}, f.options), refuses('invalid'));
});
test('expiry and cancellation prevent sending/import', async () => {
  const f = await fixture(); f.confirm(); f.advance(120000);
  await assert.rejects(f.sender.send(f.transport), refuses('expired'));
  await assert.rejects(f.receiver.receive(f.transport, f.authority, f.storage), refuses('expired'));
  const g = await fixture(); g.confirm(); await g.sender.send(g.transport); g.receiver.cancel();
  await assert.rejects(g.receiver.receive(g.transport, g.authority, g.storage), refuses('state'));
  assert.equal(g.commits, 0);
});
test('revoked sender or receiver identity fails with sanitized errors', async () => {
  const f = await fixture(); f.confirm(); f.revoke(); await assert.rejects(f.sender.send(f.transport), refuses('authority'));
  const g = await fixture(); g.confirm(); await g.sender.send(g.transport); g.revoke();
  await assert.rejects(g.receiver.receive(g.transport, g.authority, g.storage), refuses('authority')); assert.equal(g.commits, 0);
});
test('rotation while waiting for destination lock refuses commit', async () => {
  const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
  const storage = {...f.storage, async commit(input) { f.rotate(); return f.storage.commit(input); }};
  await assert.rejects(f.receiver.receive(f.transport, f.authority, storage), refuses('storage')); assert.equal(f.commits, 0);
});
test('expiry and cancel during asynchronous storage preparation refuse commit', async () => {
  for (const action of [f => f.advance(120000), f => f.receiver.cancel()]) {
    const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
    await assert.rejects(f.receiver.receive(f.transport, f.authority, {...f.storage, async commit(input) { action(f); return f.storage.commit(input); }}), refuses('storage'));
    assert.equal(f.commits, 0);
  }
});
test('destination conflict and skipped precommit validation do not report success', async () => {
  const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
  await assert.rejects(f.receiver.receive(f.transport, f.authority, {...f.storage, async commit() { throw Error('different local identity'); }}), refuses('storage'));
  await assert.rejects(f.receiver.receive(f.transport, f.authority, {...f.storage, async commit() {} }), refuses('storage'));
  assert.equal(f.completed.size, 0);
});
test('lost send response retries the exact same ciphertext', async () => {
  const f = await fixture(); f.confirm();
  await assert.rejects(f.sender.send({...f.transport, async send(...args) { await f.transport.send(...args); throw Error('lost'); }}), refuses('transport'));
  const first = structuredClone([...f.transfer.values()][0]); await f.sender.send(f.transport);
  assert.deepEqual([...f.transfer.values()][0], first);
});
test('lost commit response retries without importing twice', async () => {
  const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
  await assert.rejects(f.receiver.receive(f.transport, f.authority, {...f.storage, async commit(input) { await f.storage.commit(input); throw Error('lost'); }}), refuses('storage'));
  await f.receiver.receive(f.transport, f.authority, f.storage); await f.sender.finish(f.transport); assert.equal(f.commits, 1);
});
test('reload and expired session can republish a stored completion without another import', async () => {
  const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
  await assert.rejects(f.receiver.receive({...f.transport, async complete() { throw Error('lost'); }}, f.authority, f.storage), refuses('transport'));
  f.advance(120000); f.receiver.cancel();
  assert.equal(await reconcile(f.sender.binding, f.storage, f.transport), true);
  await f.sender.finish(f.transport); assert.equal(f.commits, 1);
});
test('forged completion is rejected by sender', async () => {
  const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
  f.completed.set(f.receiver.request.session, {transcript: f.sender.binding.transcript, mac: 'A'.repeat(43)});
  await assert.rejects(f.sender.finish(f.transport), refuses('crypto')); assert.equal(f.sender.state, 'sent');
});
test('concurrent delivery is refused and repeated completed import cannot execute', async () => {
  const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
  let unlock; const gate = new Promise(r => unlock = r);
  const first = f.receiver.receive({...f.transport, async receive(session) { await gate; return f.transport.receive(session); }}, f.authority, f.storage);
  await assert.rejects(f.receiver.receive(f.transport, f.authority, f.storage), refuses('state'));
  unlock(); await first;
  await assert.rejects(f.receiver.receive(f.transport, f.authority, f.storage), refuses('state')); assert.equal(f.commits, 1);
});
test('missing relay data is pending and adapter private diagnostics are not leaked', async () => {
  const f = await fixture(); f.confirm();
  await assert.rejects(f.receiver.receive(f.transport, f.authority, f.storage), refuses('pending'));
  await assert.rejects(f.sender.send({...f.transport, async send() { throw Error('secret diagnostic'); }}), refuses('transport'));
});
test('expired or overlong authority decisions refuse import', async () => {
  for (const validUntil of [0, 9999999999999]) {
    const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
    await assert.rejects(f.receiver.receive(f.transport, {...f.authority, async current() { return {revision: 'bad', validUntil}; }}, f.storage), refuses('authority'));
    assert.equal(f.commits, 0);
  }
});
test('cancellation during relay read never reaches keyring validation', async () => {
  const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
  let validations = 0;
  await assert.rejects(f.receiver.receive({...f.transport, async receive(session) { f.receiver.cancel(); return f.transport.receive(session); }},
    {...f.authority, async validateKeyring() { validations++; }}, f.storage), refuses('state'));
  assert.equal(validations, 0); assert.equal(f.commits, 0);
});
test('source cancellation while authority is pending never uploads ciphertext', async () => {
  const f = await fixture(); f.confirm(); const current = f.authority.current;
  f.authority.current = async binding => { f.sender.cancel(); return current(binding); };
  await assert.rejects(f.sender.send(f.transport), refuses('state')); assert.equal(f.transfer.size, 0);
});
test('plaintext borrowed by validation/storage is cleared after failure and commit', async () => {
  const f = await fixture(); f.confirm(); await f.sender.send(f.transport);
  let validationBytes, storageBytes;
  await f.receiver.receive(f.transport, {...f.authority, async validateKeyring(bytes, id) { validationBytes = bytes; await f.authority.validateKeyring(bytes, id); }},
    {...f.storage, async commit(input) { storageBytes = input.keyring; await f.storage.commit(input); }});
  assert(validationBytes.every(byte => byte === 0)); assert(storageBytes.every(byte => byte === 0));
  assert.deepEqual(f.imported, f.bytes);
});
