# openapi_client.DashboardApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard_metrics_api_v1_dashboard_get**](DashboardApi.md#get_dashboard_metrics_api_v1_dashboard_get) | **GET** /api/v1/dashboard/ | Get Dashboard Metrics


# **get_dashboard_metrics_api_v1_dashboard_get**
> DashboardMetricsDto get_dashboard_metrics_api_v1_dashboard_get(filter=filter)

Get Dashboard Metrics

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.dashboard_metrics_dto import DashboardMetricsDto
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
    api_instance = openapi_client.DashboardApi(api_client)
    filter = all # str |  (optional) (default to all)

    try:
        # Get Dashboard Metrics
        api_response = api_instance.get_dashboard_metrics_api_v1_dashboard_get(filter=filter)
        print("The response of DashboardApi->get_dashboard_metrics_api_v1_dashboard_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->get_dashboard_metrics_api_v1_dashboard_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|  | [optional] [default to all]

### Return type

[**DashboardMetricsDto**](DashboardMetricsDto.md)

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

