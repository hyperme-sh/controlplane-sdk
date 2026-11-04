# AISessionByUserIdDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**session_id** | **str** |  | 
**created_at** | **str** |  | 
**history_id** | **str** |  | 
**tenant_id** | **str** |  | [optional] 
**user_id** | **str** |  | 
**sessions** | [**List[AIHistoriesDto]**](AIHistoriesDto.md) |  | 

## Example

```python
from openapi_client.models.ai_session_by_user_id_dto import AISessionByUserIdDto

# TODO update the JSON string below
json = "{}"
# create an instance of AISessionByUserIdDto from a JSON string
ai_session_by_user_id_dto_instance = AISessionByUserIdDto.from_json(json)
# print the JSON string representation of the object
print(AISessionByUserIdDto.to_json())

# convert the object into a dict
ai_session_by_user_id_dto_dict = ai_session_by_user_id_dto_instance.to_dict()
# create an instance of AISessionByUserIdDto from a dict
ai_session_by_user_id_dto_from_dict = AISessionByUserIdDto.from_dict(ai_session_by_user_id_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


