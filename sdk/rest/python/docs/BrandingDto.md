# BrandingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**logo_type** | **str** |  | [optional] 
**contact_info** | [**ContactInfo**](ContactInfo.md) |  | [optional] 
**theme_config** | [**ThemeConfig**](ThemeConfig.md) |  | [optional] 
**tenant_id** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**app_name** | **str** |  | [optional] [default to 'SaaS Org']
**favicon_url** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.branding_dto import BrandingDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingDto from a JSON string
branding_dto_instance = BrandingDto.from_json(json)
# print the JSON string representation of the object
print(BrandingDto.to_json())

# convert the object into a dict
branding_dto_dict = branding_dto_instance.to_dict()
# create an instance of BrandingDto from a dict
branding_dto_from_dict = BrandingDto.from_dict(branding_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


