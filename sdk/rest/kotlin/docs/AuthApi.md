# AuthApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**authCallbackAuthCallbackGet**](AuthApi.md#authCallbackAuthCallbackGet) | **GET** auth/callback | OAuth2 authorization code callback |
| [**authLoginAuthLoginPost**](AuthApi.md#authLoginAuthLoginPost) | **POST** auth/login | Start OIDC login |
| [**authMeAuthMeGet**](AuthApi.md#authMeAuthMeGet) | **GET** auth/me | Auth Me |
| [**authRefreshAuthRefreshPost**](AuthApi.md#authRefreshAuthRefreshPost) | **POST** auth/refresh | Refresh access token |
| [**authTenantProbeAuthTenantGet**](AuthApi.md#authTenantProbeAuthTenantGet) | **GET** auth/tenant | Example route using get_current_tenant dependency |



OAuth2 authorization code callback

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(AuthApi::class.java)
val code : kotlin.String = code_example // kotlin.String | 
val state : kotlin.String = state_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : TokenBundleResponse = webService.authCallbackAuthCallbackGet(code, state)
}
```

### Parameters
| **code** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **state** | **kotlin.String**|  | [optional] |

### Return type

[**TokenBundleResponse**](TokenBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Start OIDC login

Returns Keycloak authorization URL; optional identity_provider_hint selects broker (Google, Entra, GitHub, …).

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(AuthApi::class.java)
val loginStartRequest : LoginStartRequest =  // LoginStartRequest | 

launch(Dispatchers.IO) {
    val result : LoginStartResponse = webService.authLoginAuthLoginPost(loginStartRequest)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **loginStartRequest** | [**LoginStartRequest**](LoginStartRequest.md)|  | [optional] |

### Return type

[**LoginStartResponse**](LoginStartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Auth Me

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AuthApi::class.java)

launch(Dispatchers.IO) {
    val result : AuthMeResponse = webService.authMeAuthMeGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthMeResponse**](AuthMeResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Refresh access token

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(AuthApi::class.java)
val refreshTokenRequest : RefreshTokenRequest =  // RefreshTokenRequest | 

launch(Dispatchers.IO) {
    val result : TokenBundleResponse = webService.authRefreshAuthRefreshPost(refreshTokenRequest)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **refreshTokenRequest** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | |

### Return type

[**TokenBundleResponse**](TokenBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Example route using get_current_tenant dependency

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AuthApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.Map<kotlin.String, kotlin.Any> = webService.authTenantProbeAuthTenantGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.Map&lt;kotlin.String, kotlin.Any&gt;**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

