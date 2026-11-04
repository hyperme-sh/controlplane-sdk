# RecoverySessionCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotency_key** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.recovery_session_create import RecoverySessionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverySessionCreate from a JSON string
recovery_session_create_instance = RecoverySessionCreate.from_json(json)
# print the JSON string representation of the object
print(RecoverySessionCreate.to_json())

# convert the object into a dict
recovery_session_create_dict = recovery_session_create_instance.to_dict()
# create an instance of RecoverySessionCreate from a dict
recovery_session_create_from_dict = RecoverySessionCreate.from_dict(recovery_session_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


