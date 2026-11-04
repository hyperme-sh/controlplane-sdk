# openapi_client.AccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_email_api_v1_account_change_email_request_patch**](AccountApi.md#change_email_api_v1_account_change_email_request_patch) | **PATCH** /api/v1/account/change_email_request | Change Email
[**change_email_confirmation_api_v1_account_change_email_confirmation_patch**](AccountApi.md#change_email_confirmation_api_v1_account_change_email_confirmation_patch) | **PATCH** /api/v1/account/change_email_confirmation | Change Email Confirmation
[**logout_api_v1_account_logout_get**](AccountApi.md#logout_api_v1_account_logout_get) | **GET** /api/v1/account/logout | Logout
[**read_users_me_api_v1_account_me_get**](AccountApi.md#read_users_me_api_v1_account_me_get) | **GET** /api/v1/account/me | Read Users Me
[**resend_activation_email_api_v1_account_resend_activation_email_post**](AccountApi.md#resend_activation_email_api_v1_account_resend_activation_email_post) | **POST** /api/v1/account/resend_activation_email | Resend Activation Email


# **change_email_api_v1_account_change_email_request_patch**
> object change_email_api_v1_account_change_email_request_patch(change_email_request_dto)

Change Email

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.change_email_request_dto import ChangeEmailRequestDto
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
    api_instance = openapi_client.AccountApi(api_client)
    change_email_request_dto = openapi_client.ChangeEmailRequestDto() # ChangeEmailRequestDto | 

    try:
        # Change Email
        api_response = api_instance.change_email_api_v1_account_change_email_request_patch(change_email_request_dto)
        print("The response of AccountApi->change_email_api_v1_account_change_email_request_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->change_email_api_v1_account_change_email_request_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_email_request_dto** | [**ChangeEmailRequestDto**](ChangeEmailRequestDto.md)|  | 

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
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_email_confirmation_api_v1_account_change_email_confirmation_patch**
> ChangeEmailResponseDto change_email_confirmation_api_v1_account_change_email_confirmation_patch(change_email_confirm_request_dto)

Change Email Confirmation

### Example


```python
import openapi_client
from openapi_client.models.change_email_confirm_request_dto import ChangeEmailConfirmRequestDto
from openapi_client.models.change_email_response_dto import ChangeEmailResponseDto
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
    api_instance = openapi_client.AccountApi(api_client)
    change_email_confirm_request_dto = openapi_client.ChangeEmailConfirmRequestDto() # ChangeEmailConfirmRequestDto | 

    try:
        # Change Email Confirmation
        api_response = api_instance.change_email_confirmation_api_v1_account_change_email_confirmation_patch(change_email_confirm_request_dto)
        print("The response of AccountApi->change_email_confirmation_api_v1_account_change_email_confirmation_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->change_email_confirmation_api_v1_account_change_email_confirmation_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_email_confirm_request_dto** | [**ChangeEmailConfirmRequestDto**](ChangeEmailConfirmRequestDto.md)|  | 

### Return type

[**ChangeEmailResponseDto**](ChangeEmailResponseDto.md)

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

# **logout_api_v1_account_logout_get**
> object logout_api_v1_account_logout_get()

Logout

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
    api_instance = openapi_client.AccountApi(api_client)

    try:
        # Logout
        api_response = api_instance.logout_api_v1_account_logout_get()
        print("The response of AccountApi->logout_api_v1_account_logout_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->logout_api_v1_account_logout_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_users_me_api_v1_account_me_get**
> MeResponseDto read_users_me_api_v1_account_me_get()

Read Users Me

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.me_response_dto import MeResponseDto
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
    api_instance = openapi_client.AccountApi(api_client)

    try:
        # Read Users Me
        api_response = api_instance.read_users_me_api_v1_account_me_get()
        print("The response of AccountApi->read_users_me_api_v1_account_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->read_users_me_api_v1_account_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MeResponseDto**](MeResponseDto.md)

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

# **resend_activation_email_api_v1_account_resend_activation_email_post**
> resend_activation_email_api_v1_account_resend_activation_email_post()

Resend Activation Email

Removed: activation is handled by Keycloak.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.AccountApi(api_client)

    try:
        # Resend Activation Email
        api_instance.resend_activation_email_api_v1_account_resend_activation_email_post()
    except Exception as e:
        print("Exception when calling AccountApi->resend_activation_email_api_v1_account_resend_activation_email_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

