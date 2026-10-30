# RecoverySessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**state** | **str** |  | 
**expires_at** | **str** |  | 

## Example

```python
from openapi_client.models.recovery_session_response import RecoverySessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverySessionResponse from a JSON string
recovery_session_response_instance = RecoverySessionResponse.from_json(json)
# print the JSON string representation of the object
print(RecoverySessionResponse.to_json())

# convert the object into a dict
recovery_session_response_dict = recovery_session_response_instance.to_dict()
# create an instance of RecoverySessionResponse from a dict
recovery_session_response_from_dict = RecoverySessionResponse.from_dict(recovery_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


