const assert = require('node:assert/strict');
const path = require('node:path');
const root = process.argv[2];
const load = name => require(path.join(root, 'models', name + '.js'));
assert.deepEqual(load('WalletPaymentChallengeRequest').WalletPaymentChallengeRequestToJSON({address:'0xabc',chainId:84532}), {address:'0xabc',chain_id:84532});
const payment = load('WalletPaymentUsdcLeasePaymentCreate').WalletPaymentUsdcLeasePaymentCreateToJSON({amountCents:50});
assert.deepEqual(JSON.parse(JSON.stringify(payment)), {amount_cents:50});
assert.deepEqual(load('WalletPaymentSubmitRequest').WalletPaymentSubmitRequestToJSON({message:'m',nonce:'n',signature:'0x1234'}), {message:'m',nonce:'n',signature:'0x1234'});
