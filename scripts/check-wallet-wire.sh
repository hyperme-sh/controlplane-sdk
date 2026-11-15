#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT
packages/sea-device-link/node_modules/.bin/tsc --target ES2020 --module commonjs --lib ES2020,DOM --outDir "$scratch" \
 sdk/rest/typescript-fetch/models/WalletPaymentChallengeRequest.ts \
 sdk/rest/typescript-fetch/models/WalletPaymentUsdcLeasePaymentCreate.ts \
 sdk/rest/typescript-fetch/models/WalletPaymentSubmitRequest.ts
node tests/wallet-typescript.cjs "$scratch"
bash sdk/rest/kotlin/gradlew --no-daemon -p tests/wallet-kotlin test
