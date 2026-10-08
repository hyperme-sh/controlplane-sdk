# PaymentsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocateBudgetApiV1BudgetsBudgetIdAllocatePost**](PaymentsAPI.md#allocatebudgetapiv1budgetsbudgetidallocatepost) | **POST** /api/v1/budgets/{budget_id}/allocate | Allocate Budget
[**apiV1BudgetsGet**](PaymentsAPI.md#apiv1budgetsget) | **GET** /api/v1/budgets | List crypto budgets
[**createCryptoBudgetApiV1BudgetsPost**](PaymentsAPI.md#createcryptobudgetapiv1budgetspost) | **POST** /api/v1/budgets | Create Crypto Budget
[**getCryptoBudgetApiV1BudgetsBudgetIdGet**](PaymentsAPI.md#getcryptobudgetapiv1budgetsbudgetidget) | **GET** /api/v1/budgets/{budget_id} | Get Crypto Budget
[**stripeWebhookApiV1PaymentsStripeWebhookPost**](PaymentsAPI.md#stripewebhookapiv1paymentsstripewebhookpost) | **POST** /api/v1/payments/stripe/webhook | Stripe Webhook


# **allocateBudgetApiV1BudgetsBudgetIdAllocatePost**
```swift
    open class func allocateBudgetApiV1BudgetsBudgetIdAllocatePost(budgetId: UUID, budgetAllocateRequest: BudgetAllocateRequest, completion: @escaping (_ data: CryptoBudgetResponse?, _ error: Error?) -> Void)
```

Allocate Budget

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let budgetId = 987 // UUID | 
let budgetAllocateRequest = BudgetAllocateRequest(deltaLamports: 123) // BudgetAllocateRequest | 

// Allocate Budget
PaymentsAPI.allocateBudgetApiV1BudgetsBudgetIdAllocatePost(budgetId: budgetId, budgetAllocateRequest: budgetAllocateRequest) { (response, error) in
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
 **budgetId** | **UUID** |  | 
 **budgetAllocateRequest** | [**BudgetAllocateRequest**](BudgetAllocateRequest.md) |  | 

### Return type

[**CryptoBudgetResponse**](CryptoBudgetResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiV1BudgetsGet**
```swift
    open class func apiV1BudgetsGet(limit: Int? = nil, offset: Int? = nil, completion: @escaping (_ data: CryptoBudgetListPage?, _ error: Error?) -> Void)
```

List crypto budgets

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let limit = 987 // Int |  (optional) (default to 50)
let offset = 987 // Int |  (optional) (default to 0)

// List crypto budgets
PaymentsAPI.apiV1BudgetsGet(limit: limit, offset: offset) { (response, error) in
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
 **limit** | **Int** |  | [optional] [default to 50]
 **offset** | **Int** |  | [optional] [default to 0]

### Return type

[**CryptoBudgetListPage**](CryptoBudgetListPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createCryptoBudgetApiV1BudgetsPost**
```swift
    open class func createCryptoBudgetApiV1BudgetsPost(cryptoBudgetCreateRequest: CryptoBudgetCreateRequest, completion: @escaping (_ data: CryptoBudgetResponse?, _ error: Error?) -> Void)
```

Create Crypto Budget

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let cryptoBudgetCreateRequest = CryptoBudgetCreateRequest(ceilingLamports: 123, mintPubkey: "mintPubkey_example", label: "label_example") // CryptoBudgetCreateRequest | 

// Create Crypto Budget
PaymentsAPI.createCryptoBudgetApiV1BudgetsPost(cryptoBudgetCreateRequest: cryptoBudgetCreateRequest) { (response, error) in
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
 **cryptoBudgetCreateRequest** | [**CryptoBudgetCreateRequest**](CryptoBudgetCreateRequest.md) |  | 

### Return type

[**CryptoBudgetResponse**](CryptoBudgetResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getCryptoBudgetApiV1BudgetsBudgetIdGet**
```swift
    open class func getCryptoBudgetApiV1BudgetsBudgetIdGet(budgetId: UUID, completion: @escaping (_ data: CryptoBudgetResponse?, _ error: Error?) -> Void)
```

Get Crypto Budget

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let budgetId = 987 // UUID | 

// Get Crypto Budget
PaymentsAPI.getCryptoBudgetApiV1BudgetsBudgetIdGet(budgetId: budgetId) { (response, error) in
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
 **budgetId** | **UUID** |  | 

### Return type

[**CryptoBudgetResponse**](CryptoBudgetResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stripeWebhookApiV1PaymentsStripeWebhookPost**
```swift
    open class func stripeWebhookApiV1PaymentsStripeWebhookPost(completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Stripe Webhook

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Stripe Webhook
PaymentsAPI.stripeWebhookApiV1PaymentsStripeWebhookPost() { (response, error) in
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

