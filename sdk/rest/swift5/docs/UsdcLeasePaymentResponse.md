# UsdcLeasePaymentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingRecordId** | **UUID** |  | 
**status** | **String** |  | 
**amountCents** | **Int** |  | 
**amountAtoms** | **Int** |  | 
**chainId** | **Int** | Base chain id from deployment config, when set. | [optional] 
**testCreditAvailable** | **Bool** | True only where PAYMENTS_USDC_TEST_CREDIT_ENABLED is set and the deployment is Base Sepolia with Stripe in test mode. The renter may then settle this payment from a test-network credit. | [optional] [default to false]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


