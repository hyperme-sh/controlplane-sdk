# AccountAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeEmailApiV1AccountChangeEmailRequestPatch**](AccountAPI.md#changeemailapiv1accountchangeemailrequestpatch) | **PATCH** /api/v1/account/change_email_request | Change Email
[**changeEmailConfirmationApiV1AccountChangeEmailConfirmationPatch**](AccountAPI.md#changeemailconfirmationapiv1accountchangeemailconfirmationpatch) | **PATCH** /api/v1/account/change_email_confirmation | Change Email Confirmation
[**logoutApiV1AccountLogoutGet**](AccountAPI.md#logoutapiv1accountlogoutget) | **GET** /api/v1/account/logout | Logout
[**readUsersMeApiV1AccountMeGet**](AccountAPI.md#readusersmeapiv1accountmeget) | **GET** /api/v1/account/me | Read Users Me
[**resendActivationEmailApiV1AccountResendActivationEmailPost**](AccountAPI.md#resendactivationemailapiv1accountresendactivationemailpost) | **POST** /api/v1/account/resend_activation_email | Resend Activation Email


# **changeEmailApiV1AccountChangeEmailRequestPatch**
```swift
    open class func changeEmailApiV1AccountChangeEmailRequestPatch(changeEmailRequestDto: ChangeEmailRequestDto, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Change Email

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let changeEmailRequestDto = ChangeEmailRequestDto(newEmail: "newEmail_example") // ChangeEmailRequestDto | 

// Change Email
AccountAPI.changeEmailApiV1AccountChangeEmailRequestPatch(changeEmailRequestDto: changeEmailRequestDto) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changeEmailRequestDto** | [**ChangeEmailRequestDto**](ChangeEmailRequestDto.md) |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **changeEmailConfirmationApiV1AccountChangeEmailConfirmationPatch**
```swift
    open class func changeEmailConfirmationApiV1AccountChangeEmailConfirmationPatch(changeEmailConfirmRequestDto: ChangeEmailConfirmRequestDto, completion: @escaping (_ data: ChangeEmailResponseDto?, _ error: Error?) -> Void)
```

Change Email Confirmation

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let changeEmailConfirmRequestDto = ChangeEmailConfirmRequestDto(token: "token_example") // ChangeEmailConfirmRequestDto | 

// Change Email Confirmation
AccountAPI.changeEmailConfirmationApiV1AccountChangeEmailConfirmationPatch(changeEmailConfirmRequestDto: changeEmailConfirmRequestDto) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changeEmailConfirmRequestDto** | [**ChangeEmailConfirmRequestDto**](ChangeEmailConfirmRequestDto.md) |  | 

### Return type

[**ChangeEmailResponseDto**](ChangeEmailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logoutApiV1AccountLogoutGet**
```swift
    open class func logoutApiV1AccountLogoutGet(completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Logout

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Logout
AccountAPI.logoutApiV1AccountLogoutGet() { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **readUsersMeApiV1AccountMeGet**
```swift
    open class func readUsersMeApiV1AccountMeGet(completion: @escaping (_ data: MeResponseDto?, _ error: Error?) -> Void)
```

Read Users Me

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Read Users Me
AccountAPI.readUsersMeApiV1AccountMeGet() { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MeResponseDto**](MeResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resendActivationEmailApiV1AccountResendActivationEmailPost**
```swift
    open class func resendActivationEmailApiV1AccountResendActivationEmailPost(completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Resend Activation Email

Removed: activation is handled by Keycloak.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Resend Activation Email
AccountAPI.resendActivationEmailApiV1AccountResendActivationEmailPost() { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

Void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

