# Wallet owner clients

The generated Python, TypeScript, Kotlin and Swift clients contain `WalletAuth`
and `WalletPayments` operations from the checked-in owner OpenAPI subsets.
Use an API client pointing at the owning Auth or Payment service origin, or a
verified gateway that forwards those exact paths. The snapshot does not imply
that every gateway currently forwards every owner operation.

The public runtime has no hosted-provider dependency. Existing public crypto
budget clients remain independent. Enterprise quota clients use integer capacity
units; they do not acquire crypto assets, spending authority or redemption rights.

## Payment discovery and observation

```python
from openapi_client import ApiClient, Configuration
from openapi_client.api.wallet_payments_api import WalletPaymentsApi

config = Configuration(host=payment_origin, access_token=current_tenant_session)
with ApiClient(config) as transport:
    payments = WalletPaymentsApi(transport)
    capabilities = payments.get_wallet_payment_capabilities(tenant_id)
    if capabilities.deposit_creation:
        # First create/bind the lease using its owner contract. Reuse the same
        # payment and UUID idempotency key after uncertain creation.
        observed = payments.get_wallet_deposit(billing_record_id, tenant_id)
```

Capability flags report server configuration, not caller permission or provider
availability. A disabled creation flag does not remove observation of an existing
owned payment. HTTP 400/403/404/409/503 remain errors; clients do not infer success,
retry a new payment, or grant quota when a command fails. `settled` is meaningful
only from the authenticated owner response. A wallet signature, redirect or
submitted transaction hash is not payment confirmation.

Deposit observations explicitly identify Base Sepolia (`84532`) and its supported
USDC contract. `amount_cents` is a USD price, not an enterprise unit count or a
new token-amount conversion API. Never infer mainnet from the provider network
label `base`. Production payments are not enabled by this sandbox contract.

## Wallet control and payout scope

Use `WalletAuthApi` with the current Auth credential to request a nonce, sign the
returned message with the wallet, and submit that exact message/signature to bind.
The service validates domain/URI, chain, address, nonce and expiry. It rejects
replay and mismatches; the SDK does not perform signature verification or invent
a challenge. EOA and supported smart-wallet behavior comes from the shared verifier.

Payout-address proofs use separate Payment challenges and require browser tenant
and host-management authority. Never submit an Auth login/binding proof as payout
or spending permission. Refunds remain owner-managed. USDC host enrollment requires
its separate configured provider capability and authorized owner flow; this SDK
adds no arbitrary wallet-send or refund-destination operation.

Owner contract snapshots are under `sdk/openapi/owners`. Their selected methods,
paths and schemas must match the merged snapshot. Generation uses the repository's
pinned generator. Unit contracts exercise wire headers, unchanged message/signature
serialization, disabled capabilities and typed owner failures; scheduled composition
remains in Infra's existing owner and SDK suites.

## Native client qualification

The wallet CI job compiles the complete generated TypeScript and Kotlin REST
source trees, then runs wallet wire contract tests. A separate Swift 6.0.3 job
builds the generated package and runs consumer tests for proof keys, pending
nullable deposits, and rejection of incomplete observations. Test harnesses live
outside generated directories. These checks do not claim mobile application,
gRPC, or complete SDK consumer qualification; those remain SDK #3.
