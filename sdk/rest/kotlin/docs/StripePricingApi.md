# StripePricingApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createPricingApiV1PricesPost**](StripePricingApi.md#createPricingApiV1PricesPost) | **POST** api/v1/prices/ | Create Pricing |
| [**getPricingListApiV1PricesGet**](StripePricingApi.md#getPricingListApiV1PricesGet) | **GET** api/v1/prices/ | Get Pricing List |
| [**updatePricingApiV1PricesPriceIdPatch**](StripePricingApi.md#updatePricingApiV1PricesPriceIdPatch) | **PATCH** api/v1/prices/{price_id} | Update Pricing |



Create Pricing

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripePricingApi::class.java)
val createPricingDto : CreatePricingDto =  // CreatePricingDto | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.createPricingApiV1PricesPost(createPricingDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createPricingDto** | [**CreatePricingDto**](CreatePricingDto.md)|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Get Pricing List

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripePricingApi::class.java)

launch(Dispatchers.IO) {
    val result : PricingListDto = webService.getPricingListApiV1PricesGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PricingListDto**](PricingListDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Update Pricing

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripePricingApi::class.java)
val priceId : kotlin.String = priceId_example // kotlin.String | 
val updatePricingDto : UpdatePricingDto =  // UpdatePricingDto | 

launch(Dispatchers.IO) {
    webService.updatePricingApiV1PricesPriceIdPatch(priceId, updatePricingDto)
}
```

### Parameters
| **priceId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **updatePricingDto** | [**UpdatePricingDto**](UpdatePricingDto.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

