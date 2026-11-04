# AIHistoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | 
**query** | **str** |  | 
**response** | **str** |  | 
**timestamp** | **str** |  | 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ai_history_dto import AIHistoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of AIHistoryDto from a JSON string
ai_history_dto_instance = AIHistoryDto.from_json(json)
# print the JSON string representation of the object
print(AIHistoryDto.to_json())

# convert the object into a dict
ai_history_dto_dict = ai_history_dto_instance.to_dict()
# create an instance of AIHistoryDto from a dict
ai_history_dto_from_dict = AIHistoryDto.from_dict(ai_history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


