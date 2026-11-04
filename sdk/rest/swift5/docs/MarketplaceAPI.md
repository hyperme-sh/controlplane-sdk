# MarketplaceAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createListingApiV1MarketplaceListingsPost**](MarketplaceAPI.md#createlistingapiv1marketplacelistingspost) | **POST** /api/v1/marketplace/listings | Create Listing
[**deleteListingApiV1MarketplaceListingsListingIdDelete**](MarketplaceAPI.md#deletelistingapiv1marketplacelistingslistingiddelete) | **DELETE** /api/v1/marketplace/listings/{listing_id} | Delete Listing
[**getListingApiV1MarketplaceListingsListingIdGet**](MarketplaceAPI.md#getlistingapiv1marketplacelistingslistingidget) | **GET** /api/v1/marketplace/listings/{listing_id} | Get Listing
[**listListingsApiV1MarketplaceListingsGet**](MarketplaceAPI.md#listlistingsapiv1marketplacelistingsget) | **GET** /api/v1/marketplace/listings | List Listings
[**purchaseListingApiV1MarketplaceListingsListingIdPurchasePost**](MarketplaceAPI.md#purchaselistingapiv1marketplacelistingslistingidpurchasepost) | **POST** /api/v1/marketplace/listings/{listing_id}/purchase | Purchase Listing
[**updateListingApiV1MarketplaceListingsListingIdPatch**](MarketplaceAPI.md#updatelistingapiv1marketplacelistingslistingidpatch) | **PATCH** /api/v1/marketplace/listings/{listing_id} | Update Listing


# **createListingApiV1MarketplaceListingsPost**
```swift
    open class func createListingApiV1MarketplaceListingsPost(listingCreateBody: ListingCreateBody, completion: @escaping (_ data: ListingResponse?, _ error: Error?) -> Void)
```

Create Listing

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let listingCreateBody = ListingCreateBody(title: "title_example", description: "description_example", listingType: "listingType_example", priceType: "priceType_example", priceAmount: 123, metadata: "TODO", isPublic: false) // ListingCreateBody | 

// Create Listing
MarketplaceAPI.createListingApiV1MarketplaceListingsPost(listingCreateBody: listingCreateBody) { (response, error) in
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
 **listingCreateBody** | [**ListingCreateBody**](ListingCreateBody.md) |  | 

### Return type

[**ListingResponse**](ListingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteListingApiV1MarketplaceListingsListingIdDelete**
```swift
    open class func deleteListingApiV1MarketplaceListingsListingIdDelete(listingId: UUID, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Delete Listing

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let listingId = 987 // UUID | 

// Delete Listing
MarketplaceAPI.deleteListingApiV1MarketplaceListingsListingIdDelete(listingId: listingId) { (response, error) in
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
 **listingId** | **UUID** |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getListingApiV1MarketplaceListingsListingIdGet**
```swift
    open class func getListingApiV1MarketplaceListingsListingIdGet(listingId: UUID, completion: @escaping (_ data: ListingResponse?, _ error: Error?) -> Void)
```

Get Listing

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let listingId = 987 // UUID | 

// Get Listing
MarketplaceAPI.getListingApiV1MarketplaceListingsListingIdGet(listingId: listingId) { (response, error) in
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
 **listingId** | **UUID** |  | 

### Return type

[**ListingResponse**](ListingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listListingsApiV1MarketplaceListingsGet**
```swift
    open class func listListingsApiV1MarketplaceListingsGet(publicOnly: Bool? = nil, completion: @escaping (_ data: [ListingResponse]?, _ error: Error?) -> Void)
```

List Listings

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let publicOnly = true // Bool |  (optional) (default to false)

// List Listings
MarketplaceAPI.listListingsApiV1MarketplaceListingsGet(publicOnly: publicOnly) { (response, error) in
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
 **publicOnly** | **Bool** |  | [optional] [default to false]

### Return type

[**[ListingResponse]**](ListingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchaseListingApiV1MarketplaceListingsListingIdPurchasePost**
```swift
    open class func purchaseListingApiV1MarketplaceListingsListingIdPurchasePost(listingId: UUID, purchaseListingBody: PurchaseListingBody? = nil, completion: @escaping (_ data: PurchaseResponse?, _ error: Error?) -> Void)
```

Purchase Listing

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let listingId = 987 // UUID | 
let purchaseListingBody = PurchaseListingBody(billingRecordId: 123) // PurchaseListingBody |  (optional)

// Purchase Listing
MarketplaceAPI.purchaseListingApiV1MarketplaceListingsListingIdPurchasePost(listingId: listingId, purchaseListingBody: purchaseListingBody) { (response, error) in
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
 **listingId** | **UUID** |  | 
 **purchaseListingBody** | [**PurchaseListingBody**](PurchaseListingBody.md) |  | [optional] 

### Return type

[**PurchaseResponse**](PurchaseResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateListingApiV1MarketplaceListingsListingIdPatch**
```swift
    open class func updateListingApiV1MarketplaceListingsListingIdPatch(listingId: UUID, listingUpdateBody: ListingUpdateBody, completion: @escaping (_ data: ListingResponse?, _ error: Error?) -> Void)
```

Update Listing

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let listingId = 987 // UUID | 
let listingUpdateBody = ListingUpdateBody(title: "title_example", description: "description_example", metadata: "TODO", isPublic: false) // ListingUpdateBody | 

// Update Listing
MarketplaceAPI.updateListingApiV1MarketplaceListingsListingIdPatch(listingId: listingId, listingUpdateBody: listingUpdateBody) { (response, error) in
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
 **listingId** | **UUID** |  | 
 **listingUpdateBody** | [**ListingUpdateBody**](ListingUpdateBody.md) |  | 

### Return type

[**ListingResponse**](ListingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

