# PaymentsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**allocateBudgetApiV1BudgetsBudgetIdAllocatePost**](PaymentsApi.md#allocateBudgetApiV1BudgetsBudgetIdAllocatePost) | **POST** api/v1/budgets/{budget_id}/allocate | Allocate Budget |
| [**apiV1BudgetsGet**](PaymentsApi.md#apiV1BudgetsGet) | **GET** api/v1/budgets | List crypto budgets |
| [**createCryptoBudgetApiV1BudgetsPost**](PaymentsApi.md#createCryptoBudgetApiV1BudgetsPost) | **POST** api/v1/budgets | Create Crypto Budget |
| [**createUsdcLeasePaymentRouteApiV1PaymentsUsdcLeasePaymentsPost**](PaymentsApi.md#createUsdcLeasePaymentRouteApiV1PaymentsUsdcLeasePaymentsPost) | **POST** api/v1/payments/usdc/lease-payments | Open a USDC payment for a lease |
| [**getCryptoBudgetApiV1BudgetsBudgetIdGet**](PaymentsApi.md#getCryptoBudgetApiV1BudgetsBudgetIdGet) | **GET** api/v1/budgets/{budget_id} | Get Crypto Budget |
| [**settleUsdcTestCreditApiV1PaymentsUsdcLeasePaymentsBillingRecordIdTestCreditPost**](PaymentsApi.md#settleUsdcTestCreditApiV1PaymentsUsdcLeasePaymentsBillingRecordIdTestCreditPost) | **POST** api/v1/payments/usdc/lease-payments/{billing_record_id}/test-credit | Settle a lease payment from the test-network credit |
| [**stripeWebhookApiV1PaymentsStripeWebhookPost**](PaymentsApi.md#stripeWebhookApiV1PaymentsStripeWebhookPost) | **POST** api/v1/payments/stripe/webhook | Stripe Webhook |



Allocate Budget

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(PaymentsApi::class.java)
val budgetId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val budgetAllocateRequest : BudgetAllocateRequest =  // BudgetAllocateRequest | 

launch(Dispatchers.IO) {
    val result : CryptoBudgetResponse = webService.allocateBudgetApiV1BudgetsBudgetIdAllocatePost(budgetId, budgetAllocateRequest)
}
```

### Parameters
| **budgetId** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **budgetAllocateRequest** | [**BudgetAllocateRequest**](BudgetAllocateRequest.md)|  | |

### Return type

[**CryptoBudgetResponse**](CryptoBudgetResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


List crypto budgets

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(PaymentsApi::class.java)
val limit : kotlin.Int = 56 // kotlin.Int | 
val offset : kotlin.Int = 56 // kotlin.Int | 

launch(Dispatchers.IO) {
    val result : CryptoBudgetListPage = webService.apiV1BudgetsGet(limit, offset)
}
```

### Parameters
| **limit** | **kotlin.Int**|  | [optional] [default to 50] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **offset** | **kotlin.Int**|  | [optional] [default to 0] |

### Return type

[**CryptoBudgetListPage**](CryptoBudgetListPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Create Crypto Budget

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(PaymentsApi::class.java)
val cryptoBudgetCreateRequest : CryptoBudgetCreateRequest =  // CryptoBudgetCreateRequest | 

launch(Dispatchers.IO) {
    val result : CryptoBudgetResponse = webService.createCryptoBudgetApiV1BudgetsPost(cryptoBudgetCreateRequest)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cryptoBudgetCreateRequest** | [**CryptoBudgetCreateRequest**](CryptoBudgetCreateRequest.md)|  | |

### Return type

[**CryptoBudgetResponse**](CryptoBudgetResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Open a USDC payment for a lease

Accepts a tenant-session JWT (human after switch-tenant) or a gateway exchange JWT from a purpose&#x3D;service key or a renter key minted via the org-admin API. Not a portal paste. Not a KV-stashed portal JWT. Raw Keycloak without tenant_id is 403. No card is charged. The renter pays the amount in USDC on Base.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(PaymentsApi::class.java)
val usdcLeasePaymentCreate : UsdcLeasePaymentCreate =  // UsdcLeasePaymentCreate | 

launch(Dispatchers.IO) {
    val result : UsdcLeasePaymentResponse = webService.createUsdcLeasePaymentRouteApiV1PaymentsUsdcLeasePaymentsPost(usdcLeasePaymentCreate)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **usdcLeasePaymentCreate** | [**UsdcLeasePaymentCreate**](UsdcLeasePaymentCreate.md)|  | |

### Return type

[**UsdcLeasePaymentResponse**](UsdcLeasePaymentResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Get Crypto Budget

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(PaymentsApi::class.java)
val budgetId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : CryptoBudgetResponse = webService.getCryptoBudgetApiV1BudgetsBudgetIdGet(budgetId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **budgetId** | **java.util.UUID**|  | |

### Return type

[**CryptoBudgetResponse**](CryptoBudgetResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Settle a lease payment from the test-network credit

Available only where the deployment is Base Sepolia with Stripe in test mode. Marks the pending USDC payment succeeded and publishes payment.succeeded.v1, the same event a confirmed chain transfer publishes. Not available on Base mainnet.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(PaymentsApi::class.java)
val billingRecordId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : UsdcLeasePaymentResponse = webService.settleUsdcTestCreditApiV1PaymentsUsdcLeasePaymentsBillingRecordIdTestCreditPost(billingRecordId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **billingRecordId** | **java.util.UUID**|  | |

### Return type

[**UsdcLeasePaymentResponse**](UsdcLeasePaymentResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Stripe Webhook

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(PaymentsApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.stripeWebhookApiV1PaymentsStripeWebhookPost()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

