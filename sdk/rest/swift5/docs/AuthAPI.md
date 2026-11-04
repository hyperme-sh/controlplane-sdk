# AuthAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authCallbackAuthCallbackGet**](AuthAPI.md#authcallbackauthcallbackget) | **GET** /auth/callback | OAuth2 authorization code callback
[**authLoginAuthLoginPost**](AuthAPI.md#authloginauthloginpost) | **POST** /auth/login | Start OIDC login
[**authMeAuthMeGet**](AuthAPI.md#authmeauthmeget) | **GET** /auth/me | Auth Me
[**authRefreshAuthRefreshPost**](AuthAPI.md#authrefreshauthrefreshpost) | **POST** /auth/refresh | Refresh access token
[**authTenantProbeAuthTenantGet**](AuthAPI.md#authtenantprobeauthtenantget) | **GET** /auth/tenant | Example route using get_current_tenant dependency


# **authCallbackAuthCallbackGet**
```swift
    open class func authCallbackAuthCallbackGet(code: String, state: String? = nil, completion: @escaping (_ data: TokenBundleResponse?, _ error: Error?) -> Void)
```

OAuth2 authorization code callback

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let code = "code_example" // String | 
let state = "state_example" // String |  (optional)

// OAuth2 authorization code callback
AuthAPI.authCallbackAuthCallbackGet(code: code, state: state) { (response, error) in
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
 **code** | **String** |  | 
 **state** | **String** |  | [optional] 

### Return type

[**TokenBundleResponse**](TokenBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authLoginAuthLoginPost**
```swift
    open class func authLoginAuthLoginPost(loginStartRequest: LoginStartRequest? = nil, completion: @escaping (_ data: LoginStartResponse?, _ error: Error?) -> Void)
```

Start OIDC login

Returns Keycloak authorization URL; optional identity_provider_hint selects broker (Google, Entra, GitHub, …).

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let loginStartRequest = LoginStartRequest(identityProviderHint: "identityProviderHint_example") // LoginStartRequest |  (optional)

// Start OIDC login
AuthAPI.authLoginAuthLoginPost(loginStartRequest: loginStartRequest) { (response, error) in
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
 **loginStartRequest** | [**LoginStartRequest**](LoginStartRequest.md) |  | [optional] 

### Return type

[**LoginStartResponse**](LoginStartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authMeAuthMeGet**
```swift
    open class func authMeAuthMeGet(completion: @escaping (_ data: AuthMeResponse?, _ error: Error?) -> Void)
```

Auth Me

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Auth Me
AuthAPI.authMeAuthMeGet() { (response, error) in
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

[**AuthMeResponse**](AuthMeResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authRefreshAuthRefreshPost**
```swift
    open class func authRefreshAuthRefreshPost(refreshTokenRequest: RefreshTokenRequest, completion: @escaping (_ data: TokenBundleResponse?, _ error: Error?) -> Void)
```

Refresh access token

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let refreshTokenRequest = RefreshTokenRequest(refreshToken: "refreshToken_example") // RefreshTokenRequest | 

// Refresh access token
AuthAPI.authRefreshAuthRefreshPost(refreshTokenRequest: refreshTokenRequest) { (response, error) in
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
 **refreshTokenRequest** | [**RefreshTokenRequest**](RefreshTokenRequest.md) |  | 

### Return type

[**TokenBundleResponse**](TokenBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authTenantProbeAuthTenantGet**
```swift
    open class func authTenantProbeAuthTenantGet(completion: @escaping (_ data: [String: AnyCodable]?, _ error: Error?) -> Void)
```

Example route using get_current_tenant dependency

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Example route using get_current_tenant dependency
AuthAPI.authTenantProbeAuthTenantGet() { (response, error) in
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

**[String: AnyCodable]**

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

