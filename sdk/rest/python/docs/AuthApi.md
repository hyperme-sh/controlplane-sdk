# openapi_client.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_callback_auth_callback_get**](AuthApi.md#auth_callback_auth_callback_get) | **GET** /auth/callback | OAuth2 authorization code callback
[**auth_login_auth_login_post**](AuthApi.md#auth_login_auth_login_post) | **POST** /auth/login | Start OIDC login
[**auth_me_auth_me_get**](AuthApi.md#auth_me_auth_me_get) | **GET** /auth/me | Auth Me
[**auth_refresh_auth_refresh_post**](AuthApi.md#auth_refresh_auth_refresh_post) | **POST** /auth/refresh | Refresh access token
[**auth_tenant_probe_auth_tenant_get**](AuthApi.md#auth_tenant_probe_auth_tenant_get) | **GET** /auth/tenant | Example route using get_current_tenant dependency


# **auth_callback_auth_callback_get**
> TokenBundleResponse auth_callback_auth_callback_get(code, state=state)

OAuth2 authorization code callback

### Example


```python
import openapi_client
from openapi_client.models.token_bundle_response import TokenBundleResponse
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
    api_instance = openapi_client.AuthApi(api_client)
    code = 'code_example' # str | 
    state = 'state_example' # str |  (optional)

    try:
        # OAuth2 authorization code callback
        api_response = api_instance.auth_callback_auth_callback_get(code, state=state)
        print("The response of AuthApi->auth_callback_auth_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_callback_auth_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **state** | **str**|  | [optional] 

### Return type

[**TokenBundleResponse**](TokenBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_login_auth_login_post**
> LoginStartResponse auth_login_auth_login_post(login_start_request=login_start_request)

Start OIDC login

Returns Keycloak authorization URL; optional identity_provider_hint selects broker (Google, Entra, GitHub, …).

### Example


```python
import openapi_client
from openapi_client.models.login_start_request import LoginStartRequest
from openapi_client.models.login_start_response import LoginStartResponse
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
    api_instance = openapi_client.AuthApi(api_client)
    login_start_request = openapi_client.LoginStartRequest() # LoginStartRequest |  (optional)

    try:
        # Start OIDC login
        api_response = api_instance.auth_login_auth_login_post(login_start_request=login_start_request)
        print("The response of AuthApi->auth_login_auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_login_auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_start_request** | [**LoginStartRequest**](LoginStartRequest.md)|  | [optional] 

### Return type

[**LoginStartResponse**](LoginStartResponse.md)

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

# **auth_me_auth_me_get**
> AuthMeResponse auth_me_auth_me_get()

Auth Me

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.auth_me_response import AuthMeResponse
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
    api_instance = openapi_client.AuthApi(api_client)

    try:
        # Auth Me
        api_response = api_instance.auth_me_auth_me_get()
        print("The response of AuthApi->auth_me_auth_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_me_auth_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthMeResponse**](AuthMeResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_refresh_auth_refresh_post**
> TokenBundleResponse auth_refresh_auth_refresh_post(refresh_token_request)

Refresh access token

### Example


```python
import openapi_client
from openapi_client.models.refresh_token_request import RefreshTokenRequest
from openapi_client.models.token_bundle_response import TokenBundleResponse
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
    api_instance = openapi_client.AuthApi(api_client)
    refresh_token_request = openapi_client.RefreshTokenRequest() # RefreshTokenRequest | 

    try:
        # Refresh access token
        api_response = api_instance.auth_refresh_auth_refresh_post(refresh_token_request)
        print("The response of AuthApi->auth_refresh_auth_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_refresh_auth_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | 

### Return type

[**TokenBundleResponse**](TokenBundleResponse.md)

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

# **auth_tenant_probe_auth_tenant_get**
> Dict[str, object] auth_tenant_probe_auth_tenant_get()

Example route using get_current_tenant dependency

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthApi(api_client)

    try:
        # Example route using get_current_tenant dependency
        api_response = api_instance.auth_tenant_probe_auth_tenant_get()
        print("The response of AuthApi->auth_tenant_probe_auth_tenant_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_tenant_probe_auth_tenant_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

