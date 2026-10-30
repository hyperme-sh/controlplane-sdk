# CryptoBudgetCreateRequest

Create an in-app Solana-style budget envelope (pubkeys only; no private keys stored).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ceiling_lamports** | **int** |  | 
**mint_pubkey** | **str** |  | 
**label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.crypto_budget_create_request import CryptoBudgetCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoBudgetCreateRequest from a JSON string
crypto_budget_create_request_instance = CryptoBudgetCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CryptoBudgetCreateRequest.to_json())

# convert the object into a dict
crypto_budget_create_request_dict = crypto_budget_create_request_instance.to_dict()
# create an instance of CryptoBudgetCreateRequest from a dict
crypto_budget_create_request_from_dict = CryptoBudgetCreateRequest.from_dict(crypto_budget_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


