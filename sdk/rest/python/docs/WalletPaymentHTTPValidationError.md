# WalletPaymentHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[WalletPaymentValidationError]**](WalletPaymentValidationError.md) |  | [optional] 

## Example

```python
from openapi_client.models.wallet_payment_http_validation_error import WalletPaymentHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPaymentHTTPValidationError from a JSON string
wallet_payment_http_validation_error_instance = WalletPaymentHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(WalletPaymentHTTPValidationError.to_json())

# convert the object into a dict
wallet_payment_http_validation_error_dict = wallet_payment_http_validation_error_instance.to_dict()
# create an instance of WalletPaymentHTTPValidationError from a dict
wallet_payment_http_validation_error_from_dict = WalletPaymentHTTPValidationError.from_dict(wallet_payment_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


