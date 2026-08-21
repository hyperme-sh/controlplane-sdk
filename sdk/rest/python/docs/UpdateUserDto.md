# UpdateUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**gender** | [**Gender**](Gender.md) |  | [optional] 
**image_url** | **str** |  | [optional] 
**role_id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**activated_at** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**sso_provider_id** | **str** |  | [optional] 
**keycloak_sub** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_user_dto import UpdateUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserDto from a JSON string
update_user_dto_instance = UpdateUserDto.from_json(json)
# print the JSON string representation of the object
print(UpdateUserDto.to_json())

# convert the object into a dict
update_user_dto_dict = update_user_dto_instance.to_dict()
# create an instance of UpdateUserDto from a dict
update_user_dto_from_dict = UpdateUserDto.from_dict(update_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


