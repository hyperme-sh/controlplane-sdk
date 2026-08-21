# StripeCheckoutApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createHostCheckoutSessionApiV1CheckoutsHostTenantIdTenantPost**](StripeCheckoutApi.md#createHostCheckoutSessionApiV1CheckoutsHostTenantIdTenantPost) | **POST** api/v1/checkouts/host/{tenant_id}/tenant | Create Host Checkout Session |
| [**createTenantCheckoutSessionApiV1CheckoutsTenantSubscriptionPost**](StripeCheckoutApi.md#createTenantCheckoutSessionApiV1CheckoutsTenantSubscriptionPost) | **POST** api/v1/checkouts/tenant/subscription | Create Tenant Checkout Session |
| [**hostCheckoutSuccessApiV1CheckoutsHostPaymentCancelPost**](StripeCheckoutApi.md#hostCheckoutSuccessApiV1CheckoutsHostPaymentCancelPost) | **POST** api/v1/checkouts/host/payment/cancel | Host Checkout Success |
| [**hostCheckoutSuccessApiV1CheckoutsHostPaymentSuccessPost**](StripeCheckoutApi.md#hostCheckoutSuccessApiV1CheckoutsHostPaymentSuccessPost) | **POST** api/v1/checkouts/host/payment/success | Host Checkout Success |
| [**listCheckoutRecordsApiV1CheckoutsAllGet**](StripeCheckoutApi.md#listCheckoutRecordsApiV1CheckoutsAllGet) | **GET** api/v1/checkouts/all | List Checkout Records |
| [**tenantCheckoutCanceledApiV1CheckoutsTenantPaymentCancelPost**](StripeCheckoutApi.md#tenantCheckoutCanceledApiV1CheckoutsTenantPaymentCancelPost) | **POST** api/v1/checkouts/tenant/payment/cancel | Tenant Checkout Canceled |
| [**tenantCheckoutSuccessApiV1CheckoutsTenantPaymentSuccessPost**](StripeCheckoutApi.md#tenantCheckoutSuccessApiV1CheckoutsTenantPaymentSuccessPost) | **POST** api/v1/checkouts/tenant/payment/success | Tenant Checkout Success |



Create Host Checkout Session

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeCheckoutApi::class.java)
val checkoutRequestDto : CheckoutRequestDto =  // CheckoutRequestDto | 

launch(Dispatchers.IO) {
    val result : CheckoutResponseDto = webService.createHostCheckoutSessionApiV1CheckoutsHostTenantIdTenantPost(checkoutRequestDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **checkoutRequestDto** | [**CheckoutRequestDto**](CheckoutRequestDto.md)|  | |

### Return type

[**CheckoutResponseDto**](CheckoutResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Create Tenant Checkout Session

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeCheckoutApi::class.java)
val checkoutRequestDto : CheckoutRequestDto =  // CheckoutRequestDto | 

launch(Dispatchers.IO) {
    val result : CheckoutResponseDto = webService.createTenantCheckoutSessionApiV1CheckoutsTenantSubscriptionPost(checkoutRequestDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **checkoutRequestDto** | [**CheckoutRequestDto**](CheckoutRequestDto.md)|  | |

### Return type

[**CheckoutResponseDto**](CheckoutResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Host Checkout Success

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeCheckoutApi::class.java)
val tenantId : kotlin.String = tenantId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.hostCheckoutSuccessApiV1CheckoutsHostPaymentCancelPost(tenantId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tenantId** | **kotlin.String**|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Host Checkout Success

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeCheckoutApi::class.java)
val sessionId : kotlin.String = sessionId_example // kotlin.String | 
val tenantId : kotlin.String = tenantId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.hostCheckoutSuccessApiV1CheckoutsHostPaymentSuccessPost(sessionId, tenantId)
}
```

### Parameters
| **sessionId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tenantId** | **kotlin.String**|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List Checkout Records

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeCheckoutApi::class.java)
val skip : kotlin.Int = 56 // kotlin.Int | 
val limit : kotlin.Int = 56 // kotlin.Int | 

launch(Dispatchers.IO) {
    val result : BillingRecordListDto = webService.listCheckoutRecordsApiV1CheckoutsAllGet(skip, limit)
}
```

### Parameters
| **skip** | **kotlin.Int**|  | [optional] [default to 0] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **kotlin.Int**|  | [optional] [default to 100] |

### Return type

[**BillingRecordListDto**](BillingRecordListDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Tenant Checkout Canceled

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeCheckoutApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.tenantCheckoutCanceledApiV1CheckoutsTenantPaymentCancelPost()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Tenant Checkout Success

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeCheckoutApi::class.java)
val sessionId : kotlin.String = sessionId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.tenantCheckoutSuccessApiV1CheckoutsTenantPaymentSuccessPost(sessionId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sessionId** | **kotlin.String**|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

