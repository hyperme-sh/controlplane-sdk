# WalletAuthAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authSiweBindAuthSiweBindPost**](WalletAuthAPI.md#authsiwebindauthsiwebindpost) | **POST** /auth/siwe/bind | Bind one SIWE wallet onto the identified Keycloak person
[**authSiweMeAuthSiweMeGet**](WalletAuthAPI.md#authsiwemeauthsiwemeget) | **GET** /auth/siwe/me | Wallet bound to the identified Keycloak person
[**authSiweNonceAuthSiweNoncePost**](WalletAuthAPI.md#authsiwenonceauthsiwenoncepost) | **POST** /auth/siwe/nonce | Issue an EIP-4361 nonce for the identified Keycloak person


# **authSiweBindAuthSiweBindPost**
```swift
    open class func authSiweBindAuthSiweBindPost(walletAuthSiweBindRequest: WalletAuthSiweBindRequest, completion: @escaping (_ data: WalletAuthWalletBindingResponse?, _ error: Error?) -> Void)
```

Bind one SIWE wallet onto the identified Keycloak person

Verifies EIP-4361 and stores the recovered address only. Not a second login. Signature is not stored or returned.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let walletAuthSiweBindRequest = WalletAuthSiweBindRequest(message: "message_example", signature: "signature_example") // WalletAuthSiweBindRequest | 

// Bind one SIWE wallet onto the identified Keycloak person
WalletAuthAPI.authSiweBindAuthSiweBindPost(walletAuthSiweBindRequest: walletAuthSiweBindRequest) { (response, error) in
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
 **walletAuthSiweBindRequest** | [**WalletAuthSiweBindRequest**](WalletAuthSiweBindRequest.md) |  | 

### Return type

[**WalletAuthWalletBindingResponse**](WalletAuthWalletBindingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authSiweMeAuthSiweMeGet**
```swift
    open class func authSiweMeAuthSiweMeGet(completion: @escaping (_ data: WalletAuthWalletBindingResponse?, _ error: Error?) -> Void)
```

Wallet bound to the identified Keycloak person

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Wallet bound to the identified Keycloak person
WalletAuthAPI.authSiweMeAuthSiweMeGet() { (response, error) in
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

[**WalletAuthWalletBindingResponse**](WalletAuthWalletBindingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authSiweNonceAuthSiweNoncePost**
```swift
    open class func authSiweNonceAuthSiweNoncePost(walletAuthSiweNonceRequest: WalletAuthSiweNonceRequest, completion: @escaping (_ data: WalletAuthSiweNonceResponse?, _ error: Error?) -> Void)
```

Issue an EIP-4361 nonce for the identified Keycloak person

Keycloak OIDC remains the login. This nonce is only for binding one wallet to that same person. Password grant stays off.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let walletAuthSiweNonceRequest = WalletAuthSiweNonceRequest(address: "address_example", chainId: 123) // WalletAuthSiweNonceRequest | 

// Issue an EIP-4361 nonce for the identified Keycloak person
WalletAuthAPI.authSiweNonceAuthSiweNoncePost(walletAuthSiweNonceRequest: walletAuthSiweNonceRequest) { (response, error) in
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
 **walletAuthSiweNonceRequest** | [**WalletAuthSiweNonceRequest**](WalletAuthSiweNonceRequest.md) |  | 

### Return type

[**WalletAuthSiweNonceResponse**](WalletAuthSiweNonceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

