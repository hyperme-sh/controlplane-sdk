# WalletAuthSiweBindRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | EIP-4361 SIWE message. Signature is verified, not stored. | 
**signature** | **str** | personal_sign of message. Never persisted. | 

## Example

```python
from openapi_client.models.wallet_auth_siwe_bind_request import WalletAuthSiweBindRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAuthSiweBindRequest from a JSON string
wallet_auth_siwe_bind_request_instance = WalletAuthSiweBindRequest.from_json(json)
# print the JSON string representation of the object
print(WalletAuthSiweBindRequest.to_json())

# convert the object into a dict
wallet_auth_siwe_bind_request_dict = wallet_auth_siwe_bind_request_instance.to_dict()
# create an instance of WalletAuthSiweBindRequest from a dict
wallet_auth_siwe_bind_request_from_dict = WalletAuthSiweBindRequest.from_dict(wallet_auth_siwe_bind_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


