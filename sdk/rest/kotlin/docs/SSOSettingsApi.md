# SSOSettingsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createSsoSettingsApiV1SsosPost**](SSOSettingsApi.md#createSsoSettingsApiV1SsosPost) | **POST** api/v1/ssos/ | Create Sso Settings |
| [**deleteSsoSettingsApiV1SsosSsoIdDelete**](SSOSettingsApi.md#deleteSsoSettingsApiV1SsosSsoIdDelete) | **DELETE** api/v1/ssos/{sso_id} | Delete Sso Settings |
| [**getAvailableSsoProvidersApiV1SsosAvailableProvidersGet**](SSOSettingsApi.md#getAvailableSsoProvidersApiV1SsosAvailableProvidersGet) | **GET** api/v1/ssos/available-providers | Get Available Sso Providers |
| [**getSsoSettingsByIdApiV1SsosSsoIdGet**](SSOSettingsApi.md#getSsoSettingsByIdApiV1SsosSsoIdGet) | **GET** api/v1/ssos/{sso_id} | Get Sso Settings By Id |
| [**listApiV1SsosGet**](SSOSettingsApi.md#listApiV1SsosGet) | **GET** api/v1/ssos/ | List |
| [**updateSsoSettingsApiV1SsosSsoIdPatch**](SSOSettingsApi.md#updateSsoSettingsApiV1SsosSsoIdPatch) | **PATCH** api/v1/ssos/{sso_id} | Update Sso Settings |



Create Sso Settings

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(SSOSettingsApi::class.java)
val createSSOSettingsDto : CreateSSOSettingsDto =  // CreateSSOSettingsDto | 

launch(Dispatchers.IO) {
    val result : SSOSettingsResponseDto = webService.createSsoSettingsApiV1SsosPost(createSSOSettingsDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createSSOSettingsDto** | [**CreateSSOSettingsDto**](CreateSSOSettingsDto.md)|  | |

### Return type

[**SSOSettingsResponseDto**](SSOSettingsResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Delete Sso Settings

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(SSOSettingsApi::class.java)
val ssoId : kotlin.String = ssoId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.Boolean = webService.deleteSsoSettingsApiV1SsosSsoIdDelete(ssoId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ssoId** | **kotlin.String**|  | |

### Return type

**kotlin.Boolean**

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Available Sso Providers

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(SSOSettingsApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<kotlin.Any> = webService.getAvailableSsoProvidersApiV1SsosAvailableProvidersGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;kotlin.Any&gt;**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Sso Settings By Id

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(SSOSettingsApi::class.java)
val ssoId : kotlin.String = ssoId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : ReadSSOSettingsDto = webService.getSsoSettingsByIdApiV1SsosSsoIdGet(ssoId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ssoId** | **kotlin.String**|  | |

### Return type

[**ReadSSOSettingsDto**](ReadSSOSettingsDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(SSOSettingsApi::class.java)

launch(Dispatchers.IO) {
    val result : SSOSettingsListDto = webService.listApiV1SsosGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SSOSettingsListDto**](SSOSettingsListDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Update Sso Settings

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(SSOSettingsApi::class.java)
val ssoId : kotlin.String = ssoId_example // kotlin.String | 
val updateSSOSettingsDto : UpdateSSOSettingsDto =  // UpdateSSOSettingsDto | 

launch(Dispatchers.IO) {
    webService.updateSsoSettingsApiV1SsosSsoIdPatch(ssoId, updateSSOSettingsDto)
}
```

### Parameters
| **ssoId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **updateSSOSettingsDto** | [**UpdateSSOSettingsDto**](UpdateSSOSettingsDto.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

