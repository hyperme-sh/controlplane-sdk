# CryptoBudgetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**owner_pubkey** | **str** |  | 
**mint_pubkey** | **str** |  | 
**ceiling_lamports** | **int** |  | 
**allocated_lamports** | **int** |  | 
**label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.crypto_budget_response import CryptoBudgetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoBudgetResponse from a JSON string
crypto_budget_response_instance = CryptoBudgetResponse.from_json(json)
# print the JSON string representation of the object
print(CryptoBudgetResponse.to_json())

# convert the object into a dict
crypto_budget_response_dict = crypto_budget_response_instance.to_dict()
# create an instance of CryptoBudgetResponse from a dict
crypto_budget_response_from_dict = CryptoBudgetResponse.from_dict(crypto_budget_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


