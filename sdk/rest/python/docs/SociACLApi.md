# openapi_client.SociACLApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sociacl_create_share_api_v1_acl_sociacl_shares_post**](SociACLApi.md#sociacl_create_share_api_v1_acl_sociacl_shares_post) | **POST** /api/v1/acl/sociacl/shares | Sociacl Create Share
[**sociacl_evaluate_api_v1_acl_sociacl_evaluate_post**](SociACLApi.md#sociacl_evaluate_api_v1_acl_sociacl_evaluate_post) | **POST** /api/v1/acl/sociacl/evaluate | Sociacl Evaluate
[**sociacl_recovery_create_api_v1_acl_sociacl_recovery_sessions_post**](SociACLApi.md#sociacl_recovery_create_api_v1_acl_sociacl_recovery_sessions_post) | **POST** /api/v1/acl/sociacl/recovery/sessions | Sociacl Recovery Create
[**sociacl_recovery_proof_api_v1_acl_sociacl_recovery_sessions_session_id_proof_post**](SociACLApi.md#sociacl_recovery_proof_api_v1_acl_sociacl_recovery_sessions_session_id_proof_post) | **POST** /api/v1/acl/sociacl/recovery/sessions/{session_id}/proof | Sociacl Recovery Proof
[**sociacl_resolve_share_api_v1_acl_sociacl_shares_by_token_token_get**](SociACLApi.md#sociacl_resolve_share_api_v1_acl_sociacl_shares_by_token_token_get) | **GET** /api/v1/acl/sociacl/shares/by-token/{token} | Sociacl Resolve Share


# **sociacl_create_share_api_v1_acl_sociacl_shares_post**
> SociaclShareCreatedResponse sociacl_create_share_api_v1_acl_sociacl_shares_post(soci_acl_share_link_create)

Sociacl Create Share

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.soci_acl_share_link_create import SociACLShareLinkCreate
from openapi_client.models.sociacl_share_created_response import SociaclShareCreatedResponse
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
    api_instance = openapi_client.SociACLApi(api_client)
    soci_acl_share_link_create = openapi_client.SociACLShareLinkCreate() # SociACLShareLinkCreate | 

    try:
        # Sociacl Create Share
        api_response = api_instance.sociacl_create_share_api_v1_acl_sociacl_shares_post(soci_acl_share_link_create)
        print("The response of SociACLApi->sociacl_create_share_api_v1_acl_sociacl_shares_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SociACLApi->sociacl_create_share_api_v1_acl_sociacl_shares_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soci_acl_share_link_create** | [**SociACLShareLinkCreate**](SociACLShareLinkCreate.md)|  | 

### Return type

[**SociaclShareCreatedResponse**](SociaclShareCreatedResponse.md)

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

# **sociacl_evaluate_api_v1_acl_sociacl_evaluate_post**
> object sociacl_evaluate_api_v1_acl_sociacl_evaluate_post(soci_acl_evaluate_request)

Sociacl Evaluate

### Example


```python
import openapi_client
from openapi_client.models.soci_acl_evaluate_request import SociACLEvaluateRequest
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
    api_instance = openapi_client.SociACLApi(api_client)
    soci_acl_evaluate_request = openapi_client.SociACLEvaluateRequest() # SociACLEvaluateRequest | 

    try:
        # Sociacl Evaluate
        api_response = api_instance.sociacl_evaluate_api_v1_acl_sociacl_evaluate_post(soci_acl_evaluate_request)
        print("The response of SociACLApi->sociacl_evaluate_api_v1_acl_sociacl_evaluate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SociACLApi->sociacl_evaluate_api_v1_acl_sociacl_evaluate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soci_acl_evaluate_request** | [**SociACLEvaluateRequest**](SociACLEvaluateRequest.md)|  | 

### Return type

**object**

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

# **sociacl_recovery_create_api_v1_acl_sociacl_recovery_sessions_post**
> RecoverySessionResponse sociacl_recovery_create_api_v1_acl_sociacl_recovery_sessions_post(recovery_session_create)

Sociacl Recovery Create

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.recovery_session_create import RecoverySessionCreate
from openapi_client.models.recovery_session_response import RecoverySessionResponse
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
    api_instance = openapi_client.SociACLApi(api_client)
    recovery_session_create = openapi_client.RecoverySessionCreate() # RecoverySessionCreate | 

    try:
        # Sociacl Recovery Create
        api_response = api_instance.sociacl_recovery_create_api_v1_acl_sociacl_recovery_sessions_post(recovery_session_create)
        print("The response of SociACLApi->sociacl_recovery_create_api_v1_acl_sociacl_recovery_sessions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SociACLApi->sociacl_recovery_create_api_v1_acl_sociacl_recovery_sessions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_session_create** | [**RecoverySessionCreate**](RecoverySessionCreate.md)|  | 

### Return type

[**RecoverySessionResponse**](RecoverySessionResponse.md)

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

# **sociacl_recovery_proof_api_v1_acl_sociacl_recovery_sessions_session_id_proof_post**
> object sociacl_recovery_proof_api_v1_acl_sociacl_recovery_sessions_session_id_proof_post(session_id, recovery_proof_request)

Sociacl Recovery Proof

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.recovery_proof_request import RecoveryProofRequest
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
    api_instance = openapi_client.SociACLApi(api_client)
    session_id = 'session_id_example' # str | 
    recovery_proof_request = openapi_client.RecoveryProofRequest() # RecoveryProofRequest | 

    try:
        # Sociacl Recovery Proof
        api_response = api_instance.sociacl_recovery_proof_api_v1_acl_sociacl_recovery_sessions_session_id_proof_post(session_id, recovery_proof_request)
        print("The response of SociACLApi->sociacl_recovery_proof_api_v1_acl_sociacl_recovery_sessions_session_id_proof_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SociACLApi->sociacl_recovery_proof_api_v1_acl_sociacl_recovery_sessions_session_id_proof_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **recovery_proof_request** | [**RecoveryProofRequest**](RecoveryProofRequest.md)|  | 

### Return type

**object**

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

# **sociacl_resolve_share_api_v1_acl_sociacl_shares_by_token_token_get**
> SociACLShareLinkPublic sociacl_resolve_share_api_v1_acl_sociacl_shares_by_token_token_get(token)

Sociacl Resolve Share

### Example


```python
import openapi_client
from openapi_client.models.soci_acl_share_link_public import SociACLShareLinkPublic
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
    api_instance = openapi_client.SociACLApi(api_client)
    token = 'token_example' # str | 

    try:
        # Sociacl Resolve Share
        api_response = api_instance.sociacl_resolve_share_api_v1_acl_sociacl_shares_by_token_token_get(token)
        print("The response of SociACLApi->sociacl_resolve_share_api_v1_acl_sociacl_shares_by_token_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SociACLApi->sociacl_resolve_share_api_v1_acl_sociacl_shares_by_token_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**SociACLShareLinkPublic**](SociACLShareLinkPublic.md)

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

