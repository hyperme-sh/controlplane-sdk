# SSOSettingsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from openapi_client.models.sso_settings_response_dto import SSOSettingsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SSOSettingsResponseDto from a JSON string
sso_settings_response_dto_instance = SSOSettingsResponseDto.from_json(json)
# print the JSON string representation of the object
print(SSOSettingsResponseDto.to_json())

# convert the object into a dict
sso_settings_response_dto_dict = sso_settings_response_dto_instance.to_dict()
# create an instance of SSOSettingsResponseDto from a dict
sso_settings_response_dto_from_dict = SSOSettingsResponseDto.from_dict(sso_settings_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


