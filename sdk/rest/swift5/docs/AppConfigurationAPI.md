# AppConfigurationAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAppConfigurationApiV1AppConfigurationGet**](AppConfigurationAPI.md#getappconfigurationapiv1appconfigurationget) | **GET** /api/v1/app_configuration/ | Get App Configuration


# **getAppConfigurationApiV1AppConfigurationGet**
```swift
    open class func getAppConfigurationApiV1AppConfigurationGet(completion: @escaping (_ data: AppConfigurationDto?, _ error: Error?) -> Void)
```

Get App Configuration

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get App Configuration
AppConfigurationAPI.getAppConfigurationApiV1AppConfigurationGet() { (response, error) in
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

[**AppConfigurationDto**](AppConfigurationDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

