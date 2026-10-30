# CreateRoleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_role_dto import CreateRoleDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleDto from a JSON string
create_role_dto_instance = CreateRoleDto.from_json(json)
# print the JSON string representation of the object
print(CreateRoleDto.to_json())

# convert the object into a dict
create_role_dto_dict = create_role_dto_instance.to_dict()
# create an instance of CreateRoleDto from a dict
create_role_dto_from_dict = CreateRoleDto.from_dict(create_role_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


