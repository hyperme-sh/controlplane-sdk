# StripePricingAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPricingApiV1PricesPost**](StripePricingAPI.md#createpricingapiv1pricespost) | **POST** /api/v1/prices/ | Create Pricing
[**getPricingListApiV1PricesGet**](StripePricingAPI.md#getpricinglistapiv1pricesget) | **GET** /api/v1/prices/ | Get Pricing List
[**updatePricingApiV1PricesPriceIdPatch**](StripePricingAPI.md#updatepricingapiv1pricespriceidpatch) | **PATCH** /api/v1/prices/{price_id} | Update Pricing


# **createPricingApiV1PricesPost**
```swift
    open class func createPricingApiV1PricesPost(createPricingDto: CreatePricingDto, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Create Pricing

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let createPricingDto = CreatePricingDto(currency: "currency_example", unitAmount: 123, product: "product_example", active: false, recurring: RecurringDto(interval: "interval_example", intervalCount: 123, usageType: "usageType_example")) // CreatePricingDto | 

// Create Pricing
StripePricingAPI.createPricingApiV1PricesPost(createPricingDto: createPricingDto) { (response, error) in
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
 **createPricingDto** | [**CreatePricingDto**](CreatePricingDto.md) |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getPricingListApiV1PricesGet**
```swift
    open class func getPricingListApiV1PricesGet(completion: @escaping (_ data: PricingListDto?, _ error: Error?) -> Void)
```

Get Pricing List

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get Pricing List
StripePricingAPI.getPricingListApiV1PricesGet() { (response, error) in
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

[**PricingListDto**](PricingListDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatePricingApiV1PricesPriceIdPatch**
```swift
    open class func updatePricingApiV1PricesPriceIdPatch(priceId: String, updatePricingDto: UpdatePricingDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Update Pricing

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let priceId = "priceId_example" // String | 
let updatePricingDto = UpdatePricingDto(active: false, metadata: "TODO", taxBehavior: "taxBehavior_example") // UpdatePricingDto | 

// Update Pricing
StripePricingAPI.updatePricingApiV1PricesPriceIdPatch(priceId: priceId, updatePricingDto: updatePricingDto) { (response, error) in
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
 **priceId** | **String** |  | 
 **updatePricingDto** | [**UpdatePricingDto**](UpdatePricingDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

