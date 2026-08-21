# openapi_client.NotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_banner_api_v1_notifications_banner_post**](NotificationsApi.md#create_notification_banner_api_v1_notifications_banner_post) | **POST** /api/v1/notifications/banner | Create Notification Banner
[**get_notification_banner_api_v1_notifications_banner_get**](NotificationsApi.md#get_notification_banner_api_v1_notifications_banner_get) | **GET** /api/v1/notifications/banner | Get Notification Banner
[**update_notification_banner_api_v1_notifications_banner_id_put**](NotificationsApi.md#update_notification_banner_api_v1_notifications_banner_id_put) | **PUT** /api/v1/notifications/banner/{id} | Update Notification Banner


# **create_notification_banner_api_v1_notifications_banner_post**
> object create_notification_banner_api_v1_notifications_banner_post(create_notification_banner_setting_dto)

Create Notification Banner

Create a new notification banner setting.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_notification_banner_setting_dto import CreateNotificationBannerSettingDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotificationsApi(api_client)
    create_notification_banner_setting_dto = openapi_client.CreateNotificationBannerSettingDto() # CreateNotificationBannerSettingDto | 

    try:
        # Create Notification Banner
        api_response = api_instance.create_notification_banner_api_v1_notifications_banner_post(create_notification_banner_setting_dto)
        print("The response of NotificationsApi->create_notification_banner_api_v1_notifications_banner_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->create_notification_banner_api_v1_notifications_banner_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_notification_banner_setting_dto** | [**CreateNotificationBannerSettingDto**](CreateNotificationBannerSettingDto.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_banner_api_v1_notifications_banner_get**
> NotificationBannerSettingDto get_notification_banner_api_v1_notifications_banner_get()

Get Notification Banner

Get the current notification banner information.

### Example


```python
import openapi_client
from openapi_client.models.notification_banner_setting_dto import NotificationBannerSettingDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotificationsApi(api_client)

    try:
        # Get Notification Banner
        api_response = api_instance.get_notification_banner_api_v1_notifications_banner_get()
        print("The response of NotificationsApi->get_notification_banner_api_v1_notifications_banner_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_banner_api_v1_notifications_banner_get: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_banner_api_v1_notifications_banner_id_put**
> update_notification_banner_api_v1_notifications_banner_id_put(id, create_notification_banner_setting_dto)

Update Notification Banner

Update an existing notification banner setting.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_notification_banner_setting_dto import CreateNotificationBannerSettingDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotificationsApi(api_client)
    id = 'id_example' # str | 
    create_notification_banner_setting_dto = openapi_client.CreateNotificationBannerSettingDto() # CreateNotificationBannerSettingDto | 

    try:
        # Update Notification Banner
        api_instance.update_notification_banner_api_v1_notifications_banner_id_put(id, create_notification_banner_setting_dto)
    except Exception as e:
        print("Exception when calling NotificationsApi->update_notification_banner_api_v1_notifications_banner_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_notification_banner_setting_dto** | [**CreateNotificationBannerSettingDto**](CreateNotificationBannerSettingDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

