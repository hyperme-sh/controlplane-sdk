# InternalValidateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | key_prefix.secret | 
**tenant_id** | **str** |  | 

## Example

```python
from openapi_client.models.internal_validate_request import InternalValidateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalValidateRequest from a JSON string
internal_validate_request_instance = InternalValidateRequest.from_json(json)
# print the JSON string representation of the object
print(InternalValidateRequest.to_json())

# convert the object into a dict
internal_validate_request_dict = internal_validate_request_instance.to_dict()
# create an instance of InternalValidateRequest from a dict
internal_validate_request_from_dict = InternalValidateRequest.from_dict(internal_validate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


