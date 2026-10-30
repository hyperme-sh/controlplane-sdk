# UserProfileImageUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** |  | 

## Example

```python
from openapi_client.models.user_profile_image_update_dto import UserProfileImageUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileImageUpdateDto from a JSON string
user_profile_image_update_dto_instance = UserProfileImageUpdateDto.from_json(json)
# print the JSON string representation of the object
print(UserProfileImageUpdateDto.to_json())

# convert the object into a dict
user_profile_image_update_dto_dict = user_profile_image_update_dto_instance.to_dict()
# create an instance of UserProfileImageUpdateDto from a dict
user_profile_image_update_dto_from_dict = UserProfileImageUpdateDto.from_dict(user_profile_image_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


