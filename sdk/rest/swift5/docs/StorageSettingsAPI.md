# StorageSettingsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureStorageApiV1StorageConfigurePost**](StorageSettingsAPI.md#configurestorageapiv1storageconfigurepost) | **POST** /api/v1/storage/configure | Configure Storage
[**getAvailableProvidersApiV1StorageAvailableGet**](StorageSettingsAPI.md#getavailableprovidersapiv1storageavailableget) | **GET** /api/v1/storage/available | Get Available Providers
[**getStorageSettingsApiV1StorageGet**](StorageSettingsAPI.md#getstoragesettingsapiv1storageget) | **GET** /api/v1/storage/ | Get Storage Settings
[**resetStorageApiV1StorageStorageIdResetPatch**](StorageSettingsAPI.md#resetstorageapiv1storagestorageidresetpatch) | **PATCH** /api/v1/storage/{storage_id}/reset | Reset Storage


# **configureStorageApiV1StorageConfigurePost**
```swift
    open class func configureStorageApiV1StorageConfigurePost(storageSettingsDto: StorageSettingsDto, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Configure Storage

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let storageSettingsDto = StorageSettingsDto(provider: "provider_example", isEnabled: false, region: "region_example", awsAccessKey: "awsAccessKey_example", awsSecretKey: "awsSecretKey_example", awsBucketName: "awsBucketName_example", azureConnectionString: "azureConnectionString_example", azureContainerName: "azureContainerName_example", updatedByUserId: "updatedByUserId_example") // StorageSettingsDto | 

// Configure Storage
StorageSettingsAPI.configureStorageApiV1StorageConfigurePost(storageSettingsDto: storageSettingsDto) { (response, error) in
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
 **storageSettingsDto** | [**StorageSettingsDto**](StorageSettingsDto.md) |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getAvailableProvidersApiV1StorageAvailableGet**
```swift
    open class func getAvailableProvidersApiV1StorageAvailableGet(completion: @escaping (_ data: [[String: String]]?, _ error: Error?) -> Void)
```

Get Available Providers

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get Available Providers
StorageSettingsAPI.getAvailableProvidersApiV1StorageAvailableGet() { (response, error) in
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

[**[[String: String]]**](Dictionary.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getStorageSettingsApiV1StorageGet**
```swift
    open class func getStorageSettingsApiV1StorageGet(completion: @escaping (_ data: [AvailableStorageProviderDto]?, _ error: Error?) -> Void)
```

Get Storage Settings

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get Storage Settings
StorageSettingsAPI.getStorageSettingsApiV1StorageGet() { (response, error) in
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

[**[AvailableStorageProviderDto]**](AvailableStorageProviderDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resetStorageApiV1StorageStorageIdResetPatch**
```swift
    open class func resetStorageApiV1StorageStorageIdResetPatch(storageId: String, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Reset Storage

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let storageId = "storageId_example" // String | 

// Reset Storage
StorageSettingsAPI.resetStorageApiV1StorageStorageIdResetPatch(storageId: storageId) { (response, error) in
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
 **storageId** | **String** |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

