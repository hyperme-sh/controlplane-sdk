# ApiKeysAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApiKeyApiV1ApiKeysPost**](ApiKeysAPI.md#createapikeyapiv1apikeyspost) | **POST** /api/v1/api-keys | Create Api Key
[**internalValidateApiV1InternalValidatePost**](ApiKeysAPI.md#internalvalidateapiv1internalvalidatepost) | **POST** /api/v1/internal/validate | Internal Validate
[**listApiKeysApiV1ApiKeysGet**](ApiKeysAPI.md#listapikeysapiv1apikeysget) | **GET** /api/v1/api-keys | List Api Keys
[**revokeApiKeyApiV1ApiKeysKeyIdDelete**](ApiKeysAPI.md#revokeapikeyapiv1apikeyskeyiddelete) | **DELETE** /api/v1/api-keys/{key_id} | Revoke Api Key


# **createApiKeyApiV1ApiKeysPost**
```swift
    open class func createApiKeyApiV1ApiKeysPost(apiKeyCreateRequest: ApiKeyCreateRequest, completion: @escaping (_ data: ApiKeyCreatedResponse?, _ error: Error?) -> Void)
```

Create Api Key

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let apiKeyCreateRequest = ApiKeyCreateRequest(name: "name_example", scopes: ["scopes_example"]) // ApiKeyCreateRequest | 

// Create Api Key
ApiKeysAPI.createApiKeyApiV1ApiKeysPost(apiKeyCreateRequest: apiKeyCreateRequest) { (response, error) in
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
 **apiKeyCreateRequest** | [**ApiKeyCreateRequest**](ApiKeyCreateRequest.md) |  | 

### Return type

[**ApiKeyCreatedResponse**](ApiKeyCreatedResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internalValidateApiV1InternalValidatePost**
```swift
    open class func internalValidateApiV1InternalValidatePost(internalValidateRequest: InternalValidateRequest, xInternalToken: String? = nil, completion: @escaping (_ data: InternalValidateResponse?, _ error: Error?) -> Void)
```

Internal Validate

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let internalValidateRequest = InternalValidateRequest(apiKey: "apiKey_example", tenantId: 123) // InternalValidateRequest | 
let xInternalToken = "xInternalToken_example" // String |  (optional)

// Internal Validate
ApiKeysAPI.internalValidateApiV1InternalValidatePost(internalValidateRequest: internalValidateRequest, xInternalToken: xInternalToken) { (response, error) in
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
 **internalValidateRequest** | [**InternalValidateRequest**](InternalValidateRequest.md) |  | 
 **xInternalToken** | **String** |  | [optional] 

### Return type

[**InternalValidateResponse**](InternalValidateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listApiKeysApiV1ApiKeysGet**
```swift
    open class func listApiKeysApiV1ApiKeysGet(completion: @escaping (_ data: [ApiKeyResponse]?, _ error: Error?) -> Void)
```

List Api Keys

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// List Api Keys
ApiKeysAPI.listApiKeysApiV1ApiKeysGet() { (response, error) in
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

[**[ApiKeyResponse]**](ApiKeyResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revokeApiKeyApiV1ApiKeysKeyIdDelete**
```swift
    open class func revokeApiKeyApiV1ApiKeysKeyIdDelete(keyId: UUID, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Revoke Api Key

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let keyId = 987 // UUID | 

// Revoke Api Key
ApiKeysAPI.revokeApiKeyApiV1ApiKeysKeyIdDelete(keyId: keyId) { (response, error) in
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
 **keyId** | **UUID** |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

