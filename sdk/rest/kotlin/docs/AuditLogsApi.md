# AuditLogsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**downloadAuditLogsApiV1AuditLogsDownloadPost**](AuditLogsApi.md#downloadAuditLogsApiV1AuditLogsDownloadPost) | **POST** api/v1/audit-logs/download | Download Audit Logs |
| [**listAuditLogsApiV1AuditLogsGet**](AuditLogsApi.md#listAuditLogsApiV1AuditLogsGet) | **GET** api/v1/audit-logs/ | List Audit Logs |



Download Audit Logs

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AuditLogsApi::class.java)
val downloadAuditRequestDto : DownloadAuditRequestDto =  // DownloadAuditRequestDto | 

launch(Dispatchers.IO) {
    val result : DownloadResponseDto = webService.downloadAuditLogsApiV1AuditLogsDownloadPost(downloadAuditRequestDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **downloadAuditRequestDto** | [**DownloadAuditRequestDto**](DownloadAuditRequestDto.md)|  | |

### Return type

[**DownloadResponseDto**](DownloadResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


List Audit Logs

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AuditLogsApi::class.java)
val limit : kotlin.Int = 56 // kotlin.Int | 
val skip : kotlin.Int = 56 // kotlin.Int | 
val action : kotlin.String = action_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : AuditLogListDto = webService.listAuditLogsApiV1AuditLogsGet(limit, skip, action)
}
```

### Parameters
| **limit** | **kotlin.Int**|  | [optional] [default to 10] |
| **skip** | **kotlin.Int**|  | [optional] [default to 0] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **action** | **kotlin.String**|  | [optional] [enum: create, update, delete, read, login, logout, error, download] |

### Return type

[**AuditLogListDto**](AuditLogListDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

