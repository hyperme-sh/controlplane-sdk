# StorageSettingsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**configureStorageApiV1StorageConfigurePost**](StorageSettingsApi.md#configureStorageApiV1StorageConfigurePost) | **POST** api/v1/storage/configure | Configure Storage |
| [**getAvailableProvidersApiV1StorageAvailableGet**](StorageSettingsApi.md#getAvailableProvidersApiV1StorageAvailableGet) | **GET** api/v1/storage/available | Get Available Providers |
| [**getStorageSettingsApiV1StorageGet**](StorageSettingsApi.md#getStorageSettingsApiV1StorageGet) | **GET** api/v1/storage/ | Get Storage Settings |
| [**resetStorageApiV1StorageStorageIdResetPatch**](StorageSettingsApi.md#resetStorageApiV1StorageStorageIdResetPatch) | **PATCH** api/v1/storage/{storage_id}/reset | Reset Storage |



Configure Storage

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StorageSettingsApi::class.java)
val storageSettingsDto : StorageSettingsDto =  // StorageSettingsDto | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.configureStorageApiV1StorageConfigurePost(storageSettingsDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **storageSettingsDto** | [**StorageSettingsDto**](StorageSettingsDto.md)|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Get Available Providers

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StorageSettingsApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<kotlin.collections.Map<kotlin.String, kotlin.String>> = webService.getAvailableProvidersApiV1StorageAvailableGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**kotlin.collections.List&lt;kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;&gt;**

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Storage Settings

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StorageSettingsApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<AvailableStorageProviderDto> = webService.getStorageSettingsApiV1StorageGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;AvailableStorageProviderDto&gt;**](AvailableStorageProviderDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Reset Storage

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StorageSettingsApi::class.java)
val storageId : kotlin.String = storageId_example // kotlin.String | 

launch(Dispatchers.IO) {
    webService.resetStorageApiV1StorageStorageIdResetPatch(storageId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **storageId** | **kotlin.String**|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

