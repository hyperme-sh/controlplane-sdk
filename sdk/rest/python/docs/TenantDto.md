# TenantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**subdomain** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to False]
**custom_domain** | **str** |  | [optional] 
**custom_domain_status** | **str** |  | [optional] [default to 'failed']
**features** | [**List[FeatureDto]**](FeatureDto.md) |  | [optional] [default to []]
**subscription_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_dto import TenantDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDto from a JSON string
tenant_dto_instance = TenantDto.from_json(json)
# print the JSON string representation of the object
print(TenantDto.to_json())

# convert the object into a dict
tenant_dto_dict = tenant_dto_instance.to_dict()
# create an instance of TenantDto from a dict
tenant_dto_from_dict = TenantDto.from_dict(tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


