# PermissionsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPermissionsApiV1PermissionsGet**](PermissionsAPI.md#getpermissionsapiv1permissionsget) | **GET** /api/v1/permissions/ | Get Permissions


# **getPermissionsApiV1PermissionsGet**
```swift
    open class func getPermissionsApiV1PermissionsGet(completion: @escaping (_ data: [PermissionDto]?, _ error: Error?) -> Void)
```

Get Permissions

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get Permissions
PermissionsAPI.getPermissionsApiV1PermissionsGet() { (response, error) in
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

[**[PermissionDto]**](PermissionDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

