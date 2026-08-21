# StorageSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**is_enabled** | **bool** |  | 
**region** | **str** |  | 
**aws_access_key** | **str** |  | [optional] 
**aws_secret_key** | **str** |  | [optional] 
**aws_bucket_name** | **str** |  | [optional] 
**azure_connection_string** | **str** |  | [optional] 
**azure_container_name** | **str** |  | [optional] 
**updated_by_user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.storage_settings_dto import StorageSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StorageSettingsDto from a JSON string
storage_settings_dto_instance = StorageSettingsDto.from_json(json)
# print the JSON string representation of the object
print(StorageSettingsDto.to_json())

# convert the object into a dict
storage_settings_dto_dict = storage_settings_dto_instance.to_dict()
# create an instance of StorageSettingsDto from a dict
storage_settings_dto_from_dict = StorageSettingsDto.from_dict(storage_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


