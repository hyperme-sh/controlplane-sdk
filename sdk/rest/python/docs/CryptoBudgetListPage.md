# CryptoBudgetListPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CryptoBudgetResponse]**](CryptoBudgetResponse.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from openapi_client.models.crypto_budget_list_page import CryptoBudgetListPage

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoBudgetListPage from a JSON string
crypto_budget_list_page_instance = CryptoBudgetListPage.from_json(json)
# print the JSON string representation of the object
print(CryptoBudgetListPage.to_json())

# convert the object into a dict
crypto_budget_list_page_dict = crypto_budget_list_page_instance.to_dict()
# create an instance of CryptoBudgetListPage from a dict
crypto_budget_list_page_from_dict = CryptoBudgetListPage.from_dict(crypto_budget_list_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


