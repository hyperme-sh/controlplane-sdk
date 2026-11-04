# InternalValidateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** |  | 
**key_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.internal_validate_response import InternalValidateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalValidateResponse from a JSON string
internal_validate_response_instance = InternalValidateResponse.from_json(json)
# print the JSON string representation of the object
print(InternalValidateResponse.to_json())

# convert the object into a dict
internal_validate_response_dict = internal_validate_response_instance.to_dict()
# create an instance of InternalValidateResponse from a dict
internal_validate_response_from_dict = InternalValidateResponse.from_dict(internal_validate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


