# AiApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**apiV1AiUsageHistoryGet**](AiApi.md#apiV1AiUsageHistoryGet) | **GET** api/v1/ai/usage/history | List inference usage history |
| [**apiV1AiUsageSummaryGet**](AiApi.md#apiV1AiUsageSummaryGet) | **GET** api/v1/ai/usage/summary | Tenant usage summary |



List inference usage history

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(AiApi::class.java)
val limit : kotlin.Int = 56 // kotlin.Int | 
val offset : kotlin.Int = 56 // kotlin.Int | 
val userId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : InferenceHistoryPage = webService.apiV1AiUsageHistoryGet(limit, offset, userId)
}
```

### Parameters
| **limit** | **kotlin.Int**|  | [optional] [default to 50] |
| **offset** | **kotlin.Int**|  | [optional] [default to 0] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **userId** | **java.util.UUID**|  | [optional] |

### Return type

[**InferenceHistoryPage**](InferenceHistoryPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Tenant usage summary

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(AiApi::class.java)

launch(Dispatchers.IO) {
    val result : TenantUsageSummaryResponse = webService.apiV1AiUsageSummaryGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TenantUsageSummaryResponse**](TenantUsageSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

