# WalletPaymentWalletCheckoutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_record_id** | **str** |  | 
**checkout_url** | **str** |  | 

## Example

```python
from openapi_client.models.wallet_payment_wallet_checkout_response import WalletPaymentWalletCheckoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPaymentWalletCheckoutResponse from a JSON string
wallet_payment_wallet_checkout_response_instance = WalletPaymentWalletCheckoutResponse.from_json(json)
# print the JSON string representation of the object
print(WalletPaymentWalletCheckoutResponse.to_json())

# convert the object into a dict
wallet_payment_wallet_checkout_response_dict = wallet_payment_wallet_checkout_response_instance.to_dict()
# create an instance of WalletPaymentWalletCheckoutResponse from a dict
wallet_payment_wallet_checkout_response_from_dict = WalletPaymentWalletCheckoutResponse.from_dict(wallet_payment_wallet_checkout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


