# openapi_client.BrandingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**partial_update_branding_api_v1_brandings_branding_id_patch**](BrandingApi.md#partial_update_branding_api_v1_brandings_branding_id_patch) | **PATCH** /api/v1/brandings/{branding_id} | Partial Update Branding
[**update_branding_api_v1_brandings_post**](BrandingApi.md#update_branding_api_v1_brandings_post) | **POST** /api/v1/brandings/ | Update Branding
[**upload_logo_api_v1_brandings_logo_put**](BrandingApi.md#upload_logo_api_v1_brandings_logo_put) | **PUT** /api/v1/brandings/logo | Upload Logo


# **partial_update_branding_api_v1_brandings_branding_id_patch**
> partial_update_branding_api_v1_brandings_branding_id_patch(branding_id, update_branding_dto)

Partial Update Branding

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.update_branding_dto import UpdateBrandingDto
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
    api_instance = openapi_client.BrandingApi(api_client)
    branding_id = 'branding_id_example' # str | 
    update_branding_dto = openapi_client.UpdateBrandingDto() # UpdateBrandingDto | 

    try:
        # Partial Update Branding
        api_instance.partial_update_branding_api_v1_brandings_branding_id_patch(branding_id, update_branding_dto)
    except Exception as e:
        print("Exception when calling BrandingApi->partial_update_branding_api_v1_brandings_branding_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branding_id** | **str**|  | 
 **update_branding_dto** | [**UpdateBrandingDto**](UpdateBrandingDto.md)|  | 

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

# **update_branding_api_v1_brandings_post**
> update_branding_api_v1_brandings_post(update_branding_dto)

Update Branding

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.update_branding_dto import UpdateBrandingDto
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
    api_instance = openapi_client.BrandingApi(api_client)
    update_branding_dto = openapi_client.UpdateBrandingDto() # UpdateBrandingDto | 

    try:
        # Update Branding
        api_instance.update_branding_api_v1_brandings_post(update_branding_dto)
    except Exception as e:
        print("Exception when calling BrandingApi->update_branding_api_v1_brandings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_branding_dto** | [**UpdateBrandingDto**](UpdateBrandingDto.md)|  | 

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

# **upload_logo_api_v1_brandings_logo_put**
> object upload_logo_api_v1_brandings_logo_put(file)

Upload Logo

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
    api_instance = openapi_client.BrandingApi(api_client)
    file = None # bytearray |

    try:
        # Upload Logo
        api_response = api_instance.upload_logo_api_v1_brandings_logo_put(file)
        print("The response of BrandingApi->upload_logo_api_v1_brandings_logo_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->upload_logo_api_v1_brandings_logo_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  |

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

