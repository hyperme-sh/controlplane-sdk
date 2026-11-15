# openapi_client.WalletAuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_siwe_bind_auth_siwe_bind_post**](WalletAuthApi.md#auth_siwe_bind_auth_siwe_bind_post) | **POST** /auth/siwe/bind | Bind one SIWE wallet onto the identified Keycloak person
[**auth_siwe_me_auth_siwe_me_get**](WalletAuthApi.md#auth_siwe_me_auth_siwe_me_get) | **GET** /auth/siwe/me | Wallet bound to the identified Keycloak person
[**auth_siwe_nonce_auth_siwe_nonce_post**](WalletAuthApi.md#auth_siwe_nonce_auth_siwe_nonce_post) | **POST** /auth/siwe/nonce | Issue an EIP-4361 nonce for the identified Keycloak person


# **auth_siwe_bind_auth_siwe_bind_post**
> WalletAuthWalletBindingResponse auth_siwe_bind_auth_siwe_bind_post(wallet_auth_siwe_bind_request)

Bind one SIWE wallet onto the identified Keycloak person

Verifies EIP-4361 and stores the recovered address only. Not a second login. Signature is not stored or returned.

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wallet_auth_siwe_bind_request import WalletAuthSiweBindRequest
from openapi_client.models.wallet_auth_wallet_binding_response import WalletAuthWalletBindingResponse
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
    api_instance = openapi_client.WalletAuthApi(api_client)
    wallet_auth_siwe_bind_request = openapi_client.WalletAuthSiweBindRequest() # WalletAuthSiweBindRequest | 

    try:
        # Bind one SIWE wallet onto the identified Keycloak person
        api_response = api_instance.auth_siwe_bind_auth_siwe_bind_post(wallet_auth_siwe_bind_request)
        print("The response of WalletAuthApi->auth_siwe_bind_auth_siwe_bind_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletAuthApi->auth_siwe_bind_auth_siwe_bind_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_auth_siwe_bind_request** | [**WalletAuthSiweBindRequest**](WalletAuthSiweBindRequest.md)|  | 

### Return type

[**WalletAuthWalletBindingResponse**](WalletAuthWalletBindingResponse.md)

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

# **auth_siwe_me_auth_siwe_me_get**
> WalletAuthWalletBindingResponse auth_siwe_me_auth_siwe_me_get()

Wallet bound to the identified Keycloak person

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wallet_auth_wallet_binding_response import WalletAuthWalletBindingResponse
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
    api_instance = openapi_client.WalletAuthApi(api_client)

    try:
        # Wallet bound to the identified Keycloak person
        api_response = api_instance.auth_siwe_me_auth_siwe_me_get()
        print("The response of WalletAuthApi->auth_siwe_me_auth_siwe_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletAuthApi->auth_siwe_me_auth_siwe_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WalletAuthWalletBindingResponse**](WalletAuthWalletBindingResponse.md)

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

# **auth_siwe_nonce_auth_siwe_nonce_post**
> WalletAuthSiweNonceResponse auth_siwe_nonce_auth_siwe_nonce_post(wallet_auth_siwe_nonce_request)

Issue an EIP-4361 nonce for the identified Keycloak person

Keycloak OIDC remains the login. This nonce is only for binding one wallet to that same person. Password grant stays off.

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wallet_auth_siwe_nonce_request import WalletAuthSiweNonceRequest
from openapi_client.models.wallet_auth_siwe_nonce_response import WalletAuthSiweNonceResponse
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
    api_instance = openapi_client.WalletAuthApi(api_client)
    wallet_auth_siwe_nonce_request = openapi_client.WalletAuthSiweNonceRequest() # WalletAuthSiweNonceRequest | 

    try:
        # Issue an EIP-4361 nonce for the identified Keycloak person
        api_response = api_instance.auth_siwe_nonce_auth_siwe_nonce_post(wallet_auth_siwe_nonce_request)
        print("The response of WalletAuthApi->auth_siwe_nonce_auth_siwe_nonce_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletAuthApi->auth_siwe_nonce_auth_siwe_nonce_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_auth_siwe_nonce_request** | [**WalletAuthSiweNonceRequest**](WalletAuthSiweNonceRequest.md)|  | 

### Return type

[**WalletAuthSiweNonceResponse**](WalletAuthSiweNonceResponse.md)

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

