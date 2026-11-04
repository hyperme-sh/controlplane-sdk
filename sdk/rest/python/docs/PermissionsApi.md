# openapi_client.PermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permissions_api_v1_permissions_get**](PermissionsApi.md#get_permissions_api_v1_permissions_get) | **GET** /api/v1/permissions/ | Get Permissions


# **get_permissions_api_v1_permissions_get**
> List[PermissionDto] get_permissions_api_v1_permissions_get()

Get Permissions

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.permission_dto import PermissionDto
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
    api_instance = openapi_client.PermissionsApi(api_client)

    try:
        # Get Permissions
        api_response = api_instance.get_permissions_api_v1_permissions_get()
        print("The response of PermissionsApi->get_permissions_api_v1_permissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_permissions_api_v1_permissions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PermissionDto]**](PermissionDto.md)

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

