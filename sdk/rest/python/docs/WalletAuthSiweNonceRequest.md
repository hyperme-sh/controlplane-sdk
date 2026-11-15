# WalletAuthSiweNonceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | EIP-55 or hex wallet the identified person will sign. | 
**chain_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.wallet_auth_siwe_nonce_request import WalletAuthSiweNonceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAuthSiweNonceRequest from a JSON string
wallet_auth_siwe_nonce_request_instance = WalletAuthSiweNonceRequest.from_json(json)
# print the JSON string representation of the object
print(WalletAuthSiweNonceRequest.to_json())

# convert the object into a dict
wallet_auth_siwe_nonce_request_dict = wallet_auth_siwe_nonce_request_instance.to_dict()
# create an instance of WalletAuthSiweNonceRequest from a dict
wallet_auth_siwe_nonce_request_from_dict = WalletAuthSiweNonceRequest.from_dict(wallet_auth_siwe_nonce_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


