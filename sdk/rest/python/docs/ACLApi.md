# openapi_client.ACLApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_api_v1_acl_policies_post**](ACLApi.md#create_policy_api_v1_acl_policies_post) | **POST** /api/v1/acl/policies | Create Policy
[**enforce_check_api_v1_acl_enforce_post**](ACLApi.md#enforce_check_api_v1_acl_enforce_post) | **POST** /api/v1/acl/enforce | Enforce Check
[**list_policies_api_v1_acl_policies_get**](ACLApi.md#list_policies_api_v1_acl_policies_get) | **GET** /api/v1/acl/policies | List Policies
[**protected_ping_api_v1_acl_protected_ping_get**](ACLApi.md#protected_ping_api_v1_acl_protected_ping_get) | **GET** /api/v1/acl/protected-ping | Protected Ping
[**remove_policy_api_v1_acl_policies_delete**](ACLApi.md#remove_policy_api_v1_acl_policies_delete) | **DELETE** /api/v1/acl/policies | Remove Policy


# **create_policy_api_v1_acl_policies_post**
> PolicyRowResponse create_policy_api_v1_acl_policies_post(policy_rule_create)

Create Policy

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.policy_row_response import PolicyRowResponse
from openapi_client.models.policy_rule_create import PolicyRuleCreate
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
    api_instance = openapi_client.ACLApi(api_client)
    policy_rule_create = openapi_client.PolicyRuleCreate() # PolicyRuleCreate | 

    try:
        # Create Policy
        api_response = api_instance.create_policy_api_v1_acl_policies_post(policy_rule_create)
        print("The response of ACLApi->create_policy_api_v1_acl_policies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->create_policy_api_v1_acl_policies_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_rule_create** | [**PolicyRuleCreate**](PolicyRuleCreate.md)|  | 

### Return type

[**PolicyRowResponse**](PolicyRowResponse.md)

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

# **enforce_check_api_v1_acl_enforce_post**
> EnforceResponse enforce_check_api_v1_acl_enforce_post(enforce_request)

Enforce Check

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.enforce_request import EnforceRequest
from openapi_client.models.enforce_response import EnforceResponse
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
    api_instance = openapi_client.ACLApi(api_client)
    enforce_request = openapi_client.EnforceRequest() # EnforceRequest | 

    try:
        # Enforce Check
        api_response = api_instance.enforce_check_api_v1_acl_enforce_post(enforce_request)
        print("The response of ACLApi->enforce_check_api_v1_acl_enforce_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->enforce_check_api_v1_acl_enforce_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enforce_request** | [**EnforceRequest**](EnforceRequest.md)|  | 

### Return type

[**EnforceResponse**](EnforceResponse.md)

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

# **list_policies_api_v1_acl_policies_get**
> List[PolicyRowResponse] list_policies_api_v1_acl_policies_get()

List Policies

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.policy_row_response import PolicyRowResponse
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
    api_instance = openapi_client.ACLApi(api_client)

    try:
        # List Policies
        api_response = api_instance.list_policies_api_v1_acl_policies_get()
        print("The response of ACLApi->list_policies_api_v1_acl_policies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->list_policies_api_v1_acl_policies_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PolicyRowResponse]**](PolicyRowResponse.md)

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

# **protected_ping_api_v1_acl_protected_ping_get**
> object protected_ping_api_v1_acl_protected_ping_get()

Protected Ping

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
    api_instance = openapi_client.ACLApi(api_client)

    try:
        # Protected Ping
        api_response = api_instance.protected_ping_api_v1_acl_protected_ping_get()
        print("The response of ACLApi->protected_ping_api_v1_acl_protected_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->protected_ping_api_v1_acl_protected_ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **remove_policy_api_v1_acl_policies_delete**
> remove_policy_api_v1_acl_policies_delete(policy_rule_delete)

Remove Policy

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.policy_rule_delete import PolicyRuleDelete
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
    api_instance = openapi_client.ACLApi(api_client)
    policy_rule_delete = openapi_client.PolicyRuleDelete() # PolicyRuleDelete | 

    try:
        # Remove Policy
        api_instance.remove_policy_api_v1_acl_policies_delete(policy_rule_delete)
    except Exception as e:
        print("Exception when calling ACLApi->remove_policy_api_v1_acl_policies_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_rule_delete** | [**PolicyRuleDelete**](PolicyRuleDelete.md)|  | 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

