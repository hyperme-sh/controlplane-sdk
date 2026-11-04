# openapi_client.PaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_budget_api_v1_budgets_budget_id_allocate_post**](PaymentsApi.md#allocate_budget_api_v1_budgets_budget_id_allocate_post) | **POST** /api/v1/budgets/{budget_id}/allocate | Allocate Budget
[**api_v1_budgets_get**](PaymentsApi.md#api_v1_budgets_get) | **GET** /api/v1/budgets | List crypto budgets
[**create_crypto_budget_api_v1_budgets_post**](PaymentsApi.md#create_crypto_budget_api_v1_budgets_post) | **POST** /api/v1/budgets | Create Crypto Budget
[**create_usdc_lease_payment_route_api_v1_payments_usdc_lease_payments_post**](PaymentsApi.md#create_usdc_lease_payment_route_api_v1_payments_usdc_lease_payments_post) | **POST** /api/v1/payments/usdc/lease-payments | Open a USDC payment for a lease
[**get_crypto_budget_api_v1_budgets_budget_id_get**](PaymentsApi.md#get_crypto_budget_api_v1_budgets_budget_id_get) | **GET** /api/v1/budgets/{budget_id} | Get Crypto Budget
[**settle_usdc_test_credit_api_v1_payments_usdc_lease_payments_billing_record_id_test_credit_post**](PaymentsApi.md#settle_usdc_test_credit_api_v1_payments_usdc_lease_payments_billing_record_id_test_credit_post) | **POST** /api/v1/payments/usdc/lease-payments/{billing_record_id}/test-credit | Settle a lease payment from the test-network credit
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

# **create_usdc_lease_payment_route_api_v1_payments_usdc_lease_payments_post**
> UsdcLeasePaymentResponse create_usdc_lease_payment_route_api_v1_payments_usdc_lease_payments_post(usdc_lease_payment_create)

Open a USDC payment for a lease

Accepts a tenant-session JWT (human after switch-tenant) or a gateway exchange JWT from a purpose=service key or a renter key minted via the org-admin API. Not a portal paste. Not a KV-stashed portal JWT. Raw Keycloak without tenant_id is 403. No card is charged. The renter pays the amount in USDC on Base.

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.usdc_lease_payment_create import UsdcLeasePaymentCreate
from openapi_client.models.usdc_lease_payment_response import UsdcLeasePaymentResponse
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
    usdc_lease_payment_create = openapi_client.UsdcLeasePaymentCreate() # UsdcLeasePaymentCreate | 

    try:
        # Open a USDC payment for a lease
        api_response = api_instance.create_usdc_lease_payment_route_api_v1_payments_usdc_lease_payments_post(usdc_lease_payment_create)
        print("The response of PaymentsApi->create_usdc_lease_payment_route_api_v1_payments_usdc_lease_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->create_usdc_lease_payment_route_api_v1_payments_usdc_lease_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usdc_lease_payment_create** | [**UsdcLeasePaymentCreate**](UsdcLeasePaymentCreate.md)|  | 

### Return type

[**UsdcLeasePaymentResponse**](UsdcLeasePaymentResponse.md)

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

# **settle_usdc_test_credit_api_v1_payments_usdc_lease_payments_billing_record_id_test_credit_post**
> UsdcLeasePaymentResponse settle_usdc_test_credit_api_v1_payments_usdc_lease_payments_billing_record_id_test_credit_post(billing_record_id)

Settle a lease payment from the test-network credit

Available only where PAYMENTS_USDC_TEST_CREDIT_ENABLED is true and the deployment is Base Sepolia with Stripe in test mode. Marks the pending USDC payment succeeded and publishes payment.succeeded.v1, the same event a confirmed chain transfer publishes. Not available on Base mainnet.

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.usdc_lease_payment_response import UsdcLeasePaymentResponse
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
    billing_record_id = 'billing_record_id_example' # str | 

    try:
        # Settle a lease payment from the test-network credit
        api_response = api_instance.settle_usdc_test_credit_api_v1_payments_usdc_lease_payments_billing_record_id_test_credit_post(billing_record_id)
        print("The response of PaymentsApi->settle_usdc_test_credit_api_v1_payments_usdc_lease_payments_billing_record_id_test_credit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->settle_usdc_test_credit_api_v1_payments_usdc_lease_payments_billing_record_id_test_credit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_record_id** | **str**|  | 

### Return type

[**UsdcLeasePaymentResponse**](UsdcLeasePaymentResponse.md)

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

