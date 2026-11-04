# DownloadAuditRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**total_records** | **int** |  | 

## Example

```python
from openapi_client.models.download_audit_request_dto import DownloadAuditRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadAuditRequestDto from a JSON string
download_audit_request_dto_instance = DownloadAuditRequestDto.from_json(json)
# print the JSON string representation of the object
print(DownloadAuditRequestDto.to_json())

# convert the object into a dict
download_audit_request_dto_dict = download_audit_request_dto_instance.to_dict()
# create an instance of DownloadAuditRequestDto from a dict
download_audit_request_dto_from_dict = DownloadAuditRequestDto.from_dict(download_audit_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


