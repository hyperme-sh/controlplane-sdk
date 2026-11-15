import assert from 'node:assert/strict';
import { Receiver, Sender } from '../dist/index.js';
export const scope = { sourceOrigin: 'https://source.example', destinationOrigin: 'https://destination.example', application: 'fixture', tenant: 'tenant-a', audience: 'test' };
export async function fixture() {
  let clock = 1000000;
  const options = { now: () => clock };
  const pair = async (name) => {
    const p = await crypto.subtle.generateKey({ name, namedCurve: 'P-256' }, true, name === 'ECDSA' ? ['sign', 'verify'] : ['deriveBits']);
    return crypto.subtle.exportKey('jwk', p.privateKey);
  };
  const signing = await pair('ECDSA'), encryption = await pair('ECDH'), retired = await pair('ECDH');
  const point = k => `${k.x}.${k.y}`;
  const id = { principal: point(signing), pub: point(signing), epub: point(encryption), rotationSeq: 1 };
  // Synthetic opaque contract fixture, NOT a SociACL codec or history verifier.
  const value = { identity: id, signing, encryption, retired: [retired], lanes: ['current', 'prior'], contactSecrets: ['current-secret', 'prior-secret'] };
  const bytes = new TextEncoder().encode(JSON.stringify(value));
  let revoked = false, revision = 'checkpoint-1';
  const authority = {
    async validateKeyring(input, identity) { assert.deepEqual(identity, id); assert.deepEqual(input, bytes); },
    async current(binding) {
      if (revoked) throw Error('private diagnostic');
      assert.deepEqual(binding.identity, id); assert.deepEqual(binding.scope, scope);
      return { revision, validUntil: Math.min(clock + 1000, binding.expiresAt) };
    },
  };
  const receiver = await Receiver.create(scope, options);
  const sender = await Sender.create({ request: receiver.request, expectedScope: scope, identity: id, keyring: bytes, authority }, options);
  await receiver.bind(sender.offer);
  const transfer = new Map(), completed = new Map();
  const transport = {
    async send(session, envelope) { if (transfer.has(session)) assert.deepEqual(transfer.get(session), envelope); transfer.set(session, structuredClone(envelope)); },
    async receive(session) { return structuredClone(transfer.get(session) ?? null); },
    async complete(session, done) { if (completed.has(session)) assert.deepEqual(completed.get(session), done); completed.set(session, structuredClone(done)); },
    async completed(session) { return structuredClone(completed.get(session) ?? null); },
  };
  let saved, commits = 0, imported;
  const storage = {
    async commit(input) {
      const checkpoint = await input.beforeCommit();
      if (input.signal.aborted || clock >= input.binding.expiresAt || clock >= checkpoint.validUntil) throw Error('aborted');
      if (saved) { assert.deepEqual(saved.binding, input.binding); return; }
      imported = input.keyring.slice(); commits++;
      saved = structuredClone({ binding: input.binding, completion: input.completion, checkpoint });
    },
    async lookup(binding) { if (!saved) return null; assert.deepEqual(binding, saved.binding); return structuredClone(saved.completion); },
  };
  return { sender, receiver, bytes, id, authority, storage, transport, transfer, completed, options,
    confirm() { sender.confirm(receiver.comparison); receiver.confirm(sender.comparison); },
    advance(ms) { clock += ms; }, revoke() { revoked = true; }, rotate() { revision = 'checkpoint-2'; },
    get imported() { return imported; }, get commits() { return commits; }, get saved() { return saved; },
  };
}
export const refuses = (code) => (e) => e.code === code && e.message === code;
