# PaymentsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**allocateBudgetApiV1BudgetsBudgetIdAllocatePost**](PaymentsApi.md#allocateBudgetApiV1BudgetsBudgetIdAllocatePost) | **POST** api/v1/budgets/{budget_id}/allocate | Allocate Budget |
| [**apiV1BudgetsGet**](PaymentsApi.md#apiV1BudgetsGet) | **GET** api/v1/budgets | List crypto budgets |
| [**createCheckoutSessionApiV1PaymentsStripeCheckoutSessionsPost**](PaymentsApi.md#createCheckoutSessionApiV1PaymentsStripeCheckoutSessionsPost) | **POST** api/v1/payments/stripe/checkout-sessions | Create Checkout Session |
| [**createCryptoBudgetApiV1BudgetsPost**](PaymentsApi.md#createCryptoBudgetApiV1BudgetsPost) | **POST** api/v1/budgets | Create Crypto Budget |
| [**getCryptoBudgetApiV1BudgetsBudgetIdGet**](PaymentsApi.md#getCryptoBudgetApiV1BudgetsBudgetIdGet) | **GET** api/v1/budgets/{budget_id} | Get Crypto Budget |
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


Create Checkout Session

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
val stripeCheckoutSessionCreate : StripeCheckoutSessionCreate =  // StripeCheckoutSessionCreate | 

launch(Dispatchers.IO) {
    val result : StripeCheckoutSessionResponse = webService.createCheckoutSessionApiV1PaymentsStripeCheckoutSessionsPost(stripeCheckoutSessionCreate)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **stripeCheckoutSessionCreate** | [**StripeCheckoutSessionCreate**](StripeCheckoutSessionCreate.md)|  | |

### Return type

[**StripeCheckoutSessionResponse**](StripeCheckoutSessionResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
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

