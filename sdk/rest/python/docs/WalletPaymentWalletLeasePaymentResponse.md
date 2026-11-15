# WalletPaymentWalletLeasePaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** |  | 
**billing_record_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.wallet_payment_wallet_lease_payment_response import WalletPaymentWalletLeasePaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPaymentWalletLeasePaymentResponse from a JSON string
wallet_payment_wallet_lease_payment_response_instance = WalletPaymentWalletLeasePaymentResponse.from_json(json)
# print the JSON string representation of the object
print(WalletPaymentWalletLeasePaymentResponse.to_json())

# convert the object into a dict
wallet_payment_wallet_lease_payment_response_dict = wallet_payment_wallet_lease_payment_response_instance.to_dict()
# create an instance of WalletPaymentWalletLeasePaymentResponse from a dict
wallet_payment_wallet_lease_payment_response_from_dict = WalletPaymentWalletLeasePaymentResponse.from_dict(wallet_payment_wallet_lease_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


