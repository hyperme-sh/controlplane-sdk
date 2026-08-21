# StripeCheckoutAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createHostCheckoutSessionApiV1CheckoutsHostTenantIdTenantPost**](StripeCheckoutAPI.md#createhostcheckoutsessionapiv1checkoutshosttenantidtenantpost) | **POST** /api/v1/checkouts/host/{tenant_id}/tenant | Create Host Checkout Session
[**createTenantCheckoutSessionApiV1CheckoutsTenantSubscriptionPost**](StripeCheckoutAPI.md#createtenantcheckoutsessionapiv1checkoutstenantsubscriptionpost) | **POST** /api/v1/checkouts/tenant/subscription | Create Tenant Checkout Session
[**hostCheckoutSuccessApiV1CheckoutsHostPaymentCancelPost**](StripeCheckoutAPI.md#hostcheckoutsuccessapiv1checkoutshostpaymentcancelpost) | **POST** /api/v1/checkouts/host/payment/cancel | Host Checkout Success
[**hostCheckoutSuccessApiV1CheckoutsHostPaymentSuccessPost**](StripeCheckoutAPI.md#hostcheckoutsuccessapiv1checkoutshostpaymentsuccesspost) | **POST** /api/v1/checkouts/host/payment/success | Host Checkout Success
[**listCheckoutRecordsApiV1CheckoutsAllGet**](StripeCheckoutAPI.md#listcheckoutrecordsapiv1checkoutsallget) | **GET** /api/v1/checkouts/all | List Checkout Records
[**tenantCheckoutCanceledApiV1CheckoutsTenantPaymentCancelPost**](StripeCheckoutAPI.md#tenantcheckoutcanceledapiv1checkoutstenantpaymentcancelpost) | **POST** /api/v1/checkouts/tenant/payment/cancel | Tenant Checkout Canceled
[**tenantCheckoutSuccessApiV1CheckoutsTenantPaymentSuccessPost**](StripeCheckoutAPI.md#tenantcheckoutsuccessapiv1checkoutstenantpaymentsuccesspost) | **POST** /api/v1/checkouts/tenant/payment/success | Tenant Checkout Success


# **createHostCheckoutSessionApiV1CheckoutsHostTenantIdTenantPost**
```swift
    open class func createHostCheckoutSessionApiV1CheckoutsHostTenantIdTenantPost(checkoutRequestDto: CheckoutRequestDto, completion: @escaping (_ data: CheckoutResponseDto?, _ error: Error?) -> Void)
```

Create Host Checkout Session

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let checkoutRequestDto = CheckoutRequestDto(priceId: "priceId_example", tenantId: "tenantId_example", mode: "mode_example", email: "email_example") // CheckoutRequestDto | 

// Create Host Checkout Session
StripeCheckoutAPI.createHostCheckoutSessionApiV1CheckoutsHostTenantIdTenantPost(checkoutRequestDto: checkoutRequestDto) { (response, error) in
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
 **checkoutRequestDto** | [**CheckoutRequestDto**](CheckoutRequestDto.md) |  | 

### Return type

[**CheckoutResponseDto**](CheckoutResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createTenantCheckoutSessionApiV1CheckoutsTenantSubscriptionPost**
```swift
    open class func createTenantCheckoutSessionApiV1CheckoutsTenantSubscriptionPost(checkoutRequestDto: CheckoutRequestDto, completion: @escaping (_ data: CheckoutResponseDto?, _ error: Error?) -> Void)
```

Create Tenant Checkout Session

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let checkoutRequestDto = CheckoutRequestDto(priceId: "priceId_example", tenantId: "tenantId_example", mode: "mode_example", email: "email_example") // CheckoutRequestDto | 

// Create Tenant Checkout Session
StripeCheckoutAPI.createTenantCheckoutSessionApiV1CheckoutsTenantSubscriptionPost(checkoutRequestDto: checkoutRequestDto) { (response, error) in
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
 **checkoutRequestDto** | [**CheckoutRequestDto**](CheckoutRequestDto.md) |  | 

### Return type

[**CheckoutResponseDto**](CheckoutResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hostCheckoutSuccessApiV1CheckoutsHostPaymentCancelPost**
```swift
    open class func hostCheckoutSuccessApiV1CheckoutsHostPaymentCancelPost(tenantId: String, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Host Checkout Success

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let tenantId = "tenantId_example" // String | 

// Host Checkout Success
StripeCheckoutAPI.hostCheckoutSuccessApiV1CheckoutsHostPaymentCancelPost(tenantId: tenantId) { (response, error) in
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
 **tenantId** | **String** |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hostCheckoutSuccessApiV1CheckoutsHostPaymentSuccessPost**
```swift
    open class func hostCheckoutSuccessApiV1CheckoutsHostPaymentSuccessPost(sessionId: String, tenantId: String, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Host Checkout Success

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let sessionId = "sessionId_example" // String | 
let tenantId = "tenantId_example" // String | 

// Host Checkout Success
StripeCheckoutAPI.hostCheckoutSuccessApiV1CheckoutsHostPaymentSuccessPost(sessionId: sessionId, tenantId: tenantId) { (response, error) in
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
 **sessionId** | **String** |  | 
 **tenantId** | **String** |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listCheckoutRecordsApiV1CheckoutsAllGet**
```swift
    open class func listCheckoutRecordsApiV1CheckoutsAllGet(skip: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: BillingRecordListDto?, _ error: Error?) -> Void)
```

List Checkout Records

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let skip = 987 // Int |  (optional) (default to 0)
let limit = 987 // Int |  (optional) (default to 100)

// List Checkout Records
StripeCheckoutAPI.listCheckoutRecordsApiV1CheckoutsAllGet(skip: skip, limit: limit) { (response, error) in
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
 **skip** | **Int** |  | [optional] [default to 0]
 **limit** | **Int** |  | [optional] [default to 100]

### Return type

[**BillingRecordListDto**](BillingRecordListDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenantCheckoutCanceledApiV1CheckoutsTenantPaymentCancelPost**
```swift
    open class func tenantCheckoutCanceledApiV1CheckoutsTenantPaymentCancelPost(completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Tenant Checkout Canceled

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Tenant Checkout Canceled
StripeCheckoutAPI.tenantCheckoutCanceledApiV1CheckoutsTenantPaymentCancelPost() { (response, error) in
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

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenantCheckoutSuccessApiV1CheckoutsTenantPaymentSuccessPost**
```swift
    open class func tenantCheckoutSuccessApiV1CheckoutsTenantPaymentSuccessPost(sessionId: String, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Tenant Checkout Success

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let sessionId = "sessionId_example" // String | 

// Tenant Checkout Success
StripeCheckoutAPI.tenantCheckoutSuccessApiV1CheckoutsTenantPaymentSuccessPost(sessionId: sessionId) { (response, error) in
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
 **sessionId** | **String** |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

