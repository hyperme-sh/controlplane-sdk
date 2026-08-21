# AccountApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**changeEmailApiV1AccountChangeEmailRequestPatch**](AccountApi.md#changeEmailApiV1AccountChangeEmailRequestPatch) | **PATCH** api/v1/account/change_email_request | Change Email |
| [**changeEmailConfirmationApiV1AccountChangeEmailConfirmationPatch**](AccountApi.md#changeEmailConfirmationApiV1AccountChangeEmailConfirmationPatch) | **PATCH** api/v1/account/change_email_confirmation | Change Email Confirmation |
| [**logoutApiV1AccountLogoutGet**](AccountApi.md#logoutApiV1AccountLogoutGet) | **GET** api/v1/account/logout | Logout |
| [**readUsersMeApiV1AccountMeGet**](AccountApi.md#readUsersMeApiV1AccountMeGet) | **GET** api/v1/account/me | Read Users Me |
| [**resendActivationEmailApiV1AccountResendActivationEmailPost**](AccountApi.md#resendActivationEmailApiV1AccountResendActivationEmailPost) | **POST** api/v1/account/resend_activation_email | Resend Activation Email |



Change Email

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AccountApi::class.java)
val changeEmailRequestDto : ChangeEmailRequestDto =  // ChangeEmailRequestDto | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.changeEmailApiV1AccountChangeEmailRequestPatch(changeEmailRequestDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **changeEmailRequestDto** | [**ChangeEmailRequestDto**](ChangeEmailRequestDto.md)|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Change Email Confirmation

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(AccountApi::class.java)
val changeEmailConfirmRequestDto : ChangeEmailConfirmRequestDto =  // ChangeEmailConfirmRequestDto | 

launch(Dispatchers.IO) {
    val result : ChangeEmailResponseDto = webService.changeEmailConfirmationApiV1AccountChangeEmailConfirmationPatch(changeEmailConfirmRequestDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **changeEmailConfirmRequestDto** | [**ChangeEmailConfirmRequestDto**](ChangeEmailConfirmRequestDto.md)|  | |

### Return type

[**ChangeEmailResponseDto**](ChangeEmailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Logout

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AccountApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.logoutApiV1AccountLogoutGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Read Users Me

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AccountApi::class.java)

launch(Dispatchers.IO) {
    val result : MeResponseDto = webService.readUsersMeApiV1AccountMeGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MeResponseDto**](MeResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Resend Activation Email

Removed: activation is handled by Keycloak.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(AccountApi::class.java)

launch(Dispatchers.IO) {
    webService.resendActivationEmailApiV1AccountResendActivationEmailPost()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

