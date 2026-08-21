# AppConfigurationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAppConfigurationApiV1AppConfigurationGet**](AppConfigurationApi.md#getAppConfigurationApiV1AppConfigurationGet) | **GET** api/v1/app_configuration/ | Get App Configuration |



Get App Configuration

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AppConfigurationApi::class.java)

launch(Dispatchers.IO) {
    val result : AppConfigurationDto = webService.getAppConfigurationApiV1AppConfigurationGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AppConfigurationDto**](AppConfigurationDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

