# AIHistoriesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**histories** | [**List[AIHistoryDto]**](AIHistoryDto.md) |  | 

## Example

```python
from openapi_client.models.ai_histories_dto import AIHistoriesDto

# TODO update the JSON string below
json = "{}"
# create an instance of AIHistoriesDto from a JSON string
ai_histories_dto_instance = AIHistoriesDto.from_json(json)
# print the JSON string representation of the object
print(AIHistoriesDto.to_json())

# convert the object into a dict
ai_histories_dto_dict = ai_histories_dto_instance.to_dict()
# create an instance of AIHistoriesDto from a dict
ai_histories_dto_from_dict = AIHistoriesDto.from_dict(ai_histories_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


