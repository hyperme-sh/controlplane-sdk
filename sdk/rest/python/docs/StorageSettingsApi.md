# openapi_client.StorageSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_storage_api_v1_storage_configure_post**](StorageSettingsApi.md#configure_storage_api_v1_storage_configure_post) | **POST** /api/v1/storage/configure | Configure Storage
[**get_available_providers_api_v1_storage_available_get**](StorageSettingsApi.md#get_available_providers_api_v1_storage_available_get) | **GET** /api/v1/storage/available | Get Available Providers
[**get_storage_settings_api_v1_storage_get**](StorageSettingsApi.md#get_storage_settings_api_v1_storage_get) | **GET** /api/v1/storage/ | Get Storage Settings
[**reset_storage_api_v1_storage_storage_id_reset_patch**](StorageSettingsApi.md#reset_storage_api_v1_storage_storage_id_reset_patch) | **PATCH** /api/v1/storage/{storage_id}/reset | Reset Storage


# **configure_storage_api_v1_storage_configure_post**
> object configure_storage_api_v1_storage_configure_post(storage_settings_dto)

Configure Storage

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.storage_settings_dto import StorageSettingsDto
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
    api_instance = openapi_client.StorageSettingsApi(api_client)
    storage_settings_dto = openapi_client.StorageSettingsDto() # StorageSettingsDto | 

    try:
        # Configure Storage
        api_response = api_instance.configure_storage_api_v1_storage_configure_post(storage_settings_dto)
        print("The response of StorageSettingsApi->configure_storage_api_v1_storage_configure_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSettingsApi->configure_storage_api_v1_storage_configure_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_settings_dto** | [**StorageSettingsDto**](StorageSettingsDto.md)|  | 

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

# **get_available_providers_api_v1_storage_available_get**
> List[Dict[str, str]] get_available_providers_api_v1_storage_available_get()

Get Available Providers

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
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
    api_instance = openapi_client.StorageSettingsApi(api_client)

    try:
        # Get Available Providers
        api_response = api_instance.get_available_providers_api_v1_storage_available_get()
        print("The response of StorageSettingsApi->get_available_providers_api_v1_storage_available_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSettingsApi->get_available_providers_api_v1_storage_available_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Dict[str, str]]**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_settings_api_v1_storage_get**
> List[AvailableStorageProviderDto] get_storage_settings_api_v1_storage_get()

Get Storage Settings

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.available_storage_provider_dto import AvailableStorageProviderDto
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
    api_instance = openapi_client.StorageSettingsApi(api_client)

    try:
        # Get Storage Settings
        api_response = api_instance.get_storage_settings_api_v1_storage_get()
        print("The response of StorageSettingsApi->get_storage_settings_api_v1_storage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSettingsApi->get_storage_settings_api_v1_storage_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AvailableStorageProviderDto]**](AvailableStorageProviderDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_storage_api_v1_storage_storage_id_reset_patch**
> reset_storage_api_v1_storage_storage_id_reset_patch(storage_id)

Reset Storage

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
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
    api_instance = openapi_client.StorageSettingsApi(api_client)
    storage_id = 'storage_id_example' # str | 

    try:
        # Reset Storage
        api_instance.reset_storage_api_v1_storage_storage_id_reset_patch(storage_id)
    except Exception as e:
        print("Exception when calling StorageSettingsApi->reset_storage_api_v1_storage_storage_id_reset_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

