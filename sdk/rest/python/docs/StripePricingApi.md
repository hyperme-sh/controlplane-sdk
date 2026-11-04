# openapi_client.StripePricingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_api_v1_prices_post**](StripePricingApi.md#create_pricing_api_v1_prices_post) | **POST** /api/v1/prices/ | Create Pricing
[**get_pricing_list_api_v1_prices_get**](StripePricingApi.md#get_pricing_list_api_v1_prices_get) | **GET** /api/v1/prices/ | Get Pricing List
[**update_pricing_api_v1_prices_price_id_patch**](StripePricingApi.md#update_pricing_api_v1_prices_price_id_patch) | **PATCH** /api/v1/prices/{price_id} | Update Pricing


# **create_pricing_api_v1_prices_post**
> object create_pricing_api_v1_prices_post(create_pricing_dto)

Create Pricing

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_pricing_dto import CreatePricingDto
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
    api_instance = openapi_client.StripePricingApi(api_client)
    create_pricing_dto = openapi_client.CreatePricingDto() # CreatePricingDto | 

    try:
        # Create Pricing
        api_response = api_instance.create_pricing_api_v1_prices_post(create_pricing_dto)
        print("The response of StripePricingApi->create_pricing_api_v1_prices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripePricingApi->create_pricing_api_v1_prices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pricing_dto** | [**CreatePricingDto**](CreatePricingDto.md)|  | 

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

# **get_pricing_list_api_v1_prices_get**
> PricingListDto get_pricing_list_api_v1_prices_get()

Get Pricing List

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.pricing_list_dto import PricingListDto
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
    api_instance = openapi_client.StripePricingApi(api_client)

    try:
        # Get Pricing List
        api_response = api_instance.get_pricing_list_api_v1_prices_get()
        print("The response of StripePricingApi->get_pricing_list_api_v1_prices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripePricingApi->get_pricing_list_api_v1_prices_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PricingListDto**](PricingListDto.md)

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

# **update_pricing_api_v1_prices_price_id_patch**
> update_pricing_api_v1_prices_price_id_patch(price_id, update_pricing_dto)

Update Pricing

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.update_pricing_dto import UpdatePricingDto
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
    api_instance = openapi_client.StripePricingApi(api_client)
    price_id = 'price_id_example' # str | 
    update_pricing_dto = openapi_client.UpdatePricingDto() # UpdatePricingDto | 

    try:
        # Update Pricing
        api_instance.update_pricing_api_v1_prices_price_id_patch(price_id, update_pricing_dto)
    except Exception as e:
        print("Exception when calling StripePricingApi->update_pricing_api_v1_prices_price_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_id** | **str**|  | 
 **update_pricing_dto** | [**UpdatePricingDto**](UpdatePricingDto.md)|  | 

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

