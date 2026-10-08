
# UsdcLeasePaymentResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **billingRecordId** | [**java.util.UUID**](java.util.UUID.md) |  |  |
| **status** | **kotlin.String** |  |  |
| **amountCents** | **kotlin.Int** |  |  |
| **amountAtoms** | **kotlin.Int** |  |  |
| **chainId** | **kotlin.Int** | Base chain id from deployment config, when set. |  [optional] |
| **testCreditAvailable** | **kotlin.Boolean** | True only on a Base Sepolia deployment with Stripe in test mode. The renter may then settle this payment from a test-network credit. |  [optional] |



