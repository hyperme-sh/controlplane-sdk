# StripeBillingAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPlanApiV1BillingPlansPost**](StripeBillingAPI.md#createplanapiv1billingplanspost) | **POST** /api/v1/billing/plans | Create a new plan
[**deletePlanApiV1BillingPlansPlanIdDelete**](StripeBillingAPI.md#deleteplanapiv1billingplansplaniddelete) | **DELETE** /api/v1/billing/plans/{plan_id} | Delete existing plan
[**getPlanApiV1BillingPlansPlanIdGet**](StripeBillingAPI.md#getplanapiv1billingplansplanidget) | **GET** /api/v1/billing/plans/{plan_id} | Retrieve a plan details
[**listPlansApiV1BillingPlansGet**](StripeBillingAPI.md#listplansapiv1billingplansget) | **GET** /api/v1/billing/plans | List available plans
[**updatePlanApiV1BillingPlansPlanIdPatch**](StripeBillingAPI.md#updateplanapiv1billingplansplanidpatch) | **PATCH** /api/v1/billing/plans/{plan_id} | Update a existing plan


# **createPlanApiV1BillingPlansPost**
```swift
    open class func createPlanApiV1BillingPlansPost(createPlanDto: CreatePlanDto, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Create a new plan

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let createPlanDto = CreatePlanDto(currency: "currency_example", interval: "interval_example", productId: "productId_example", amount: 123) // CreatePlanDto | 

// Create a new plan
StripeBillingAPI.createPlanApiV1BillingPlansPost(createPlanDto: createPlanDto) { (response, error) in
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
 **createPlanDto** | [**CreatePlanDto**](CreatePlanDto.md) |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletePlanApiV1BillingPlansPlanIdDelete**
```swift
    open class func deletePlanApiV1BillingPlansPlanIdDelete(planId: String, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Delete existing plan

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let planId = "planId_example" // String | 

// Delete existing plan
StripeBillingAPI.deletePlanApiV1BillingPlansPlanIdDelete(planId: planId) { (response, error) in
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
 **planId** | **String** |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getPlanApiV1BillingPlansPlanIdGet**
```swift
    open class func getPlanApiV1BillingPlansPlanIdGet(planId: String, completion: @escaping (_ data: PlanDto?, _ error: Error?) -> Void)
```

Retrieve a plan details

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let planId = "planId_example" // String | 

// Retrieve a plan details
StripeBillingAPI.getPlanApiV1BillingPlansPlanIdGet(planId: planId) { (response, error) in
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
 **planId** | **String** |  | 

### Return type

[**PlanDto**](PlanDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listPlansApiV1BillingPlansGet**
```swift
    open class func listPlansApiV1BillingPlansGet(completion: @escaping (_ data: PlanListDto?, _ error: Error?) -> Void)
```

List available plans

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// List available plans
StripeBillingAPI.listPlansApiV1BillingPlansGet() { (response, error) in
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

[**PlanListDto**](PlanListDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatePlanApiV1BillingPlansPlanIdPatch**
```swift
    open class func updatePlanApiV1BillingPlansPlanIdPatch(planId: String, updatePlanDto: UpdatePlanDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Update a existing plan

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let planId = "planId_example" // String | 
let updatePlanDto = UpdatePlanDto(trialPeriodDays: 123, active: false, metadata: "TODO") // UpdatePlanDto | 

// Update a existing plan
StripeBillingAPI.updatePlanApiV1BillingPlansPlanIdPatch(planId: planId, updatePlanDto: updatePlanDto) { (response, error) in
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
 **planId** | **String** |  | 
 **updatePlanDto** | [**UpdatePlanDto**](UpdatePlanDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

