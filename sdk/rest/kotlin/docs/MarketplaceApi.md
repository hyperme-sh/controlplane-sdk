# MarketplaceApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createListingApiV1MarketplaceListingsPost**](MarketplaceApi.md#createListingApiV1MarketplaceListingsPost) | **POST** api/v1/marketplace/listings | Create Listing |
| [**deleteListingApiV1MarketplaceListingsListingIdDelete**](MarketplaceApi.md#deleteListingApiV1MarketplaceListingsListingIdDelete) | **DELETE** api/v1/marketplace/listings/{listing_id} | Delete Listing |
| [**getListingApiV1MarketplaceListingsListingIdGet**](MarketplaceApi.md#getListingApiV1MarketplaceListingsListingIdGet) | **GET** api/v1/marketplace/listings/{listing_id} | Get Listing |
| [**listListingsApiV1MarketplaceListingsGet**](MarketplaceApi.md#listListingsApiV1MarketplaceListingsGet) | **GET** api/v1/marketplace/listings | List Listings |
| [**purchaseListingApiV1MarketplaceListingsListingIdPurchasePost**](MarketplaceApi.md#purchaseListingApiV1MarketplaceListingsListingIdPurchasePost) | **POST** api/v1/marketplace/listings/{listing_id}/purchase | Purchase Listing |
| [**updateListingApiV1MarketplaceListingsListingIdPatch**](MarketplaceApi.md#updateListingApiV1MarketplaceListingsListingIdPatch) | **PATCH** api/v1/marketplace/listings/{listing_id} | Update Listing |



Create Listing

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(MarketplaceApi::class.java)
val listingCreateBody : ListingCreateBody =  // ListingCreateBody | 

launch(Dispatchers.IO) {
    val result : ListingResponse = webService.createListingApiV1MarketplaceListingsPost(listingCreateBody)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **listingCreateBody** | [**ListingCreateBody**](ListingCreateBody.md)|  | |

### Return type

[**ListingResponse**](ListingResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Delete Listing

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(MarketplaceApi::class.java)
val listingId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    webService.deleteListingApiV1MarketplaceListingsListingIdDelete(listingId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **listingId** | **java.util.UUID**|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Listing

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(MarketplaceApi::class.java)
val listingId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : ListingResponse = webService.getListingApiV1MarketplaceListingsListingIdGet(listingId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **listingId** | **java.util.UUID**|  | |

### Return type

[**ListingResponse**](ListingResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List Listings

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(MarketplaceApi::class.java)
val publicOnly : kotlin.Boolean = true // kotlin.Boolean | 

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<ListingResponse> = webService.listListingsApiV1MarketplaceListingsGet(publicOnly)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **publicOnly** | **kotlin.Boolean**|  | [optional] [default to false] |

### Return type

[**kotlin.collections.List&lt;ListingResponse&gt;**](ListingResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Purchase Listing

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(MarketplaceApi::class.java)
val listingId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val purchaseListingBody : PurchaseListingBody =  // PurchaseListingBody | 

launch(Dispatchers.IO) {
    val result : PurchaseResponse = webService.purchaseListingApiV1MarketplaceListingsListingIdPurchasePost(listingId, purchaseListingBody)
}
```

### Parameters
| **listingId** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **purchaseListingBody** | [**PurchaseListingBody**](PurchaseListingBody.md)|  | [optional] |

### Return type

[**PurchaseResponse**](PurchaseResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Update Listing

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(MarketplaceApi::class.java)
val listingId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val listingUpdateBody : ListingUpdateBody =  // ListingUpdateBody | 

launch(Dispatchers.IO) {
    val result : ListingResponse = webService.updateListingApiV1MarketplaceListingsListingIdPatch(listingId, listingUpdateBody)
}
```

### Parameters
| **listingId** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **listingUpdateBody** | [**ListingUpdateBody**](ListingUpdateBody.md)|  | |

### Return type

[**ListingResponse**](ListingResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

