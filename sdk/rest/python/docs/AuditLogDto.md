# AuditLogDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** |  | 
**action** | **str** |  | 
**changes** | **Dict[str, object]** |  | [optional] 
**user_id** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] [default to '2026-03-31T19:38:43.792086']
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.audit_log_dto import AuditLogDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogDto from a JSON string
audit_log_dto_instance = AuditLogDto.from_json(json)
# print the JSON string representation of the object
print(AuditLogDto.to_json())

# convert the object into a dict
audit_log_dto_dict = audit_log_dto_instance.to_dict()
# create an instance of AuditLogDto from a dict
audit_log_dto_from_dict = AuditLogDto.from_dict(audit_log_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


