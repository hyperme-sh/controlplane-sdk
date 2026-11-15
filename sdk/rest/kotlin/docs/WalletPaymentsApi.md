# WalletPaymentsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**challengeApiV1PaymentsHostPayoutAddressChallengePost**](WalletPaymentsApi.md#challengeApiV1PaymentsHostPayoutAddressChallengePost) | **POST** api/v1/payments/host-payout-address/challenge | Challenge |
| [**createWalletCheckout**](WalletPaymentsApi.md#createWalletCheckout) | **POST** api/v1/payments/wallet/lease-payments/{billing_record_id}/checkout | Open Stablecoin Checkout |
| [**createWalletDeposit**](WalletPaymentsApi.md#createWalletDeposit) | **POST** api/v1/payments/wallet/lease-payments/{billing_record_id}/deposit | Create Deposit |
| [**createWalletLeasePayment**](WalletPaymentsApi.md#createWalletLeasePayment) | **POST** api/v1/payments/wallet/lease-payments | Create Usdc Lease Payment Route |
| [**getWalletDeposit**](WalletPaymentsApi.md#getWalletDeposit) | **GET** api/v1/payments/wallet/lease-payments/{billing_record_id}/deposit | Deposit Status |
| [**getWalletPaymentCapabilities**](WalletPaymentsApi.md#getWalletPaymentCapabilities) | **GET** api/v1/payments/wallet/capabilities | Wallet Capabilities |
| [**submitApiV1PaymentsHostPayoutAddressPost**](WalletPaymentsApi.md#submitApiV1PaymentsHostPayoutAddressPost) | **POST** api/v1/payments/host-payout-address | Submit |



Challenge

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(WalletPaymentsApi::class.java)
val xTenantID : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | Must match the browser tenant session
val walletPaymentChallengeRequest : WalletPaymentChallengeRequest =  // WalletPaymentChallengeRequest | 

launch(Dispatchers.IO) {
    val result : WalletPaymentPayoutChallenge = webService.challengeApiV1PaymentsHostPayoutAddressChallengePost(xTenantID, walletPaymentChallengeRequest)
}
```

### Parameters
| **xTenantID** | **java.util.UUID**| Must match the browser tenant session | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **walletPaymentChallengeRequest** | [**WalletPaymentChallengeRequest**](WalletPaymentChallengeRequest.md)|  | |

### Return type

[**WalletPaymentPayoutChallenge**](WalletPaymentPayoutChallenge.md)

### Authorization


Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Open Stablecoin Checkout

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(WalletPaymentsApi::class.java)
val billingRecordId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val xTenantID : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : WalletPaymentWalletCheckoutResponse = webService.createWalletCheckout(billingRecordId, xTenantID)
}
```

### Parameters
| **billingRecordId** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **xTenantID** | **java.util.UUID**|  | |

### Return type

[**WalletPaymentWalletCheckoutResponse**](WalletPaymentWalletCheckoutResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Create Deposit

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(WalletPaymentsApi::class.java)
val billingRecordId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val xTenantID : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : WalletPaymentWalletDepositStatus = webService.createWalletDeposit(billingRecordId, xTenantID)
}
```

### Parameters
| **billingRecordId** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **xTenantID** | **java.util.UUID**|  | |

### Return type

[**WalletPaymentWalletDepositStatus**](WalletPaymentWalletDepositStatus.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Create Usdc Lease Payment Route

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(WalletPaymentsApi::class.java)
val xTenantID : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val walletPaymentUsdcLeasePaymentCreate : WalletPaymentUsdcLeasePaymentCreate =  // WalletPaymentUsdcLeasePaymentCreate | 
val idempotencyKey : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | Reuse the same UUID when retrying the same payment request.

launch(Dispatchers.IO) {
    val result : WalletPaymentWalletLeasePaymentResponse = webService.createWalletLeasePayment(xTenantID, walletPaymentUsdcLeasePaymentCreate, idempotencyKey)
}
```

### Parameters
| **xTenantID** | **java.util.UUID**|  | |
| **walletPaymentUsdcLeasePaymentCreate** | [**WalletPaymentUsdcLeasePaymentCreate**](WalletPaymentUsdcLeasePaymentCreate.md)|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotencyKey** | **java.util.UUID**| Reuse the same UUID when retrying the same payment request. | [optional] |

### Return type

[**WalletPaymentWalletLeasePaymentResponse**](WalletPaymentWalletLeasePaymentResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Deposit Status

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(WalletPaymentsApi::class.java)
val billingRecordId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val xTenantID : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : WalletPaymentWalletDepositStatus = webService.getWalletDeposit(billingRecordId, xTenantID)
}
```

### Parameters
| **billingRecordId** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **xTenantID** | **java.util.UUID**|  | |

### Return type

[**WalletPaymentWalletDepositStatus**](WalletPaymentWalletDepositStatus.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Wallet Capabilities

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(WalletPaymentsApi::class.java)
val xTenantID : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : WalletPaymentWalletCapabilities = webService.getWalletPaymentCapabilities(xTenantID)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **xTenantID** | **java.util.UUID**|  | |

### Return type

[**WalletPaymentWalletCapabilities**](WalletPaymentWalletCapabilities.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Submit

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(WalletPaymentsApi::class.java)
val xTenantID : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | Must match the browser tenant session
val walletPaymentSubmitRequest : WalletPaymentSubmitRequest =  // WalletPaymentSubmitRequest | 

launch(Dispatchers.IO) {
    val result : WalletPaymentRegisteredDestination = webService.submitApiV1PaymentsHostPayoutAddressPost(xTenantID, walletPaymentSubmitRequest)
}
```

### Parameters
| **xTenantID** | **java.util.UUID**| Must match the browser tenant session | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **walletPaymentSubmitRequest** | [**WalletPaymentSubmitRequest**](WalletPaymentSubmitRequest.md)|  | |

### Return type

[**WalletPaymentRegisteredDestination**](WalletPaymentRegisteredDestination.md)

### Authorization


Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

