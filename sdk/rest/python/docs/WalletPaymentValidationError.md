# WalletPaymentValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[ValidationErrorLocInner]**](ValidationErrorLocInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 
**input** | **object** |  | [optional] 
**ctx** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.wallet_payment_validation_error import WalletPaymentValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPaymentValidationError from a JSON string
wallet_payment_validation_error_instance = WalletPaymentValidationError.from_json(json)
# print the JSON string representation of the object
print(WalletPaymentValidationError.to_json())

# convert the object into a dict
wallet_payment_validation_error_dict = wallet_payment_validation_error_instance.to_dict()
# create an instance of WalletPaymentValidationError from a dict
wallet_payment_validation_error_from_dict = WalletPaymentValidationError.from_dict(wallet_payment_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


