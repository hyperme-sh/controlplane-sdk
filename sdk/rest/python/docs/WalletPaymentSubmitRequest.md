# WalletPaymentSubmitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**nonce** | **str** |  | 
**signature** | **str** |  | 

## Example

```python
from openapi_client.models.wallet_payment_submit_request import WalletPaymentSubmitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPaymentSubmitRequest from a JSON string
wallet_payment_submit_request_instance = WalletPaymentSubmitRequest.from_json(json)
# print the JSON string representation of the object
print(WalletPaymentSubmitRequest.to_json())

# convert the object into a dict
wallet_payment_submit_request_dict = wallet_payment_submit_request_instance.to_dict()
# create an instance of WalletPaymentSubmitRequest from a dict
wallet_payment_submit_request_from_dict = WalletPaymentSubmitRequest.from_dict(wallet_payment_submit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


