# UserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**gender** | [**Gender**](Gender.md) |  | 
**role_id** | **str** |  | [optional] 
**is_active** | **bool** |  | 
**activated_at** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**tenant_id** | **str** |  | [optional] 
**sso_provider_id** | **str** |  | [optional] 
**keycloak_sub** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_dto import UserDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserDto from a JSON string
user_dto_instance = UserDto.from_json(json)
# print the JSON string representation of the object
print(UserDto.to_json())

# convert the object into a dict
user_dto_dict = user_dto_instance.to_dict()
# create an instance of UserDto from a dict
user_dto_from_dict = UserDto.from_dict(user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


