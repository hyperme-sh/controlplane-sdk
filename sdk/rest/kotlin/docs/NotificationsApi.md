# NotificationsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createNotificationBannerApiV1NotificationsBannerPost**](NotificationsApi.md#createNotificationBannerApiV1NotificationsBannerPost) | **POST** api/v1/notifications/banner | Create Notification Banner |
| [**getNotificationBannerApiV1NotificationsBannerGet**](NotificationsApi.md#getNotificationBannerApiV1NotificationsBannerGet) | **GET** api/v1/notifications/banner | Get Notification Banner |
| [**updateNotificationBannerApiV1NotificationsBannerIdPut**](NotificationsApi.md#updateNotificationBannerApiV1NotificationsBannerIdPut) | **PUT** api/v1/notifications/banner/{id} | Update Notification Banner |



Create Notification Banner

Create a new notification banner setting.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(NotificationsApi::class.java)
val createNotificationBannerSettingDto : CreateNotificationBannerSettingDto =  // CreateNotificationBannerSettingDto | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.createNotificationBannerApiV1NotificationsBannerPost(createNotificationBannerSettingDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createNotificationBannerSettingDto** | [**CreateNotificationBannerSettingDto**](CreateNotificationBannerSettingDto.md)|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Get Notification Banner

Get the current notification banner information.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(NotificationsApi::class.java)

launch(Dispatchers.IO) {
    val result : NotificationBannerSettingDto = webService.getNotificationBannerApiV1NotificationsBannerGet()
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


Update Notification Banner

Update an existing notification banner setting.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(NotificationsApi::class.java)
val id : kotlin.String = id_example // kotlin.String | 
val createNotificationBannerSettingDto : CreateNotificationBannerSettingDto =  // CreateNotificationBannerSettingDto | 

launch(Dispatchers.IO) {
    webService.updateNotificationBannerApiV1NotificationsBannerIdPut(id, createNotificationBannerSettingDto)
}
```

### Parameters
| **id** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createNotificationBannerSettingDto** | [**CreateNotificationBannerSettingDto**](CreateNotificationBannerSettingDto.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

