# HealthApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**healthCheckApiV1HealthGet**](HealthApi.md#healthCheckApiV1HealthGet) | **GET** api/v1/health/ | Health Check |



Health Check

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(HealthApi::class.java)

launch(Dispatchers.IO) {
    val result : HealthCheckResponseDto = webService.healthCheckApiV1HealthGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthCheckResponseDto**](HealthCheckResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

