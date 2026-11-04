# AIModelInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**digest** | **str** |  | 
**size** | **str** |  | 
**created** | **str** |  | 

## Example

```python
from openapi_client.models.ai_model_info_dto import AIModelInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of AIModelInfoDto from a JSON string
ai_model_info_dto_instance = AIModelInfoDto.from_json(json)
# print the JSON string representation of the object
print(AIModelInfoDto.to_json())

# convert the object into a dict
ai_model_info_dto_dict = ai_model_info_dto_instance.to_dict()
# create an instance of AIModelInfoDto from a dict
ai_model_info_dto_from_dict = AIModelInfoDto.from_dict(ai_model_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


