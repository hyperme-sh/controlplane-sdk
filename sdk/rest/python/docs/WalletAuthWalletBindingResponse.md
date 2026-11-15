# WalletAuthWalletBindingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound** | **bool** |  | [optional] [default to True]
**email** | **str** |  | [optional] 
**keycloak_sub** | **str** |  | 
**wallet_address** | **str** |  | 

## Example

```python
from openapi_client.models.wallet_auth_wallet_binding_response import WalletAuthWalletBindingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAuthWalletBindingResponse from a JSON string
wallet_auth_wallet_binding_response_instance = WalletAuthWalletBindingResponse.from_json(json)
# print the JSON string representation of the object
print(WalletAuthWalletBindingResponse.to_json())

# convert the object into a dict
wallet_auth_wallet_binding_response_dict = wallet_auth_wallet_binding_response_instance.to_dict()
# create an instance of WalletAuthWalletBindingResponse from a dict
wallet_auth_wallet_binding_response_from_dict = WalletAuthWalletBindingResponse.from_dict(wallet_auth_wallet_binding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


