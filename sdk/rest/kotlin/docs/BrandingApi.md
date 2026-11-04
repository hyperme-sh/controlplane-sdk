# BrandingApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**partialUpdateBrandingApiV1BrandingsBrandingIdPatch**](BrandingApi.md#partialUpdateBrandingApiV1BrandingsBrandingIdPatch) | **PATCH** api/v1/brandings/{branding_id} | Partial Update Branding |
| [**updateBrandingApiV1BrandingsPost**](BrandingApi.md#updateBrandingApiV1BrandingsPost) | **POST** api/v1/brandings/ | Update Branding |
| [**uploadLogoApiV1BrandingsLogoPut**](BrandingApi.md#uploadLogoApiV1BrandingsLogoPut) | **PUT** api/v1/brandings/logo | Upload Logo |



Partial Update Branding

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(BrandingApi::class.java)
val brandingId : kotlin.String = brandingId_example // kotlin.String | 
val updateBrandingDto : UpdateBrandingDto =  // UpdateBrandingDto | 

launch(Dispatchers.IO) {
    webService.partialUpdateBrandingApiV1BrandingsBrandingIdPatch(brandingId, updateBrandingDto)
}
```

### Parameters
| **brandingId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **updateBrandingDto** | [**UpdateBrandingDto**](UpdateBrandingDto.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Update Branding

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(BrandingApi::class.java)
val updateBrandingDto : UpdateBrandingDto =  // UpdateBrandingDto | 

launch(Dispatchers.IO) {
    webService.updateBrandingApiV1BrandingsPost(updateBrandingDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **updateBrandingDto** | [**UpdateBrandingDto**](UpdateBrandingDto.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Upload Logo

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(BrandingApi::class.java)
val file : kotlin.String = file_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.uploadLogoApiV1BrandingsLogoPut(file)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **file** | **kotlin.String**|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

