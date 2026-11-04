# HealthAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthCheckApiV1HealthGet**](HealthAPI.md#healthcheckapiv1healthget) | **GET** /api/v1/health/ | Health Check


# **healthCheckApiV1HealthGet**
```swift
    open class func healthCheckApiV1HealthGet(completion: @escaping (_ data: HealthCheckResponseDto?, _ error: Error?) -> Void)
```

Health Check

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Health Check
HealthAPI.healthCheckApiV1HealthGet() { (response, error) in
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

[**HealthCheckResponseDto**](HealthCheckResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

