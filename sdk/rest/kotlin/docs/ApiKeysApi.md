# ApiKeysApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createApiKeyApiV1ApiKeysPost**](ApiKeysApi.md#createApiKeyApiV1ApiKeysPost) | **POST** api/v1/api-keys | Create Api Key |
| [**internalValidateApiV1InternalValidatePost**](ApiKeysApi.md#internalValidateApiV1InternalValidatePost) | **POST** api/v1/internal/validate | Internal Validate |
| [**listApiKeysApiV1ApiKeysGet**](ApiKeysApi.md#listApiKeysApiV1ApiKeysGet) | **GET** api/v1/api-keys | List Api Keys |
| [**revokeApiKeyApiV1ApiKeysKeyIdDelete**](ApiKeysApi.md#revokeApiKeyApiV1ApiKeysKeyIdDelete) | **DELETE** api/v1/api-keys/{key_id} | Revoke Api Key |



Create Api Key

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(ApiKeysApi::class.java)
val apiKeyCreateRequest : ApiKeyCreateRequest =  // ApiKeyCreateRequest | 

launch(Dispatchers.IO) {
    val result : ApiKeyCreatedResponse = webService.createApiKeyApiV1ApiKeysPost(apiKeyCreateRequest)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **apiKeyCreateRequest** | [**ApiKeyCreateRequest**](ApiKeyCreateRequest.md)|  | |

### Return type

[**ApiKeyCreatedResponse**](ApiKeyCreatedResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Internal Validate

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(ApiKeysApi::class.java)
val internalValidateRequest : InternalValidateRequest =  // InternalValidateRequest | 
val xInternalToken : kotlin.String = xInternalToken_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : InternalValidateResponse = webService.internalValidateApiV1InternalValidatePost(internalValidateRequest, xInternalToken)
}
```

### Parameters
| **internalValidateRequest** | [**InternalValidateRequest**](InternalValidateRequest.md)|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **xInternalToken** | **kotlin.String**|  | [optional] |

### Return type

[**InternalValidateResponse**](InternalValidateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


List Api Keys

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(ApiKeysApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<ApiKeyResponse> = webService.listApiKeysApiV1ApiKeysGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;ApiKeyResponse&gt;**](ApiKeyResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Revoke Api Key

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(ApiKeysApi::class.java)
val keyId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    webService.revokeApiKeyApiV1ApiKeysKeyIdDelete(keyId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **keyId** | **java.util.UUID**|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

