import { mkdtemp, readFile, writeFile, rm, readdir } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { execFileSync } from 'node:child_process';
import assert from 'node:assert/strict';
const root = process.cwd();
const temporary = await mkdtemp(join(tmpdir(), 'sea-link-consumer-'));
try {
  const output = JSON.parse(execFileSync('npm', ['pack', '--json', '--ignore-scripts', '--pack-destination', temporary], {cwd: root, encoding: 'utf8'}));
  const files = output[0].files.map(f => f.path);
  assert(files.includes('dist/index.js')); assert(files.includes('dist/index.d.ts')); assert(files.includes('vectors/v1.json'));
  assert(!files.some(f => /^(src|test|node_modules)\//.test(f)));
  for (const name of await readdir(join(root, 'dist'))) {
    if (name.endsWith('.js')) assert(!/node:|\brequire\(|\bBuffer\b|process\./.test(await readFile(join(root, 'dist', name), 'utf8')));
  }
  await writeFile(join(temporary, 'package.json'), JSON.stringify({private: true, type: 'module'}));
  execFileSync('npm', ['install', '--offline', '--ignore-scripts', '--no-audit', '--no-fund', '--no-package-lock', join(temporary, output[0].filename)], {cwd: temporary, stdio: 'inherit'});
  execFileSync(process.execPath, ['--input-type=module', '-e', "import {Receiver, Sender, decodeRequest, reconcile} from 'sea-device-link'; if (![Receiver, Sender, decodeRequest, reconcile].every(x => typeof x === 'function')) throw Error('exports'); try { await import('sea-device-link/dist/wire.js'); throw Error('internal export exposed'); } catch (e) { if (e.code !== 'ERR_PACKAGE_PATH_NOT_EXPORTED') throw e; }"], {cwd: temporary, stdio: 'inherit'});
  await writeFile(join(temporary, 'consumer.ts'), "import {Receiver, type StorageAdapter, type IdentityAdapter} from 'sea-device-link'; const create: typeof Receiver.create = Receiver.create; export {create}; export type {StorageAdapter, IdentityAdapter};\n");
  execFileSync(process.execPath, [resolve(root, 'node_modules/typescript/bin/tsc'), '--strict', '--noEmit', '--target', 'ES2022', '--module', 'NodeNext', '--moduleResolution', 'NodeNext', join(temporary, 'consumer.ts')], {cwd: temporary, stdio: 'inherit'});
} finally { await rm(temporary, {recursive: true, force: true}); }
