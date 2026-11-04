# openapi_client.AIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ask_ai_api_v1_ai_ask_post**](AIApi.md#ask_ai_api_v1_ai_ask_post) | **POST** /api/v1/ai/ask | Ask Ai
[**complete_api_v1_ai_complete_post**](AIApi.md#complete_api_v1_ai_complete_post) | **POST** /api/v1/ai/complete | Complete
[**create_new_session_api_v1_ai_new_session_get**](AIApi.md#create_new_session_api_v1_ai_new_session_get) | **GET** /api/v1/ai/new_session | Create New Session
[**delete_session_api_v1_ai_sessions_session_id_delete**](AIApi.md#delete_session_api_v1_ai_sessions_session_id_delete) | **DELETE** /api/v1/ai/sessions/{session_id} | Delete Session
[**get_history_api_v1_ai_history_get**](AIApi.md#get_history_api_v1_ai_history_get) | **GET** /api/v1/ai/history | Get History
[**get_models_api_v1_ai_models_get**](AIApi.md#get_models_api_v1_ai_models_get) | **GET** /api/v1/ai/models | Get Models
[**get_single_session_api_v1_ai_sessions_session_id_get**](AIApi.md#get_single_session_api_v1_ai_sessions_session_id_get) | **GET** /api/v1/ai/sessions/{session_id} | Get Single Session
[**inference_api_v1_ai_inference_post**](AIApi.md#inference_api_v1_ai_inference_post) | **POST** /api/v1/ai/inference | Inference
[**set_preferred_model_api_v1_ai_set_model_preference_model_name_put**](AIApi.md#set_preferred_model_api_v1_ai_set_model_preference_model_name_put) | **PUT** /api/v1/ai/set_model_preference/{model_name} | Set Preferred Model


# **ask_ai_api_v1_ai_ask_post**
> object ask_ai_api_v1_ai_ask_post(ai_ask_request_dto)

Ask Ai

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.ai_ask_request_dto import AIAskRequestDto
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
    api_instance = openapi_client.AIApi(api_client)
    ai_ask_request_dto = openapi_client.AIAskRequestDto() # AIAskRequestDto | 

    try:
        # Ask Ai
        api_response = api_instance.ask_ai_api_v1_ai_ask_post(ai_ask_request_dto)
        print("The response of AIApi->ask_ai_api_v1_ai_ask_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->ask_ai_api_v1_ai_ask_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_ask_request_dto** | [**AIAskRequestDto**](AIAskRequestDto.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_api_v1_ai_complete_post**
> InferenceResponse complete_api_v1_ai_complete_post(inference_request)

Complete

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.inference_request import InferenceRequest
from openapi_client.models.inference_response import InferenceResponse
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AIApi(api_client)
    inference_request = openapi_client.InferenceRequest() # InferenceRequest | 

    try:
        # Complete
        api_response = api_instance.complete_api_v1_ai_complete_post(inference_request)
        print("The response of AIApi->complete_api_v1_ai_complete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->complete_api_v1_ai_complete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inference_request** | [**InferenceRequest**](InferenceRequest.md)|  | 

### Return type

[**InferenceResponse**](InferenceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_session_api_v1_ai_new_session_get**
> NewSessionResponseDto create_new_session_api_v1_ai_new_session_get()

Create New Session

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.new_session_response_dto import NewSessionResponseDto
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
    api_instance = openapi_client.AIApi(api_client)

    try:
        # Create New Session
        api_response = api_instance.create_new_session_api_v1_ai_new_session_get()
        print("The response of AIApi->create_new_session_api_v1_ai_new_session_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->create_new_session_api_v1_ai_new_session_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NewSessionResponseDto**](NewSessionResponseDto.md)

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

# **delete_session_api_v1_ai_sessions_session_id_delete**
> object delete_session_api_v1_ai_sessions_session_id_delete(session_id)

Delete Session

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
    api_instance = openapi_client.AIApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Delete Session
        api_response = api_instance.delete_session_api_v1_ai_sessions_session_id_delete(session_id)
        print("The response of AIApi->delete_session_api_v1_ai_sessions_session_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->delete_session_api_v1_ai_sessions_session_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_api_v1_ai_history_get**
> List[AISessionByUserIdDto] get_history_api_v1_ai_history_get()

Get History

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.ai_session_by_user_id_dto import AISessionByUserIdDto
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
    api_instance = openapi_client.AIApi(api_client)

    try:
        # Get History
        api_response = api_instance.get_history_api_v1_ai_history_get()
        print("The response of AIApi->get_history_api_v1_ai_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->get_history_api_v1_ai_history_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AISessionByUserIdDto]**](AISessionByUserIdDto.md)

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

# **get_models_api_v1_ai_models_get**
> List[AIModelInfoDto] get_models_api_v1_ai_models_get()

Get Models

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.ai_model_info_dto import AIModelInfoDto
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
    api_instance = openapi_client.AIApi(api_client)

    try:
        # Get Models
        api_response = api_instance.get_models_api_v1_ai_models_get()
        print("The response of AIApi->get_models_api_v1_ai_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->get_models_api_v1_ai_models_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AIModelInfoDto]**](AIModelInfoDto.md)

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

# **get_single_session_api_v1_ai_sessions_session_id_get**
> List[AIHistoriesDto] get_single_session_api_v1_ai_sessions_session_id_get(session_id)

Get Single Session

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.ai_histories_dto import AIHistoriesDto
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
    api_instance = openapi_client.AIApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Get Single Session
        api_response = api_instance.get_single_session_api_v1_ai_sessions_session_id_get(session_id)
        print("The response of AIApi->get_single_session_api_v1_ai_sessions_session_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->get_single_session_api_v1_ai_sessions_session_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**List[AIHistoriesDto]**](AIHistoriesDto.md)

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

# **inference_api_v1_ai_inference_post**
> InferenceResponse inference_api_v1_ai_inference_post(inference_request)

Inference

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.inference_request import InferenceRequest
from openapi_client.models.inference_response import InferenceResponse
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AIApi(api_client)
    inference_request = openapi_client.InferenceRequest() # InferenceRequest | 

    try:
        # Inference
        api_response = api_instance.inference_api_v1_ai_inference_post(inference_request)
        print("The response of AIApi->inference_api_v1_ai_inference_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->inference_api_v1_ai_inference_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inference_request** | [**InferenceRequest**](InferenceRequest.md)|  | 

### Return type

[**InferenceResponse**](InferenceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_preferred_model_api_v1_ai_set_model_preference_model_name_put**
> set_preferred_model_api_v1_ai_set_model_preference_model_name_put(model_name)

Set Preferred Model

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
    api_instance = openapi_client.AIApi(api_client)
    model_name = 'model_name_example' # str | 

    try:
        # Set Preferred Model
        api_instance.set_preferred_model_api_v1_ai_set_model_preference_model_name_put(model_name)
    except Exception as e:
        print("Exception when calling AIApi->set_preferred_model_api_v1_ai_set_model_preference_model_name_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**|  | 

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

