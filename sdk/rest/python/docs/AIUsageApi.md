# openapi_client.AIUsageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_ai_usage_history_get**](AIUsageApi.md#api_v1_ai_usage_history_get) | **GET** /api/v1/ai/usage/history | List inference usage history
[**api_v1_ai_usage_summary_get**](AIUsageApi.md#api_v1_ai_usage_summary_get) | **GET** /api/v1/ai/usage/summary | Tenant usage summary


# **api_v1_ai_usage_history_get**
> InferenceHistoryPage api_v1_ai_usage_history_get(limit=limit, offset=offset, user_id=user_id)

List inference usage history

### Example


```python
import openapi_client
from openapi_client.models.inference_history_page import InferenceHistoryPage
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
    api_instance = openapi_client.AIUsageApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    user_id = 'user_id_example' # str |  (optional)

    try:
        # List inference usage history
        api_response = api_instance.api_v1_ai_usage_history_get(limit=limit, offset=offset, user_id=user_id)
        print("The response of AIUsageApi->api_v1_ai_usage_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIUsageApi->api_v1_ai_usage_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **user_id** | **str**|  | [optional] 

### Return type

[**InferenceHistoryPage**](InferenceHistoryPage.md)

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

# **api_v1_ai_usage_summary_get**
> TenantUsageSummaryResponse api_v1_ai_usage_summary_get()

Tenant usage summary

### Example


```python
import openapi_client
from openapi_client.models.tenant_usage_summary_response import TenantUsageSummaryResponse
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
    api_instance = openapi_client.AIUsageApi(api_client)

    try:
        # Tenant usage summary
        api_response = api_instance.api_v1_ai_usage_summary_get()
        print("The response of AIUsageApi->api_v1_ai_usage_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIUsageApi->api_v1_ai_usage_summary_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantUsageSummaryResponse**](TenantUsageSummaryResponse.md)

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

