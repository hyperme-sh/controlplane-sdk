# UserRoleUpdateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** |  | 

## Example

```python
from openapi_client.models.user_role_update_request_dto import UserRoleUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleUpdateRequestDto from a JSON string
user_role_update_request_dto_instance = UserRoleUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print(UserRoleUpdateRequestDto.to_json())

# convert the object into a dict
user_role_update_request_dto_dict = user_role_update_request_dto_instance.to_dict()
# create an instance of UserRoleUpdateRequestDto from a dict
user_role_update_request_dto_from_dict = UserRoleUpdateRequestDto.from_dict(user_role_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


