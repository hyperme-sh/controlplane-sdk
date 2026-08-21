
# AuditLogDto

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **entity** | **kotlin.String** |  |  |
| **action** | [**inline**](#Action) |  |  |
| **changes** | [**kotlin.collections.Map&lt;kotlin.String, kotlin.Any&gt;**](kotlin.Any.md) |  |  [optional] |
| **userId** | **kotlin.String** |  |  [optional] |
| **timestamp** | **kotlin.String** |  |  [optional] |
| **tenantId** | **kotlin.String** |  |  [optional] |


<a id="Action"></a>
## Enum: action
| Name | Value |
| ---- | ----- |
| action | create, update, delete, read, login, logout, error, download |



