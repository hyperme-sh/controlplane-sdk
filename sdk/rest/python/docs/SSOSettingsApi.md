# openapi_client.SSOSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sso_settings_api_v1_ssos_post**](SSOSettingsApi.md#create_sso_settings_api_v1_ssos_post) | **POST** /api/v1/ssos/ | Create Sso Settings
[**delete_sso_settings_api_v1_ssos_sso_id_delete**](SSOSettingsApi.md#delete_sso_settings_api_v1_ssos_sso_id_delete) | **DELETE** /api/v1/ssos/{sso_id} | Delete Sso Settings
[**get_available_sso_providers_api_v1_ssos_available_providers_get**](SSOSettingsApi.md#get_available_sso_providers_api_v1_ssos_available_providers_get) | **GET** /api/v1/ssos/available-providers | Get Available Sso Providers
[**get_sso_settings_by_id_api_v1_ssos_sso_id_get**](SSOSettingsApi.md#get_sso_settings_by_id_api_v1_ssos_sso_id_get) | **GET** /api/v1/ssos/{sso_id} | Get Sso Settings By Id
[**list_api_v1_ssos_get**](SSOSettingsApi.md#list_api_v1_ssos_get) | **GET** /api/v1/ssos/ | List
[**update_sso_settings_api_v1_ssos_sso_id_patch**](SSOSettingsApi.md#update_sso_settings_api_v1_ssos_sso_id_patch) | **PATCH** /api/v1/ssos/{sso_id} | Update Sso Settings


# **create_sso_settings_api_v1_ssos_post**
> SSOSettingsResponseDto create_sso_settings_api_v1_ssos_post(create_sso_settings_dto)

Create Sso Settings

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_sso_settings_dto import CreateSSOSettingsDto
from openapi_client.models.sso_settings_response_dto import SSOSettingsResponseDto
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
    api_instance = openapi_client.SSOSettingsApi(api_client)
    create_sso_settings_dto = openapi_client.CreateSSOSettingsDto() # CreateSSOSettingsDto | 

    try:
        # Create Sso Settings
        api_response = api_instance.create_sso_settings_api_v1_ssos_post(create_sso_settings_dto)
        print("The response of SSOSettingsApi->create_sso_settings_api_v1_ssos_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->create_sso_settings_api_v1_ssos_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sso_settings_dto** | [**CreateSSOSettingsDto**](CreateSSOSettingsDto.md)|  | 

### Return type

[**SSOSettingsResponseDto**](SSOSettingsResponseDto.md)

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

# **delete_sso_settings_api_v1_ssos_sso_id_delete**
> bool delete_sso_settings_api_v1_ssos_sso_id_delete(sso_id)

Delete Sso Settings

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
    api_instance = openapi_client.SSOSettingsApi(api_client)
    sso_id = 'sso_id_example' # str | 

    try:
        # Delete Sso Settings
        api_response = api_instance.delete_sso_settings_api_v1_ssos_sso_id_delete(sso_id)
        print("The response of SSOSettingsApi->delete_sso_settings_api_v1_ssos_sso_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->delete_sso_settings_api_v1_ssos_sso_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_id** | **str**|  | 

### Return type

**bool**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_sso_providers_api_v1_ssos_available_providers_get**
> List[object] get_available_sso_providers_api_v1_ssos_available_providers_get()

Get Available Sso Providers

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
    api_instance = openapi_client.SSOSettingsApi(api_client)

    try:
        # Get Available Sso Providers
        api_response = api_instance.get_available_sso_providers_api_v1_ssos_available_providers_get()
        print("The response of SSOSettingsApi->get_available_sso_providers_api_v1_ssos_available_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->get_available_sso_providers_api_v1_ssos_available_providers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

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

# **get_sso_settings_by_id_api_v1_ssos_sso_id_get**
> ReadSSOSettingsDto get_sso_settings_by_id_api_v1_ssos_sso_id_get(sso_id)

Get Sso Settings By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.read_sso_settings_dto import ReadSSOSettingsDto
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
    api_instance = openapi_client.SSOSettingsApi(api_client)
    sso_id = 'sso_id_example' # str | 

    try:
        # Get Sso Settings By Id
        api_response = api_instance.get_sso_settings_by_id_api_v1_ssos_sso_id_get(sso_id)
        print("The response of SSOSettingsApi->get_sso_settings_by_id_api_v1_ssos_sso_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->get_sso_settings_by_id_api_v1_ssos_sso_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_id** | **str**|  | 

### Return type

[**ReadSSOSettingsDto**](ReadSSOSettingsDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_v1_ssos_get**
> SSOSettingsListDto list_api_v1_ssos_get()

List

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.sso_settings_list_dto import SSOSettingsListDto
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
    api_instance = openapi_client.SSOSettingsApi(api_client)

    try:
        # List
        api_response = api_instance.list_api_v1_ssos_get()
        print("The response of SSOSettingsApi->list_api_v1_ssos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->list_api_v1_ssos_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SSOSettingsListDto**](SSOSettingsListDto.md)

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

# **update_sso_settings_api_v1_ssos_sso_id_patch**
> update_sso_settings_api_v1_ssos_sso_id_patch(sso_id, update_sso_settings_dto)

Update Sso Settings

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.update_sso_settings_dto import UpdateSSOSettingsDto
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
    api_instance = openapi_client.SSOSettingsApi(api_client)
    sso_id = 'sso_id_example' # str | 
    update_sso_settings_dto = openapi_client.UpdateSSOSettingsDto() # UpdateSSOSettingsDto | 

    try:
        # Update Sso Settings
        api_instance.update_sso_settings_api_v1_ssos_sso_id_patch(sso_id, update_sso_settings_dto)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->update_sso_settings_api_v1_ssos_sso_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_id** | **str**|  | 
 **update_sso_settings_dto** | [**UpdateSSOSettingsDto**](UpdateSSOSettingsDto.md)|  | 

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

