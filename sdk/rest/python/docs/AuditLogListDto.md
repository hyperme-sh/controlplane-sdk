# AuditLogListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**logs** | [**List[AuditLogDto]**](AuditLogDto.md) |  | 
**has_next** | **bool** |  | 
**has_previous** | **bool** |  | 
**limit** | **int** |  | 
**skip** | **int** |  | 

## Example

```python
from openapi_client.models.audit_log_list_dto import AuditLogListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogListDto from a JSON string
audit_log_list_dto_instance = AuditLogListDto.from_json(json)
# print the JSON string representation of the object
print(AuditLogListDto.to_json())

# convert the object into a dict
audit_log_list_dto_dict = audit_log_list_dto_instance.to_dict()
# create an instance of AuditLogListDto from a dict
audit_log_list_dto_from_dict = AuditLogListDto.from_dict(audit_log_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


