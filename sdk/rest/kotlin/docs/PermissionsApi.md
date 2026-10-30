# PermissionsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getPermissionsApiV1PermissionsGet**](PermissionsApi.md#getPermissionsApiV1PermissionsGet) | **GET** api/v1/permissions/ | Get Permissions |



Get Permissions

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(PermissionsApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<PermissionDto> = webService.getPermissionsApiV1PermissionsGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;PermissionDto&gt;**](PermissionDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

