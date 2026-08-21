# RoleListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[RoleDto]**](RoleDto.md) |  | 
**skip** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**has_previous** | **bool** |  | 
**has_next** | **bool** |  | 

## Example

```python
from openapi_client.models.role_list_dto import RoleListDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleListDto from a JSON string
role_list_dto_instance = RoleListDto.from_json(json)
# print the JSON string representation of the object
print(RoleListDto.to_json())

# convert the object into a dict
role_list_dto_dict = role_list_dto_instance.to_dict()
# create an instance of RoleListDto from a dict
role_list_dto_from_dict = RoleListDto.from_dict(role_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


