# ReadSSOSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**provider** | **str** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] [default to []]
**redirect_uris** | **List[str]** |  | [optional] [default to []]
**id** | **str** |  | 

## Example

```python
from openapi_client.models.read_sso_settings_dto import ReadSSOSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReadSSOSettingsDto from a JSON string
read_sso_settings_dto_instance = ReadSSOSettingsDto.from_json(json)
# print the JSON string representation of the object
print(ReadSSOSettingsDto.to_json())

# convert the object into a dict
read_sso_settings_dto_dict = read_sso_settings_dto_instance.to_dict()
# create an instance of ReadSSOSettingsDto from a dict
read_sso_settings_dto_from_dict = ReadSSOSettingsDto.from_dict(read_sso_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


