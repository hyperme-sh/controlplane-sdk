# UpdateBrandingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**IdentityDto**](IdentityDto.md) |  | [optional] 
**contact_info** | [**ContactInfo**](ContactInfo.md) |  | [optional] 
**theme_config** | [**ThemeConfig**](ThemeConfig.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**logo_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_branding_dto import UpdateBrandingDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBrandingDto from a JSON string
update_branding_dto_instance = UpdateBrandingDto.from_json(json)
# print the JSON string representation of the object
print(UpdateBrandingDto.to_json())

# convert the object into a dict
update_branding_dto_dict = update_branding_dto_instance.to_dict()
# create an instance of UpdateBrandingDto from a dict
update_branding_dto_from_dict = UpdateBrandingDto.from_dict(update_branding_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


