# WalletAuthValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctx** | **object** |  | [optional] 
**input** | **object** |  | [optional] 
**loc** | [**List[ValidationErrorLocInner]**](ValidationErrorLocInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.wallet_auth_validation_error import WalletAuthValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAuthValidationError from a JSON string
wallet_auth_validation_error_instance = WalletAuthValidationError.from_json(json)
# print the JSON string representation of the object
print(WalletAuthValidationError.to_json())

# convert the object into a dict
wallet_auth_validation_error_dict = wallet_auth_validation_error_instance.to_dict()
# create an instance of WalletAuthValidationError from a dict
wallet_auth_validation_error_from_dict = WalletAuthValidationError.from_dict(wallet_auth_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


