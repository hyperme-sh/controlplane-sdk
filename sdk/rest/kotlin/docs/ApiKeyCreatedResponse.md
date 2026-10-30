
# ApiKeyCreatedResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | [**java.util.UUID**](java.util.UUID.md) |  |  |
| **tenantId** | [**java.util.UUID**](java.util.UUID.md) |  |  |
| **keyPrefix** | **kotlin.String** |  |  |
| **name** | **kotlin.String** |  |  |
| **scopes** | **kotlin.collections.List&lt;kotlin.String&gt;** |  |  |
| **createdAt** | **kotlin.String** |  |  |
| **secretPlaintext** | **kotlin.String** | Full key prefix.secret — store securely; never shown again. |  |
| **apiKey** | **kotlin.String** | Alias for prefix.secret |  |
| **revokedAt** | **kotlin.String** |  |  [optional] |



