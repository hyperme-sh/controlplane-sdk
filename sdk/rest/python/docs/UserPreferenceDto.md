# UserPreferenceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**preferences** | **Dict[str, object]** |  | 

## Example

```python
from openapi_client.models.user_preference_dto import UserPreferenceDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserPreferenceDto from a JSON string
user_preference_dto_instance = UserPreferenceDto.from_json(json)
# print the JSON string representation of the object
print(UserPreferenceDto.to_json())

# convert the object into a dict
user_preference_dto_dict = user_preference_dto_instance.to_dict()
# create an instance of UserPreferenceDto from a dict
user_preference_dto_from_dict = UserPreferenceDto.from_dict(user_preference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


