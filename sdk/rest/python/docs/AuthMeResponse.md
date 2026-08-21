# AuthMeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **str** |  | 
**email** | **str** |  | [optional] 
**preferred_username** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.auth_me_response import AuthMeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMeResponse from a JSON string
auth_me_response_instance = AuthMeResponse.from_json(json)
# print the JSON string representation of the object
print(AuthMeResponse.to_json())

# convert the object into a dict
auth_me_response_dict = auth_me_response_instance.to_dict()
# create an instance of AuthMeResponse from a dict
auth_me_response_from_dict = AuthMeResponse.from_dict(auth_me_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


