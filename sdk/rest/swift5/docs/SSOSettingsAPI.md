# SSOSettingsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSsoSettingsApiV1SsosPost**](SSOSettingsAPI.md#createssosettingsapiv1ssospost) | **POST** /api/v1/ssos/ | Create Sso Settings
[**deleteSsoSettingsApiV1SsosSsoIdDelete**](SSOSettingsAPI.md#deletessosettingsapiv1ssosssoiddelete) | **DELETE** /api/v1/ssos/{sso_id} | Delete Sso Settings
[**getAvailableSsoProvidersApiV1SsosAvailableProvidersGet**](SSOSettingsAPI.md#getavailablessoprovidersapiv1ssosavailableprovidersget) | **GET** /api/v1/ssos/available-providers | Get Available Sso Providers
[**getSsoSettingsByIdApiV1SsosSsoIdGet**](SSOSettingsAPI.md#getssosettingsbyidapiv1ssosssoidget) | **GET** /api/v1/ssos/{sso_id} | Get Sso Settings By Id
[**listApiV1SsosGet**](SSOSettingsAPI.md#listapiv1ssosget) | **GET** /api/v1/ssos/ | List
[**updateSsoSettingsApiV1SsosSsoIdPatch**](SSOSettingsAPI.md#updatessosettingsapiv1ssosssoidpatch) | **PATCH** /api/v1/ssos/{sso_id} | Update Sso Settings


# **createSsoSettingsApiV1SsosPost**
```swift
    open class func createSsoSettingsApiV1SsosPost(createSSOSettingsDto: CreateSSOSettingsDto, completion: @escaping (_ data: SSOSettingsResponseDto?, _ error: Error?) -> Void)
```

Create Sso Settings

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let createSSOSettingsDto = CreateSSOSettingsDto(enabled: false, provider: "provider_example", clientId: "clientId_example", clientSecret: "clientSecret_example", scopes: ["scopes_example"], redirectUris: ["redirectUris_example"], tenantId: "tenantId_example") // CreateSSOSettingsDto | 

// Create Sso Settings
SSOSettingsAPI.createSsoSettingsApiV1SsosPost(createSSOSettingsDto: createSSOSettingsDto) { (response, error) in
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
 **createSSOSettingsDto** | [**CreateSSOSettingsDto**](CreateSSOSettingsDto.md) |  | 

### Return type

[**SSOSettingsResponseDto**](SSOSettingsResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteSsoSettingsApiV1SsosSsoIdDelete**
```swift
    open class func deleteSsoSettingsApiV1SsosSsoIdDelete(ssoId: String, completion: @escaping (_ data: Bool?, _ error: Error?) -> Void)
```

Delete Sso Settings

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let ssoId = "ssoId_example" // String | 

// Delete Sso Settings
SSOSettingsAPI.deleteSsoSettingsApiV1SsosSsoIdDelete(ssoId: ssoId) { (response, error) in
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
 **ssoId** | **String** |  | 

### Return type

**Bool**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getAvailableSsoProvidersApiV1SsosAvailableProvidersGet**
```swift
    open class func getAvailableSsoProvidersApiV1SsosAvailableProvidersGet(completion: @escaping (_ data: [AnyCodable]?, _ error: Error?) -> Void)
```

Get Available Sso Providers

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get Available Sso Providers
SSOSettingsAPI.getAvailableSsoProvidersApiV1SsosAvailableProvidersGet() { (response, error) in
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

**[AnyCodable]**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getSsoSettingsByIdApiV1SsosSsoIdGet**
```swift
    open class func getSsoSettingsByIdApiV1SsosSsoIdGet(ssoId: String, completion: @escaping (_ data: ReadSSOSettingsDto?, _ error: Error?) -> Void)
```

Get Sso Settings By Id

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let ssoId = "ssoId_example" // String | 

// Get Sso Settings By Id
SSOSettingsAPI.getSsoSettingsByIdApiV1SsosSsoIdGet(ssoId: ssoId) { (response, error) in
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
 **ssoId** | **String** |  | 

### Return type

[**ReadSSOSettingsDto**](ReadSSOSettingsDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listApiV1SsosGet**
```swift
    open class func listApiV1SsosGet(completion: @escaping (_ data: SSOSettingsListDto?, _ error: Error?) -> Void)
```

List

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// List
SSOSettingsAPI.listApiV1SsosGet() { (response, error) in
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

[**SSOSettingsListDto**](SSOSettingsListDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateSsoSettingsApiV1SsosSsoIdPatch**
```swift
    open class func updateSsoSettingsApiV1SsosSsoIdPatch(ssoId: String, updateSSOSettingsDto: UpdateSSOSettingsDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Update Sso Settings

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let ssoId = "ssoId_example" // String | 
let updateSSOSettingsDto = UpdateSSOSettingsDto(enabled: false, provider: "provider_example", clientId: "clientId_example", clientSecret: "clientSecret_example", scopes: ["scopes_example"]) // UpdateSSOSettingsDto | 

// Update Sso Settings
SSOSettingsAPI.updateSsoSettingsApiV1SsosSsoIdPatch(ssoId: ssoId, updateSSOSettingsDto: updateSSOSettingsDto) { (response, error) in
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
 **ssoId** | **String** |  | 
 **updateSSOSettingsDto** | [**UpdateSSOSettingsDto**](UpdateSSOSettingsDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

