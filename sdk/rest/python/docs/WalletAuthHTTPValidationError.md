# WalletAuthHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[WalletAuthValidationError]**](WalletAuthValidationError.md) |  | [optional] 

## Example

```python
from openapi_client.models.wallet_auth_http_validation_error import WalletAuthHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAuthHTTPValidationError from a JSON string
wallet_auth_http_validation_error_instance = WalletAuthHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(WalletAuthHTTPValidationError.to_json())

# convert the object into a dict
wallet_auth_http_validation_error_dict = wallet_auth_http_validation_error_instance.to_dict()
# create an instance of WalletAuthHTTPValidationError from a dict
wallet_auth_http_validation_error_from_dict = WalletAuthHTTPValidationError.from_dict(wallet_auth_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


