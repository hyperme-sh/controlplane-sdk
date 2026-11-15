# openapi_client.WalletPaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**challenge_api_v1_payments_host_payout_address_challenge_post**](WalletPaymentsApi.md#challenge_api_v1_payments_host_payout_address_challenge_post) | **POST** /api/v1/payments/host-payout-address/challenge | Challenge
[**create_wallet_checkout**](WalletPaymentsApi.md#create_wallet_checkout) | **POST** /api/v1/payments/wallet/lease-payments/{billing_record_id}/checkout | Open Stablecoin Checkout
[**create_wallet_deposit**](WalletPaymentsApi.md#create_wallet_deposit) | **POST** /api/v1/payments/wallet/lease-payments/{billing_record_id}/deposit | Create Deposit
[**create_wallet_lease_payment**](WalletPaymentsApi.md#create_wallet_lease_payment) | **POST** /api/v1/payments/wallet/lease-payments | Create Usdc Lease Payment Route
[**get_wallet_deposit**](WalletPaymentsApi.md#get_wallet_deposit) | **GET** /api/v1/payments/wallet/lease-payments/{billing_record_id}/deposit | Deposit Status
[**get_wallet_payment_capabilities**](WalletPaymentsApi.md#get_wallet_payment_capabilities) | **GET** /api/v1/payments/wallet/capabilities | Wallet Capabilities
[**submit_api_v1_payments_host_payout_address_post**](WalletPaymentsApi.md#submit_api_v1_payments_host_payout_address_post) | **POST** /api/v1/payments/host-payout-address | Submit


# **challenge_api_v1_payments_host_payout_address_challenge_post**
> WalletPaymentPayoutChallenge challenge_api_v1_payments_host_payout_address_challenge_post(x_tenant_id, wallet_payment_challenge_request)

Challenge

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wallet_payment_challenge_request import WalletPaymentChallengeRequest
from openapi_client.models.wallet_payment_payout_challenge import WalletPaymentPayoutChallenge
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WalletPaymentsApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str | Must match the browser tenant session
    wallet_payment_challenge_request = openapi_client.WalletPaymentChallengeRequest() # WalletPaymentChallengeRequest | 

    try:
        # Challenge
        api_response = api_instance.challenge_api_v1_payments_host_payout_address_challenge_post(x_tenant_id, wallet_payment_challenge_request)
        print("The response of WalletPaymentsApi->challenge_api_v1_payments_host_payout_address_challenge_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletPaymentsApi->challenge_api_v1_payments_host_payout_address_challenge_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Must match the browser tenant session | 
 **wallet_payment_challenge_request** | [**WalletPaymentChallengeRequest**](WalletPaymentChallengeRequest.md)|  | 

### Return type

[**WalletPaymentPayoutChallenge**](WalletPaymentPayoutChallenge.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wallet_checkout**
> WalletPaymentWalletCheckoutResponse create_wallet_checkout(billing_record_id, x_tenant_id)

Open Stablecoin Checkout

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wallet_payment_wallet_checkout_response import WalletPaymentWalletCheckoutResponse
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
    api_instance = openapi_client.WalletPaymentsApi(api_client)
    billing_record_id = 'billing_record_id_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str | 

    try:
        # Open Stablecoin Checkout
        api_response = api_instance.create_wallet_checkout(billing_record_id, x_tenant_id)
        print("The response of WalletPaymentsApi->create_wallet_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletPaymentsApi->create_wallet_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_record_id** | **str**|  | 
 **x_tenant_id** | **str**|  | 

### Return type

[**WalletPaymentWalletCheckoutResponse**](WalletPaymentWalletCheckoutResponse.md)

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

# **create_wallet_deposit**
> WalletPaymentWalletDepositStatus create_wallet_deposit(billing_record_id, x_tenant_id)

Create Deposit

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wallet_payment_wallet_deposit_status import WalletPaymentWalletDepositStatus
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
    api_instance = openapi_client.WalletPaymentsApi(api_client)
    billing_record_id = 'billing_record_id_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str | 

    try:
        # Create Deposit
        api_response = api_instance.create_wallet_deposit(billing_record_id, x_tenant_id)
        print("The response of WalletPaymentsApi->create_wallet_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletPaymentsApi->create_wallet_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_record_id** | **str**|  | 
 **x_tenant_id** | **str**|  | 

### Return type

[**WalletPaymentWalletDepositStatus**](WalletPaymentWalletDepositStatus.md)

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

# **create_wallet_lease_payment**
> WalletPaymentWalletLeasePaymentResponse create_wallet_lease_payment(x_tenant_id, wallet_payment_usdc_lease_payment_create, idempotency_key=idempotency_key)

Create Usdc Lease Payment Route

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wallet_payment_usdc_lease_payment_create import WalletPaymentUsdcLeasePaymentCreate
from openapi_client.models.wallet_payment_wallet_lease_payment_response import WalletPaymentWalletLeasePaymentResponse
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
    api_instance = openapi_client.WalletPaymentsApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str | 
    wallet_payment_usdc_lease_payment_create = openapi_client.WalletPaymentUsdcLeasePaymentCreate() # WalletPaymentUsdcLeasePaymentCreate | 
    idempotency_key = 'idempotency_key_example' # str | Reuse the same UUID when retrying the same payment request. (optional)

    try:
        # Create Usdc Lease Payment Route
        api_response = api_instance.create_wallet_lease_payment(x_tenant_id, wallet_payment_usdc_lease_payment_create, idempotency_key=idempotency_key)
        print("The response of WalletPaymentsApi->create_wallet_lease_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletPaymentsApi->create_wallet_lease_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**|  | 
 **wallet_payment_usdc_lease_payment_create** | [**WalletPaymentUsdcLeasePaymentCreate**](WalletPaymentUsdcLeasePaymentCreate.md)|  | 
 **idempotency_key** | **str**| Reuse the same UUID when retrying the same payment request. | [optional] 

### Return type

[**WalletPaymentWalletLeasePaymentResponse**](WalletPaymentWalletLeasePaymentResponse.md)

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

# **get_wallet_deposit**
> WalletPaymentWalletDepositStatus get_wallet_deposit(billing_record_id, x_tenant_id)

Deposit Status

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wallet_payment_wallet_deposit_status import WalletPaymentWalletDepositStatus
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
    api_instance = openapi_client.WalletPaymentsApi(api_client)
    billing_record_id = 'billing_record_id_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str | 

    try:
        # Deposit Status
        api_response = api_instance.get_wallet_deposit(billing_record_id, x_tenant_id)
        print("The response of WalletPaymentsApi->get_wallet_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletPaymentsApi->get_wallet_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_record_id** | **str**|  | 
 **x_tenant_id** | **str**|  | 

### Return type

[**WalletPaymentWalletDepositStatus**](WalletPaymentWalletDepositStatus.md)

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

# **get_wallet_payment_capabilities**
> WalletPaymentWalletCapabilities get_wallet_payment_capabilities(x_tenant_id)

Wallet Capabilities

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wallet_payment_wallet_capabilities import WalletPaymentWalletCapabilities
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
    api_instance = openapi_client.WalletPaymentsApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str | 

    try:
        # Wallet Capabilities
        api_response = api_instance.get_wallet_payment_capabilities(x_tenant_id)
        print("The response of WalletPaymentsApi->get_wallet_payment_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletPaymentsApi->get_wallet_payment_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**|  | 

### Return type

[**WalletPaymentWalletCapabilities**](WalletPaymentWalletCapabilities.md)

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

# **submit_api_v1_payments_host_payout_address_post**
> WalletPaymentRegisteredDestination submit_api_v1_payments_host_payout_address_post(x_tenant_id, wallet_payment_submit_request)

Submit

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wallet_payment_registered_destination import WalletPaymentRegisteredDestination
from openapi_client.models.wallet_payment_submit_request import WalletPaymentSubmitRequest
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WalletPaymentsApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str | Must match the browser tenant session
    wallet_payment_submit_request = openapi_client.WalletPaymentSubmitRequest() # WalletPaymentSubmitRequest | 

    try:
        # Submit
        api_response = api_instance.submit_api_v1_payments_host_payout_address_post(x_tenant_id, wallet_payment_submit_request)
        print("The response of WalletPaymentsApi->submit_api_v1_payments_host_payout_address_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletPaymentsApi->submit_api_v1_payments_host_payout_address_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Must match the browser tenant session | 
 **wallet_payment_submit_request** | [**WalletPaymentSubmitRequest**](WalletPaymentSubmitRequest.md)|  | 

### Return type

[**WalletPaymentRegisteredDestination**](WalletPaymentRegisteredDestination.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

