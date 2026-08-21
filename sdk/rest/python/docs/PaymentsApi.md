# openapi_client.PaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_budget_api_v1_budgets_budget_id_allocate_post**](PaymentsApi.md#allocate_budget_api_v1_budgets_budget_id_allocate_post) | **POST** /api/v1/budgets/{budget_id}/allocate | Allocate Budget
[**api_v1_budgets_get**](PaymentsApi.md#api_v1_budgets_get) | **GET** /api/v1/budgets | List crypto budgets
[**create_checkout_session_api_v1_payments_stripe_checkout_sessions_post**](PaymentsApi.md#create_checkout_session_api_v1_payments_stripe_checkout_sessions_post) | **POST** /api/v1/payments/stripe/checkout-sessions | Create Checkout Session
[**create_crypto_budget_api_v1_budgets_post**](PaymentsApi.md#create_crypto_budget_api_v1_budgets_post) | **POST** /api/v1/budgets | Create Crypto Budget
[**get_crypto_budget_api_v1_budgets_budget_id_get**](PaymentsApi.md#get_crypto_budget_api_v1_budgets_budget_id_get) | **GET** /api/v1/budgets/{budget_id} | Get Crypto Budget
[**stripe_webhook_api_v1_payments_stripe_webhook_post**](PaymentsApi.md#stripe_webhook_api_v1_payments_stripe_webhook_post) | **POST** /api/v1/payments/stripe/webhook | Stripe Webhook


# **allocate_budget_api_v1_budgets_budget_id_allocate_post**
> CryptoBudgetResponse allocate_budget_api_v1_budgets_budget_id_allocate_post(budget_id, budget_allocate_request)

Allocate Budget

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.budget_allocate_request import BudgetAllocateRequest
from openapi_client.models.crypto_budget_response import CryptoBudgetResponse
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
    api_instance = openapi_client.PaymentsApi(api_client)
    budget_id = 'budget_id_example' # str | 
    budget_allocate_request = openapi_client.BudgetAllocateRequest() # BudgetAllocateRequest | 

    try:
        # Allocate Budget
        api_response = api_instance.allocate_budget_api_v1_budgets_budget_id_allocate_post(budget_id, budget_allocate_request)
        print("The response of PaymentsApi->allocate_budget_api_v1_budgets_budget_id_allocate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->allocate_budget_api_v1_budgets_budget_id_allocate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**|  | 
 **budget_allocate_request** | [**BudgetAllocateRequest**](BudgetAllocateRequest.md)|  | 

### Return type

[**CryptoBudgetResponse**](CryptoBudgetResponse.md)

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

# **api_v1_budgets_get**
> CryptoBudgetListPage api_v1_budgets_get(limit=limit, offset=offset)

List crypto budgets

### Example


```python
import openapi_client
from openapi_client.models.crypto_budget_list_page import CryptoBudgetListPage
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
    api_instance = openapi_client.PaymentsApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List crypto budgets
        api_response = api_instance.api_v1_budgets_get(limit=limit, offset=offset)
        print("The response of PaymentsApi->api_v1_budgets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->api_v1_budgets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**CryptoBudgetListPage**](CryptoBudgetListPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_checkout_session_api_v1_payments_stripe_checkout_sessions_post**
> StripeCheckoutSessionResponse create_checkout_session_api_v1_payments_stripe_checkout_sessions_post(stripe_checkout_session_create)

Create Checkout Session

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.stripe_checkout_session_create import StripeCheckoutSessionCreate
from openapi_client.models.stripe_checkout_session_response import StripeCheckoutSessionResponse
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
    api_instance = openapi_client.PaymentsApi(api_client)
    stripe_checkout_session_create = openapi_client.StripeCheckoutSessionCreate() # StripeCheckoutSessionCreate | 

    try:
        # Create Checkout Session
        api_response = api_instance.create_checkout_session_api_v1_payments_stripe_checkout_sessions_post(stripe_checkout_session_create)
        print("The response of PaymentsApi->create_checkout_session_api_v1_payments_stripe_checkout_sessions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->create_checkout_session_api_v1_payments_stripe_checkout_sessions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_checkout_session_create** | [**StripeCheckoutSessionCreate**](StripeCheckoutSessionCreate.md)|  | 

### Return type

[**StripeCheckoutSessionResponse**](StripeCheckoutSessionResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_crypto_budget_api_v1_budgets_post**
> CryptoBudgetResponse create_crypto_budget_api_v1_budgets_post(crypto_budget_create_request)

Create Crypto Budget

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.crypto_budget_create_request import CryptoBudgetCreateRequest
from openapi_client.models.crypto_budget_response import CryptoBudgetResponse
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
    api_instance = openapi_client.PaymentsApi(api_client)
    crypto_budget_create_request = openapi_client.CryptoBudgetCreateRequest() # CryptoBudgetCreateRequest | 

    try:
        # Create Crypto Budget
        api_response = api_instance.create_crypto_budget_api_v1_budgets_post(crypto_budget_create_request)
        print("The response of PaymentsApi->create_crypto_budget_api_v1_budgets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->create_crypto_budget_api_v1_budgets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_budget_create_request** | [**CryptoBudgetCreateRequest**](CryptoBudgetCreateRequest.md)|  | 

### Return type

[**CryptoBudgetResponse**](CryptoBudgetResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_budget_api_v1_budgets_budget_id_get**
> CryptoBudgetResponse get_crypto_budget_api_v1_budgets_budget_id_get(budget_id)

Get Crypto Budget

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.crypto_budget_response import CryptoBudgetResponse
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
    api_instance = openapi_client.PaymentsApi(api_client)
    budget_id = 'budget_id_example' # str | 

    try:
        # Get Crypto Budget
        api_response = api_instance.get_crypto_budget_api_v1_budgets_budget_id_get(budget_id)
        print("The response of PaymentsApi->get_crypto_budget_api_v1_budgets_budget_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_crypto_budget_api_v1_budgets_budget_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**|  | 

### Return type

[**CryptoBudgetResponse**](CryptoBudgetResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stripe_webhook_api_v1_payments_stripe_webhook_post**
> object stripe_webhook_api_v1_payments_stripe_webhook_post()

Stripe Webhook

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
    api_instance = openapi_client.PaymentsApi(api_client)

    try:
        # Stripe Webhook
        api_response = api_instance.stripe_webhook_api_v1_payments_stripe_webhook_post()
        print("The response of PaymentsApi->stripe_webhook_api_v1_payments_stripe_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->stripe_webhook_api_v1_payments_stripe_webhook_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

