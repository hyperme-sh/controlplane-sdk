# ManageSecurityApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteRegisteredPasskeyApiV1SecurityPasskeysCredentialIdDelete**](ManageSecurityApi.md#deleteRegisteredPasskeyApiV1SecurityPasskeysCredentialIdDelete) | **DELETE** api/v1/security/passkeys/{credential_id} | Delete Registered Passkey |
| [**getRegisteredPasskeysApiV1SecurityPasskeysGet**](ManageSecurityApi.md#getRegisteredPasskeysApiV1SecurityPasskeysGet) | **GET** api/v1/security/passkeys | Get Registered Passkeys |



Delete Registered Passkey

Endpoint to delete a registered passkey for the current user.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(ManageSecurityApi::class.java)
val credentialId : kotlin.String = credentialId_example // kotlin.String | 

launch(Dispatchers.IO) {
    webService.deleteRegisteredPasskeyApiV1SecurityPasskeysCredentialIdDelete(credentialId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **credentialId** | **kotlin.String**|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Registered Passkeys

Endpoint to retrieve registered passkeys for the current user.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(ManageSecurityApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<RegisteredPasskeyCredentialsDto> = webService.getRegisteredPasskeysApiV1SecurityPasskeysGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;RegisteredPasskeyCredentialsDto&gt;**](RegisteredPasskeyCredentialsDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

