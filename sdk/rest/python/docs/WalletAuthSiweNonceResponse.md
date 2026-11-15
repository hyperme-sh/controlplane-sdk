# WalletAuthSiweNonceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **int** |  | 
**domain** | **str** |  | 
**issued_at** | **str** |  | 
**message** | **str** |  | 
**nonce** | **str** |  | 
**statement** | **str** |  | 
**uri** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from openapi_client.models.wallet_auth_siwe_nonce_response import WalletAuthSiweNonceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAuthSiweNonceResponse from a JSON string
wallet_auth_siwe_nonce_response_instance = WalletAuthSiweNonceResponse.from_json(json)
# print the JSON string representation of the object
print(WalletAuthSiweNonceResponse.to_json())

# convert the object into a dict
wallet_auth_siwe_nonce_response_dict = wallet_auth_siwe_nonce_response_instance.to_dict()
# create an instance of WalletAuthSiweNonceResponse from a dict
wallet_auth_siwe_nonce_response_from_dict = WalletAuthSiweNonceResponse.from_dict(wallet_auth_siwe_nonce_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


