# UpdateRoleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_role_dto import UpdateRoleDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoleDto from a JSON string
update_role_dto_instance = UpdateRoleDto.from_json(json)
# print the JSON string representation of the object
print(UpdateRoleDto.to_json())

# convert the object into a dict
update_role_dto_dict = update_role_dto_instance.to_dict()
# create an instance of UpdateRoleDto from a dict
update_role_dto_from_dict = UpdateRoleDto.from_dict(update_role_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


