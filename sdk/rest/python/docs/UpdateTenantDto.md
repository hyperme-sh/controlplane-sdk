# UpdateTenantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional] 
**custom_domain** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**custom_domain_status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_tenant_dto import UpdateTenantDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantDto from a JSON string
update_tenant_dto_instance = UpdateTenantDto.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantDto.to_json())

# convert the object into a dict
update_tenant_dto_dict = update_tenant_dto_instance.to_dict()
# create an instance of UpdateTenantDto from a dict
update_tenant_dto_from_dict = UpdateTenantDto.from_dict(update_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


