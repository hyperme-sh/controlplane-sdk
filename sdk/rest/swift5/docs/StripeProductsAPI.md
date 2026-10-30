# StripeProductsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProductApiV1ProductsPost**](StripeProductsAPI.md#createproductapiv1productspost) | **POST** /api/v1/products/ | Create a Product
[**deleteProductApiV1ProductsProductIdDelete**](StripeProductsAPI.md#deleteproductapiv1productsproductiddelete) | **DELETE** /api/v1/products/{product_id} | Delete a Product
[**getProductByIdApiV1ProductsProductIdGet**](StripeProductsAPI.md#getproductbyidapiv1productsproductidget) | **GET** /api/v1/products/{product_id} | Get Product by ID
[**listProductsApiV1ProductsGet**](StripeProductsAPI.md#listproductsapiv1productsget) | **GET** /api/v1/products/ | List Products
[**updateProductApiV1ProductsProductIdPatch**](StripeProductsAPI.md#updateproductapiv1productsproductidpatch) | **PATCH** /api/v1/products/{product_id} | Update a Product


# **createProductApiV1ProductsPost**
```swift
    open class func createProductApiV1ProductsPost(createProductDto: CreateProductDto, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Create a Product

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let createProductDto = CreateProductDto(name: "name_example", description: "description_example", taxCode: "taxCode_example", active: false) // CreateProductDto | 

// Create a Product
StripeProductsAPI.createProductApiV1ProductsPost(createProductDto: createProductDto) { (response, error) in
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
 **createProductDto** | [**CreateProductDto**](CreateProductDto.md) |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteProductApiV1ProductsProductIdDelete**
```swift
    open class func deleteProductApiV1ProductsProductIdDelete(productId: String, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Delete a Product

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let productId = "productId_example" // String | 

// Delete a Product
StripeProductsAPI.deleteProductApiV1ProductsProductIdDelete(productId: productId) { (response, error) in
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
 **productId** | **String** |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getProductByIdApiV1ProductsProductIdGet**
```swift
    open class func getProductByIdApiV1ProductsProductIdGet(productId: String, completion: @escaping (_ data: ProductDto?, _ error: Error?) -> Void)
```

Get Product by ID

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let productId = "productId_example" // String | 

// Get Product by ID
StripeProductsAPI.getProductByIdApiV1ProductsProductIdGet(productId: productId) { (response, error) in
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
 **productId** | **String** |  | 

### Return type

[**ProductDto**](ProductDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listProductsApiV1ProductsGet**
```swift
    open class func listProductsApiV1ProductsGet(active: Bool? = nil, completion: @escaping (_ data: ProductListDto?, _ error: Error?) -> Void)
```

List Products

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let active = true // Bool | Filter active products, defaults to True (optional) (default to true)

// List Products
StripeProductsAPI.listProductsApiV1ProductsGet(active: active) { (response, error) in
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
 **active** | **Bool** | Filter active products, defaults to True | [optional] [default to true]

### Return type

[**ProductListDto**](ProductListDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateProductApiV1ProductsProductIdPatch**
```swift
    open class func updateProductApiV1ProductsProductIdPatch(productId: String, createProductDto: CreateProductDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Update a Product

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let productId = "productId_example" // String | 
let createProductDto = CreateProductDto(name: "name_example", description: "description_example", taxCode: "taxCode_example", active: false) // CreateProductDto | 

// Update a Product
StripeProductsAPI.updateProductApiV1ProductsProductIdPatch(productId: productId, createProductDto: createProductDto) { (response, error) in
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
 **productId** | **String** |  | 
 **createProductDto** | [**CreateProductDto**](CreateProductDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

