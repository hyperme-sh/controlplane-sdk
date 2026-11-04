# openapi_client.AppConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_configuration_api_v1_app_configuration_get**](AppConfigurationApi.md#get_app_configuration_api_v1_app_configuration_get) | **GET** /api/v1/app_configuration/ | Get App Configuration


# **get_app_configuration_api_v1_app_configuration_get**
> AppConfigurationDto get_app_configuration_api_v1_app_configuration_get()

Get App Configuration

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.app_configuration_dto import AppConfigurationDto
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
    api_instance = openapi_client.AppConfigurationApi(api_client)

    try:
        # Get App Configuration
        api_response = api_instance.get_app_configuration_api_v1_app_configuration_get()
        print("The response of AppConfigurationApi->get_app_configuration_api_v1_app_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppConfigurationApi->get_app_configuration_api_v1_app_configuration_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppConfigurationDto**](AppConfigurationDto.md)

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

