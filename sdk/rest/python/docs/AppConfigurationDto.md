# AppConfigurationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_multi_tenant_enabled** | **bool** |  | 
**multi_tenancy_strategy** | **str** |  | 
**host_main_domain** | **str** |  | 
**is_user_logged_in** | **bool** |  | [optional] [default to False]
**user_preferences** | [**UserPreferenceDto**](UserPreferenceDto.md) |  | [optional] 
**current_tenant** | [**TenantDto**](TenantDto.md) |  | [optional] 
**environment** | **str** |  | 
**enabled_sso_providers** | **List[str]** |  | [optional] 
**branding** | [**BrandingDto**](BrandingDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_configuration_dto import AppConfigurationDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppConfigurationDto from a JSON string
app_configuration_dto_instance = AppConfigurationDto.from_json(json)
# print the JSON string representation of the object
print(AppConfigurationDto.to_json())

# convert the object into a dict
app_configuration_dto_dict = app_configuration_dto_instance.to_dict()
# create an instance of AppConfigurationDto from a dict
app_configuration_dto_from_dict = AppConfigurationDto.from_dict(app_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


