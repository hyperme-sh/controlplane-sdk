# SSOSettingsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReadSSOSettingsDto]**](ReadSSOSettingsDto.md) |  | 

## Example

```python
from openapi_client.models.sso_settings_list_dto import SSOSettingsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of SSOSettingsListDto from a JSON string
sso_settings_list_dto_instance = SSOSettingsListDto.from_json(json)
# print the JSON string representation of the object
print(SSOSettingsListDto.to_json())

# convert the object into a dict
sso_settings_list_dto_dict = sso_settings_list_dto_instance.to_dict()
# create an instance of SSOSettingsListDto from a dict
sso_settings_list_dto_from_dict = SSOSettingsListDto.from_dict(sso_settings_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


