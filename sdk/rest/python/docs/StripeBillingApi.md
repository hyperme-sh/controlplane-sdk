# openapi_client.StripeBillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan_api_v1_billing_plans_post**](StripeBillingApi.md#create_plan_api_v1_billing_plans_post) | **POST** /api/v1/billing/plans | Create a new plan
[**delete_plan_api_v1_billing_plans_plan_id_delete**](StripeBillingApi.md#delete_plan_api_v1_billing_plans_plan_id_delete) | **DELETE** /api/v1/billing/plans/{plan_id} | Delete existing plan
[**get_plan_api_v1_billing_plans_plan_id_get**](StripeBillingApi.md#get_plan_api_v1_billing_plans_plan_id_get) | **GET** /api/v1/billing/plans/{plan_id} | Retrieve a plan details
[**list_plans_api_v1_billing_plans_get**](StripeBillingApi.md#list_plans_api_v1_billing_plans_get) | **GET** /api/v1/billing/plans | List available plans
[**update_plan_api_v1_billing_plans_plan_id_patch**](StripeBillingApi.md#update_plan_api_v1_billing_plans_plan_id_patch) | **PATCH** /api/v1/billing/plans/{plan_id} | Update a existing plan


# **create_plan_api_v1_billing_plans_post**
> object create_plan_api_v1_billing_plans_post(create_plan_dto)

Create a new plan

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_plan_dto import CreatePlanDto
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
    api_instance = openapi_client.StripeBillingApi(api_client)
    create_plan_dto = openapi_client.CreatePlanDto() # CreatePlanDto | 

    try:
        # Create a new plan
        api_response = api_instance.create_plan_api_v1_billing_plans_post(create_plan_dto)
        print("The response of StripeBillingApi->create_plan_api_v1_billing_plans_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeBillingApi->create_plan_api_v1_billing_plans_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_plan_dto** | [**CreatePlanDto**](CreatePlanDto.md)|  | 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plan_api_v1_billing_plans_plan_id_delete**
> object delete_plan_api_v1_billing_plans_plan_id_delete(plan_id)

Delete existing plan

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
    api_instance = openapi_client.StripeBillingApi(api_client)
    plan_id = 'plan_id_example' # str | 

    try:
        # Delete existing plan
        api_response = api_instance.delete_plan_api_v1_billing_plans_plan_id_delete(plan_id)
        print("The response of StripeBillingApi->delete_plan_api_v1_billing_plans_plan_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeBillingApi->delete_plan_api_v1_billing_plans_plan_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

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

# **get_plan_api_v1_billing_plans_plan_id_get**
> PlanDto get_plan_api_v1_billing_plans_plan_id_get(plan_id)

Retrieve a plan details

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.plan_dto import PlanDto
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
    api_instance = openapi_client.StripeBillingApi(api_client)
    plan_id = 'plan_id_example' # str | 

    try:
        # Retrieve a plan details
        api_response = api_instance.get_plan_api_v1_billing_plans_plan_id_get(plan_id)
        print("The response of StripeBillingApi->get_plan_api_v1_billing_plans_plan_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeBillingApi->get_plan_api_v1_billing_plans_plan_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

### Return type

[**PlanDto**](PlanDto.md)

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

# **list_plans_api_v1_billing_plans_get**
> PlanListDto list_plans_api_v1_billing_plans_get()

List available plans

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.plan_list_dto import PlanListDto
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
    api_instance = openapi_client.StripeBillingApi(api_client)

    try:
        # List available plans
        api_response = api_instance.list_plans_api_v1_billing_plans_get()
        print("The response of StripeBillingApi->list_plans_api_v1_billing_plans_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeBillingApi->list_plans_api_v1_billing_plans_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PlanListDto**](PlanListDto.md)

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

# **update_plan_api_v1_billing_plans_plan_id_patch**
> update_plan_api_v1_billing_plans_plan_id_patch(plan_id, update_plan_dto)

Update a existing plan

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.update_plan_dto import UpdatePlanDto
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
    api_instance = openapi_client.StripeBillingApi(api_client)
    plan_id = 'plan_id_example' # str | 
    update_plan_dto = openapi_client.UpdatePlanDto() # UpdatePlanDto | 

    try:
        # Update a existing plan
        api_instance.update_plan_api_v1_billing_plans_plan_id_patch(plan_id, update_plan_dto)
    except Exception as e:
        print("Exception when calling StripeBillingApi->update_plan_api_v1_billing_plans_plan_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **update_plan_dto** | [**UpdatePlanDto**](UpdatePlanDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

