# DashboardAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDashboardMetricsApiV1DashboardGet**](DashboardAPI.md#getdashboardmetricsapiv1dashboardget) | **GET** /api/v1/dashboard/ | Get Dashboard Metrics


# **getDashboardMetricsApiV1DashboardGet**
```swift
    open class func getDashboardMetricsApiV1DashboardGet(filter: Filter_getDashboardMetricsApiV1DashboardGet? = nil, completion: @escaping (_ data: DashboardMetricsDto?, _ error: Error?) -> Void)
```

Get Dashboard Metrics

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let filter = "filter_example" // String |  (optional) (default to .all)

// Get Dashboard Metrics
DashboardAPI.getDashboardMetricsApiV1DashboardGet(filter: filter) { (response, error) in
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
 **filter** | **String** |  | [optional] [default to .all]

### Return type

[**DashboardMetricsDto**](DashboardMetricsDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

