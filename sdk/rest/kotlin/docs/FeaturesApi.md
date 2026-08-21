# FeaturesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listFeaturesApiV1FeaturesGet**](FeaturesApi.md#listFeaturesApiV1FeaturesGet) | **GET** api/v1/features/ | List Features |



List Features

List all available features. Requires HOST_MANAGE_TENANTS permission.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(FeaturesApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<Feature> = webService.listFeaturesApiV1FeaturesGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;Feature&gt;**](Feature.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

