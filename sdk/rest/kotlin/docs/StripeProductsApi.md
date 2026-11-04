# StripeProductsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createProductApiV1ProductsPost**](StripeProductsApi.md#createProductApiV1ProductsPost) | **POST** api/v1/products/ | Create a Product |
| [**deleteProductApiV1ProductsProductIdDelete**](StripeProductsApi.md#deleteProductApiV1ProductsProductIdDelete) | **DELETE** api/v1/products/{product_id} | Delete a Product |
| [**getProductByIdApiV1ProductsProductIdGet**](StripeProductsApi.md#getProductByIdApiV1ProductsProductIdGet) | **GET** api/v1/products/{product_id} | Get Product by ID |
| [**listProductsApiV1ProductsGet**](StripeProductsApi.md#listProductsApiV1ProductsGet) | **GET** api/v1/products/ | List Products |
| [**updateProductApiV1ProductsProductIdPatch**](StripeProductsApi.md#updateProductApiV1ProductsProductIdPatch) | **PATCH** api/v1/products/{product_id} | Update a Product |



Create a Product

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeProductsApi::class.java)
val createProductDto : CreateProductDto =  // CreateProductDto | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.createProductApiV1ProductsPost(createProductDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createProductDto** | [**CreateProductDto**](CreateProductDto.md)|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Delete a Product

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeProductsApi::class.java)
val productId : kotlin.String = productId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.deleteProductApiV1ProductsProductIdDelete(productId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **productId** | **kotlin.String**|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Product by ID

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeProductsApi::class.java)
val productId : kotlin.String = productId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : ProductDto = webService.getProductByIdApiV1ProductsProductIdGet(productId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **productId** | **kotlin.String**|  | |

### Return type

[**ProductDto**](ProductDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List Products

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeProductsApi::class.java)
val active : kotlin.Boolean = true // kotlin.Boolean | Filter active products, defaults to True

launch(Dispatchers.IO) {
    val result : ProductListDto = webService.listProductsApiV1ProductsGet(active)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **active** | **kotlin.Boolean**| Filter active products, defaults to True | [optional] [default to true] |

### Return type

[**ProductListDto**](ProductListDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Update a Product

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeProductsApi::class.java)
val productId : kotlin.String = productId_example // kotlin.String | 
val createProductDto : CreateProductDto =  // CreateProductDto | 

launch(Dispatchers.IO) {
    webService.updateProductApiV1ProductsProductIdPatch(productId, createProductDto)
}
```

### Parameters
| **productId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createProductDto** | [**CreateProductDto**](CreateProductDto.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

