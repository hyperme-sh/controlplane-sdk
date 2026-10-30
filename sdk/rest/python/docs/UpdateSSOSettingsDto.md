# UpdateSSOSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**provider** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.update_sso_settings_dto import UpdateSSOSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSSOSettingsDto from a JSON string
update_sso_settings_dto_instance = UpdateSSOSettingsDto.from_json(json)
# print the JSON string representation of the object
print(UpdateSSOSettingsDto.to_json())

# convert the object into a dict
update_sso_settings_dto_dict = update_sso_settings_dto_instance.to_dict()
# create an instance of UpdateSSOSettingsDto from a dict
update_sso_settings_dto_from_dict = UpdateSSOSettingsDto.from_dict(update_sso_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


