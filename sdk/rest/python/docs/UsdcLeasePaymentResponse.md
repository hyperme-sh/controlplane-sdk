# UsdcLeasePaymentResponse

A USDC lease payment. ``amount_atoms`` has 6 decimals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_record_id** | **str** |  | 
**status** | **str** |  | 
**amount_cents** | **int** |  | 
**amount_atoms** | **int** | USDC atoms (6 decimals). 64-bit: large payments exceed 32 bits. | 
**chain_id** | **int** | Base chain id from deployment config, when set. | [optional] 
**test_credit_available** | **bool** | True only where PAYMENTS_USDC_TEST_CREDIT_ENABLED is set and the deployment is Base Sepolia with Stripe in test mode. The renter may then settle this payment from a test-network credit. | [optional] [default to False]

## Example

```python
from openapi_client.models.usdc_lease_payment_response import UsdcLeasePaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsdcLeasePaymentResponse from a JSON string
usdc_lease_payment_response_instance = UsdcLeasePaymentResponse.from_json(json)
# print the JSON string representation of the object
print(UsdcLeasePaymentResponse.to_json())

# convert the object into a dict
usdc_lease_payment_response_dict = usdc_lease_payment_response_instance.to_dict()
# create an instance of UsdcLeasePaymentResponse from a dict
usdc_lease_payment_response_from_dict = UsdcLeasePaymentResponse.from_dict(usdc_lease_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


