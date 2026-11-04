# NotificationsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNotificationBannerApiV1NotificationsBannerPost**](NotificationsAPI.md#createnotificationbannerapiv1notificationsbannerpost) | **POST** /api/v1/notifications/banner | Create Notification Banner
[**getNotificationBannerApiV1NotificationsBannerGet**](NotificationsAPI.md#getnotificationbannerapiv1notificationsbannerget) | **GET** /api/v1/notifications/banner | Get Notification Banner
[**updateNotificationBannerApiV1NotificationsBannerIdPut**](NotificationsAPI.md#updatenotificationbannerapiv1notificationsbanneridput) | **PUT** /api/v1/notifications/banner/{id} | Update Notification Banner


# **createNotificationBannerApiV1NotificationsBannerPost**
```swift
    open class func createNotificationBannerApiV1NotificationsBannerPost(createNotificationBannerSettingDto: CreateNotificationBannerSettingDto, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Create Notification Banner

Create a new notification banner setting.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let createNotificationBannerSettingDto = CreateNotificationBannerSettingDto(isEnabled: false, message: "message_example") // CreateNotificationBannerSettingDto | 

// Create Notification Banner
NotificationsAPI.createNotificationBannerApiV1NotificationsBannerPost(createNotificationBannerSettingDto: createNotificationBannerSettingDto) { (response, error) in
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
 **createNotificationBannerSettingDto** | [**CreateNotificationBannerSettingDto**](CreateNotificationBannerSettingDto.md) |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getNotificationBannerApiV1NotificationsBannerGet**
```swift
    open class func getNotificationBannerApiV1NotificationsBannerGet(completion: @escaping (_ data: NotificationBannerSettingDto?, _ error: Error?) -> Void)
```

Get Notification Banner

Get the current notification banner information.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get Notification Banner
NotificationsAPI.getNotificationBannerApiV1NotificationsBannerGet() { (response, error) in
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

[**NotificationBannerSettingDto**](NotificationBannerSettingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateNotificationBannerApiV1NotificationsBannerIdPut**
```swift
    open class func updateNotificationBannerApiV1NotificationsBannerIdPut(id: String, createNotificationBannerSettingDto: CreateNotificationBannerSettingDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Update Notification Banner

Update an existing notification banner setting.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let id = "id_example" // String | 
let createNotificationBannerSettingDto = CreateNotificationBannerSettingDto(isEnabled: false, message: "message_example") // CreateNotificationBannerSettingDto | 

// Update Notification Banner
NotificationsAPI.updateNotificationBannerApiV1NotificationsBannerIdPut(id: id, createNotificationBannerSettingDto: createNotificationBannerSettingDto) { (response, error) in
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
 **id** | **String** |  | 
 **createNotificationBannerSettingDto** | [**CreateNotificationBannerSettingDto**](CreateNotificationBannerSettingDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

