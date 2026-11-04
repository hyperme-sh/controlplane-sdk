# CreateTenantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**subdomain** | **str** |  | 
**admin_email** | **str** |  | 
**admin_password** | **str** |  | [optional] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**gender** | [**Gender**](Gender.md) |  | 

## Example

```python
from openapi_client.models.create_tenant_dto import CreateTenantDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantDto from a JSON string
create_tenant_dto_instance = CreateTenantDto.from_json(json)
# print the JSON string representation of the object
print(CreateTenantDto.to_json())

# convert the object into a dict
create_tenant_dto_dict = create_tenant_dto_instance.to_dict()
# create an instance of CreateTenantDto from a dict
create_tenant_dto_from_dict = CreateTenantDto.from_dict(create_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


