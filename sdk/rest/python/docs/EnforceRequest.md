# EnforceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] [default to 'rbac']
**sub** | **str** |  | 
**obj** | **str** |  | 
**act** | **str** |  | 
**extra** | **str** | 4th request field for ABAC model (e.g. political_view category) | [optional] 

## Example

```python
from openapi_client.models.enforce_request import EnforceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnforceRequest from a JSON string
enforce_request_instance = EnforceRequest.from_json(json)
# print the JSON string representation of the object
print(EnforceRequest.to_json())

# convert the object into a dict
enforce_request_dict = enforce_request_instance.to_dict()
# create an instance of EnforceRequest from a dict
enforce_request_from_dict = EnforceRequest.from_dict(enforce_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


