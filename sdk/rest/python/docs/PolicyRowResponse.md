# PolicyRowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**ptype** | **str** |  | 
**v0** | **str** |  | 
**v1** | **str** |  | 
**v2** | **str** |  | 
**v3** | **str** |  | 
**v4** | **str** |  | 
**v5** | **str** |  | 

## Example

```python
from openapi_client.models.policy_row_response import PolicyRowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRowResponse from a JSON string
policy_row_response_instance = PolicyRowResponse.from_json(json)
# print the JSON string representation of the object
print(PolicyRowResponse.to_json())

# convert the object into a dict
policy_row_response_dict = policy_row_response_instance.to_dict()
# create an instance of PolicyRowResponse from a dict
policy_row_response_from_dict = PolicyRowResponse.from_dict(policy_row_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


