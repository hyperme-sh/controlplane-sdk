# InferenceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **String** |  | 
**model** | **String** |  | 
**maxTokens** | **Int** |  | [optional] 
**billingMode** | **String** |  | [optional] [default to ._none]
**budgetId** | **UUID** | Crypto agent budget (payment-service); required when billing_mode is crypto. | [optional] 
**stripeCustomerId** | **String** | Optional Stripe customer id for metered usage events. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


