# AIAskRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | 
**model_name** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ai_ask_request_dto import AIAskRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AIAskRequestDto from a JSON string
ai_ask_request_dto_instance = AIAskRequestDto.from_json(json)
# print the JSON string representation of the object
print(AIAskRequestDto.to_json())

# convert the object into a dict
ai_ask_request_dto_dict = ai_ask_request_dto_instance.to_dict()
# create an instance of AIAskRequestDto from a dict
ai_ask_request_dto_from_dict = AIAskRequestDto.from_dict(ai_ask_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


