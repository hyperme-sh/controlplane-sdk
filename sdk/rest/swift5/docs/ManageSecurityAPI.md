# ManageSecurityAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRegisteredPasskeyApiV1SecurityPasskeysCredentialIdDelete**](ManageSecurityAPI.md#deleteregisteredpasskeyapiv1securitypasskeyscredentialiddelete) | **DELETE** /api/v1/security/passkeys/{credential_id} | Delete Registered Passkey
[**getRegisteredPasskeysApiV1SecurityPasskeysGet**](ManageSecurityAPI.md#getregisteredpasskeysapiv1securitypasskeysget) | **GET** /api/v1/security/passkeys | Get Registered Passkeys


# **deleteRegisteredPasskeyApiV1SecurityPasskeysCredentialIdDelete**
```swift
    open class func deleteRegisteredPasskeyApiV1SecurityPasskeysCredentialIdDelete(credentialId: String, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Delete Registered Passkey

Endpoint to delete a registered passkey for the current user.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let credentialId = "credentialId_example" // String | 

// Delete Registered Passkey
ManageSecurityAPI.deleteRegisteredPasskeyApiV1SecurityPasskeysCredentialIdDelete(credentialId: credentialId) { (response, error) in
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
 **credentialId** | **String** |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getRegisteredPasskeysApiV1SecurityPasskeysGet**
```swift
    open class func getRegisteredPasskeysApiV1SecurityPasskeysGet(completion: @escaping (_ data: [RegisteredPasskeyCredentialsDto]?, _ error: Error?) -> Void)
```

Get Registered Passkeys

Endpoint to retrieve registered passkeys for the current user.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get Registered Passkeys
ManageSecurityAPI.getRegisteredPasskeysApiV1SecurityPasskeysGet() { (response, error) in
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

[**[RegisteredPasskeyCredentialsDto]**](RegisteredPasskeyCredentialsDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

