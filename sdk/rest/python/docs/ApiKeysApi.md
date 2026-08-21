# openapi_client.ApiKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key_api_v1_api_keys_post**](ApiKeysApi.md#create_api_key_api_v1_api_keys_post) | **POST** /api/v1/api-keys | Create Api Key
[**internal_validate_api_v1_internal_validate_post**](ApiKeysApi.md#internal_validate_api_v1_internal_validate_post) | **POST** /api/v1/internal/validate | Internal Validate
[**list_api_keys_api_v1_api_keys_get**](ApiKeysApi.md#list_api_keys_api_v1_api_keys_get) | **GET** /api/v1/api-keys | List Api Keys
[**revoke_api_key_api_v1_api_keys_key_id_delete**](ApiKeysApi.md#revoke_api_key_api_v1_api_keys_key_id_delete) | **DELETE** /api/v1/api-keys/{key_id} | Revoke Api Key


# **create_api_key_api_v1_api_keys_post**
> ApiKeyCreatedResponse create_api_key_api_v1_api_keys_post(api_key_create_request)

Create Api Key

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.api_key_create_request import ApiKeyCreateRequest
from openapi_client.models.api_key_created_response import ApiKeyCreatedResponse
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
    api_instance = openapi_client.ApiKeysApi(api_client)
    api_key_create_request = openapi_client.ApiKeyCreateRequest() # ApiKeyCreateRequest | 

    try:
        # Create Api Key
        api_response = api_instance.create_api_key_api_v1_api_keys_post(api_key_create_request)
        print("The response of ApiKeysApi->create_api_key_api_v1_api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->create_api_key_api_v1_api_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_create_request** | [**ApiKeyCreateRequest**](ApiKeyCreateRequest.md)|  | 

### Return type

[**ApiKeyCreatedResponse**](ApiKeyCreatedResponse.md)

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

# **internal_validate_api_v1_internal_validate_post**
> InternalValidateResponse internal_validate_api_v1_internal_validate_post(internal_validate_request, x_internal_token=x_internal_token)

Internal Validate

### Example


```python
import openapi_client
from openapi_client.models.internal_validate_request import InternalValidateRequest
from openapi_client.models.internal_validate_response import InternalValidateResponse
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
    api_instance = openapi_client.ApiKeysApi(api_client)
    internal_validate_request = openapi_client.InternalValidateRequest() # InternalValidateRequest | 
    x_internal_token = 'x_internal_token_example' # str |  (optional)

    try:
        # Internal Validate
        api_response = api_instance.internal_validate_api_v1_internal_validate_post(internal_validate_request, x_internal_token=x_internal_token)
        print("The response of ApiKeysApi->internal_validate_api_v1_internal_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->internal_validate_api_v1_internal_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_validate_request** | [**InternalValidateRequest**](InternalValidateRequest.md)|  | 
 **x_internal_token** | **str**|  | [optional] 

### Return type

[**InternalValidateResponse**](InternalValidateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys_api_v1_api_keys_get**
> List[ApiKeyResponse] list_api_keys_api_v1_api_keys_get()

List Api Keys

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.api_key_response import ApiKeyResponse
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
    api_instance = openapi_client.ApiKeysApi(api_client)

    try:
        # List Api Keys
        api_response = api_instance.list_api_keys_api_v1_api_keys_get()
        print("The response of ApiKeysApi->list_api_keys_api_v1_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->list_api_keys_api_v1_api_keys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiKeyResponse]**](ApiKeyResponse.md)

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

# **revoke_api_key_api_v1_api_keys_key_id_delete**
> revoke_api_key_api_v1_api_keys_key_id_delete(key_id)

Revoke Api Key

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
    api_instance = openapi_client.ApiKeysApi(api_client)
    key_id = 'key_id_example' # str | 

    try:
        # Revoke Api Key
        api_instance.revoke_api_key_api_v1_api_keys_key_id_delete(key_id)
    except Exception as e:
        print("Exception when calling ApiKeysApi->revoke_api_key_api_v1_api_keys_key_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

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

