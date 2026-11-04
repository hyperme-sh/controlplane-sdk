# TenantListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[TenantDto]**](TenantDto.md) |  | 
**skip** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**has_previous** | **bool** |  | 
**has_next** | **bool** |  | 

## Example

```python
from openapi_client.models.tenant_list_dto import TenantListDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantListDto from a JSON string
tenant_list_dto_instance = TenantListDto.from_json(json)
# print the JSON string representation of the object
print(TenantListDto.to_json())

# convert the object into a dict
tenant_list_dto_dict = tenant_list_dto_instance.to_dict()
# create an instance of TenantListDto from a dict
tenant_list_dto_from_dict = TenantListDto.from_dict(tenant_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


