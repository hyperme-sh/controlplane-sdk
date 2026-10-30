# DashboardApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getDashboardMetricsApiV1DashboardGet**](DashboardApi.md#getDashboardMetricsApiV1DashboardGet) | **GET** api/v1/dashboard/ | Get Dashboard Metrics |



Get Dashboard Metrics

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(DashboardApi::class.java)
val filter : kotlin.String = filter_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : DashboardMetricsDto = webService.getDashboardMetricsApiV1DashboardGet(filter)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **filter** | **kotlin.String**|  | [optional] [default to all] [enum: today, this_week, last_3_months, all] |

### Return type

[**DashboardMetricsDto**](DashboardMetricsDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

