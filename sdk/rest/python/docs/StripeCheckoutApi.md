# openapi_client.StripeCheckoutApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_host_checkout_session_api_v1_checkouts_host_tenant_id_tenant_post**](StripeCheckoutApi.md#create_host_checkout_session_api_v1_checkouts_host_tenant_id_tenant_post) | **POST** /api/v1/checkouts/host/{tenant_id}/tenant | Create Host Checkout Session
[**create_tenant_checkout_session_api_v1_checkouts_tenant_subscription_post**](StripeCheckoutApi.md#create_tenant_checkout_session_api_v1_checkouts_tenant_subscription_post) | **POST** /api/v1/checkouts/tenant/subscription | Create Tenant Checkout Session
[**host_checkout_success_api_v1_checkouts_host_payment_cancel_post**](StripeCheckoutApi.md#host_checkout_success_api_v1_checkouts_host_payment_cancel_post) | **POST** /api/v1/checkouts/host/payment/cancel | Host Checkout Success
[**host_checkout_success_api_v1_checkouts_host_payment_success_post**](StripeCheckoutApi.md#host_checkout_success_api_v1_checkouts_host_payment_success_post) | **POST** /api/v1/checkouts/host/payment/success | Host Checkout Success
[**list_checkout_records_api_v1_checkouts_all_get**](StripeCheckoutApi.md#list_checkout_records_api_v1_checkouts_all_get) | **GET** /api/v1/checkouts/all | List Checkout Records
[**tenant_checkout_canceled_api_v1_checkouts_tenant_payment_cancel_post**](StripeCheckoutApi.md#tenant_checkout_canceled_api_v1_checkouts_tenant_payment_cancel_post) | **POST** /api/v1/checkouts/tenant/payment/cancel | Tenant Checkout Canceled
[**tenant_checkout_success_api_v1_checkouts_tenant_payment_success_post**](StripeCheckoutApi.md#tenant_checkout_success_api_v1_checkouts_tenant_payment_success_post) | **POST** /api/v1/checkouts/tenant/payment/success | Tenant Checkout Success


# **create_host_checkout_session_api_v1_checkouts_host_tenant_id_tenant_post**
> CheckoutResponseDto create_host_checkout_session_api_v1_checkouts_host_tenant_id_tenant_post(checkout_request_dto)

Create Host Checkout Session

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.checkout_request_dto import CheckoutRequestDto
from openapi_client.models.checkout_response_dto import CheckoutResponseDto
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
    api_instance = openapi_client.StripeCheckoutApi(api_client)
    checkout_request_dto = openapi_client.CheckoutRequestDto() # CheckoutRequestDto | 

    try:
        # Create Host Checkout Session
        api_response = api_instance.create_host_checkout_session_api_v1_checkouts_host_tenant_id_tenant_post(checkout_request_dto)
        print("The response of StripeCheckoutApi->create_host_checkout_session_api_v1_checkouts_host_tenant_id_tenant_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeCheckoutApi->create_host_checkout_session_api_v1_checkouts_host_tenant_id_tenant_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_request_dto** | [**CheckoutRequestDto**](CheckoutRequestDto.md)|  | 

### Return type

[**CheckoutResponseDto**](CheckoutResponseDto.md)

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

# **create_tenant_checkout_session_api_v1_checkouts_tenant_subscription_post**
> CheckoutResponseDto create_tenant_checkout_session_api_v1_checkouts_tenant_subscription_post(checkout_request_dto)

Create Tenant Checkout Session

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.checkout_request_dto import CheckoutRequestDto
from openapi_client.models.checkout_response_dto import CheckoutResponseDto
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
    api_instance = openapi_client.StripeCheckoutApi(api_client)
    checkout_request_dto = openapi_client.CheckoutRequestDto() # CheckoutRequestDto | 

    try:
        # Create Tenant Checkout Session
        api_response = api_instance.create_tenant_checkout_session_api_v1_checkouts_tenant_subscription_post(checkout_request_dto)
        print("The response of StripeCheckoutApi->create_tenant_checkout_session_api_v1_checkouts_tenant_subscription_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeCheckoutApi->create_tenant_checkout_session_api_v1_checkouts_tenant_subscription_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_request_dto** | [**CheckoutRequestDto**](CheckoutRequestDto.md)|  | 

### Return type

[**CheckoutResponseDto**](CheckoutResponseDto.md)

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

# **host_checkout_success_api_v1_checkouts_host_payment_cancel_post**
> object host_checkout_success_api_v1_checkouts_host_payment_cancel_post(tenant_id)

Host Checkout Success

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
    api_instance = openapi_client.StripeCheckoutApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Host Checkout Success
        api_response = api_instance.host_checkout_success_api_v1_checkouts_host_payment_cancel_post(tenant_id)
        print("The response of StripeCheckoutApi->host_checkout_success_api_v1_checkouts_host_payment_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeCheckoutApi->host_checkout_success_api_v1_checkouts_host_payment_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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

# **host_checkout_success_api_v1_checkouts_host_payment_success_post**
> object host_checkout_success_api_v1_checkouts_host_payment_success_post(session_id, tenant_id)

Host Checkout Success

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
    api_instance = openapi_client.StripeCheckoutApi(api_client)
    session_id = 'session_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Host Checkout Success
        api_response = api_instance.host_checkout_success_api_v1_checkouts_host_payment_success_post(session_id, tenant_id)
        print("The response of StripeCheckoutApi->host_checkout_success_api_v1_checkouts_host_payment_success_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeCheckoutApi->host_checkout_success_api_v1_checkouts_host_payment_success_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **tenant_id** | **str**|  | 

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

# **list_checkout_records_api_v1_checkouts_all_get**
> BillingRecordListDto list_checkout_records_api_v1_checkouts_all_get(skip=skip, limit=limit)

List Checkout Records

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.billing_record_list_dto import BillingRecordListDto
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
    api_instance = openapi_client.StripeCheckoutApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List Checkout Records
        api_response = api_instance.list_checkout_records_api_v1_checkouts_all_get(skip=skip, limit=limit)
        print("The response of StripeCheckoutApi->list_checkout_records_api_v1_checkouts_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeCheckoutApi->list_checkout_records_api_v1_checkouts_all_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**BillingRecordListDto**](BillingRecordListDto.md)

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

# **tenant_checkout_canceled_api_v1_checkouts_tenant_payment_cancel_post**
> object tenant_checkout_canceled_api_v1_checkouts_tenant_payment_cancel_post()

Tenant Checkout Canceled

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
    api_instance = openapi_client.StripeCheckoutApi(api_client)

    try:
        # Tenant Checkout Canceled
        api_response = api_instance.tenant_checkout_canceled_api_v1_checkouts_tenant_payment_cancel_post()
        print("The response of StripeCheckoutApi->tenant_checkout_canceled_api_v1_checkouts_tenant_payment_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeCheckoutApi->tenant_checkout_canceled_api_v1_checkouts_tenant_payment_cancel_post: %s\n" % e)
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
**202** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_checkout_success_api_v1_checkouts_tenant_payment_success_post**
> object tenant_checkout_success_api_v1_checkouts_tenant_payment_success_post(session_id)

Tenant Checkout Success

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
    api_instance = openapi_client.StripeCheckoutApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Tenant Checkout Success
        api_response = api_instance.tenant_checkout_success_api_v1_checkouts_tenant_payment_success_post(session_id)
        print("The response of StripeCheckoutApi->tenant_checkout_success_api_v1_checkouts_tenant_payment_success_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeCheckoutApi->tenant_checkout_success_api_v1_checkouts_tenant_payment_success_post: %s\n" % e)
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

