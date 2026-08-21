# CreateSSOSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**provider** | **str** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] [default to []]
**redirect_uris** | **List[str]** |  | [optional] [default to []]
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_sso_settings_dto import CreateSSOSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSSOSettingsDto from a JSON string
create_sso_settings_dto_instance = CreateSSOSettingsDto.from_json(json)
# print the JSON string representation of the object
print(CreateSSOSettingsDto.to_json())

# convert the object into a dict
create_sso_settings_dto_dict = create_sso_settings_dto_instance.to_dict()
# create an instance of CreateSSOSettingsDto from a dict
create_sso_settings_dto_from_dict = CreateSSOSettingsDto.from_dict(create_sso_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


