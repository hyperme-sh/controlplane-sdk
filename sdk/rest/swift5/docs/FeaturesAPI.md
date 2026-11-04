# FeaturesAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listFeaturesApiV1FeaturesGet**](FeaturesAPI.md#listfeaturesapiv1featuresget) | **GET** /api/v1/features/ | List Features


# **listFeaturesApiV1FeaturesGet**
```swift
    open class func listFeaturesApiV1FeaturesGet(completion: @escaping (_ data: [Feature]?, _ error: Error?) -> Void)
```

List Features

List all available features. Requires HOST_MANAGE_TENANTS permission.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// List Features
FeaturesAPI.listFeaturesApiV1FeaturesGet() { (response, error) in
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

[**[Feature]**](Feature.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

