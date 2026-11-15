# WalletAuthApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**authSiweBindAuthSiweBindPost**](WalletAuthApi.md#authSiweBindAuthSiweBindPost) | **POST** auth/siwe/bind | Bind one SIWE wallet onto the identified Keycloak person |
| [**authSiweMeAuthSiweMeGet**](WalletAuthApi.md#authSiweMeAuthSiweMeGet) | **GET** auth/siwe/me | Wallet bound to the identified Keycloak person |
| [**authSiweNonceAuthSiweNoncePost**](WalletAuthApi.md#authSiweNonceAuthSiweNoncePost) | **POST** auth/siwe/nonce | Issue an EIP-4361 nonce for the identified Keycloak person |



Bind one SIWE wallet onto the identified Keycloak person

Verifies EIP-4361 and stores the recovered address only. Not a second login. Signature is not stored or returned.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(WalletAuthApi::class.java)
val walletAuthSiweBindRequest : WalletAuthSiweBindRequest =  // WalletAuthSiweBindRequest | 

launch(Dispatchers.IO) {
    val result : WalletAuthWalletBindingResponse = webService.authSiweBindAuthSiweBindPost(walletAuthSiweBindRequest)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **walletAuthSiweBindRequest** | [**WalletAuthSiweBindRequest**](WalletAuthSiweBindRequest.md)|  | |

### Return type

[**WalletAuthWalletBindingResponse**](WalletAuthWalletBindingResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Wallet bound to the identified Keycloak person

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(WalletAuthApi::class.java)

launch(Dispatchers.IO) {
    val result : WalletAuthWalletBindingResponse = webService.authSiweMeAuthSiweMeGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WalletAuthWalletBindingResponse**](WalletAuthWalletBindingResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Issue an EIP-4361 nonce for the identified Keycloak person

Keycloak OIDC remains the login. This nonce is only for binding one wallet to that same person. Password grant stays off.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(WalletAuthApi::class.java)
val walletAuthSiweNonceRequest : WalletAuthSiweNonceRequest =  // WalletAuthSiweNonceRequest | 

launch(Dispatchers.IO) {
    val result : WalletAuthSiweNonceResponse = webService.authSiweNonceAuthSiweNoncePost(walletAuthSiweNonceRequest)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **walletAuthSiweNonceRequest** | [**WalletAuthSiweNonceRequest**](WalletAuthSiweNonceRequest.md)|  | |

### Return type

[**WalletAuthSiweNonceResponse**](WalletAuthSiweNonceResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

