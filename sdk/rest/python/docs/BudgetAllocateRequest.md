# BudgetAllocateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta_lamports** | **int** |  | 

## Example

```python
from openapi_client.models.budget_allocate_request import BudgetAllocateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetAllocateRequest from a JSON string
budget_allocate_request_instance = BudgetAllocateRequest.from_json(json)
# print the JSON string representation of the object
print(BudgetAllocateRequest.to_json())

# convert the object into a dict
budget_allocate_request_dict = budget_allocate_request_instance.to_dict()
# create an instance of BudgetAllocateRequest from a dict
budget_allocate_request_from_dict = BudgetAllocateRequest.from_dict(budget_allocate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


