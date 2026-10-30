
# InferenceRequest

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **prompt** | **kotlin.String** |  |  |
| **model** | **kotlin.String** |  |  |
| **maxTokens** | **kotlin.Int** |  |  [optional] |
| **billingMode** | [**inline**](#BillingMode) |  |  [optional] |
| **budgetId** | [**java.util.UUID**](java.util.UUID.md) | Crypto agent budget (payment-service); required when billing_mode is crypto. |  [optional] |
| **stripeCustomerId** | **kotlin.String** | Optional Stripe customer id for metered usage events. |  [optional] |


<a id="BillingMode"></a>
## Enum: billing_mode
| Name | Value |
| ---- | ----- |
| billingMode | none, crypto, stripe |



