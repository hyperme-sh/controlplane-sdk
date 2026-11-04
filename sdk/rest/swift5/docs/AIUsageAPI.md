# AIUsageAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1AiUsageHistoryGet**](AIUsageAPI.md#apiv1aiusagehistoryget) | **GET** /api/v1/ai/usage/history | List inference usage history
[**apiV1AiUsageSummaryGet**](AIUsageAPI.md#apiv1aiusagesummaryget) | **GET** /api/v1/ai/usage/summary | Tenant usage summary


# **apiV1AiUsageHistoryGet**
```swift
    open class func apiV1AiUsageHistoryGet(limit: Int? = nil, offset: Int? = nil, userId: UUID? = nil, completion: @escaping (_ data: InferenceHistoryPage?, _ error: Error?) -> Void)
```

List inference usage history

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let limit = 987 // Int |  (optional) (default to 50)
let offset = 987 // Int |  (optional) (default to 0)
let userId = 987 // UUID |  (optional)

// List inference usage history
AIUsageAPI.apiV1AiUsageHistoryGet(limit: limit, offset: offset, userId: userId) { (response, error) in
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
 **userId** | **UUID** |  | [optional] 

### Return type

[**InferenceHistoryPage**](InferenceHistoryPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiV1AiUsageSummaryGet**
```swift
    open class func apiV1AiUsageSummaryGet(completion: @escaping (_ data: TenantUsageSummaryResponse?, _ error: Error?) -> Void)
```

Tenant usage summary

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Tenant usage summary
AIUsageAPI.apiV1AiUsageSummaryGet() { (response, error) in
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

[**TenantUsageSummaryResponse**](TenantUsageSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

