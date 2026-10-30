# AvailableStorageProviderDto


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
**id** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.available_storage_provider_dto import AvailableStorageProviderDto

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableStorageProviderDto from a JSON string
available_storage_provider_dto_instance = AvailableStorageProviderDto.from_json(json)
# print the JSON string representation of the object
print(AvailableStorageProviderDto.to_json())

# convert the object into a dict
available_storage_provider_dto_dict = available_storage_provider_dto_instance.to_dict()
# create an instance of AvailableStorageProviderDto from a dict
available_storage_provider_dto_from_dict = AvailableStorageProviderDto.from_dict(available_storage_provider_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


