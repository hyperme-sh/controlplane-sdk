# openapi_client.StripeProductsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_api_v1_products_post**](StripeProductsApi.md#create_product_api_v1_products_post) | **POST** /api/v1/products/ | Create a Product
[**delete_product_api_v1_products_product_id_delete**](StripeProductsApi.md#delete_product_api_v1_products_product_id_delete) | **DELETE** /api/v1/products/{product_id} | Delete a Product
[**get_product_by_id_api_v1_products_product_id_get**](StripeProductsApi.md#get_product_by_id_api_v1_products_product_id_get) | **GET** /api/v1/products/{product_id} | Get Product by ID
[**list_products_api_v1_products_get**](StripeProductsApi.md#list_products_api_v1_products_get) | **GET** /api/v1/products/ | List Products
[**update_product_api_v1_products_product_id_patch**](StripeProductsApi.md#update_product_api_v1_products_product_id_patch) | **PATCH** /api/v1/products/{product_id} | Update a Product


# **create_product_api_v1_products_post**
> object create_product_api_v1_products_post(create_product_dto)

Create a Product

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_product_dto import CreateProductDto
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
    api_instance = openapi_client.StripeProductsApi(api_client)
    create_product_dto = openapi_client.CreateProductDto() # CreateProductDto | 

    try:
        # Create a Product
        api_response = api_instance.create_product_api_v1_products_post(create_product_dto)
        print("The response of StripeProductsApi->create_product_api_v1_products_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeProductsApi->create_product_api_v1_products_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_product_dto** | [**CreateProductDto**](CreateProductDto.md)|  | 

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

# **delete_product_api_v1_products_product_id_delete**
> object delete_product_api_v1_products_product_id_delete(product_id)

Delete a Product

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
    api_instance = openapi_client.StripeProductsApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        # Delete a Product
        api_response = api_instance.delete_product_api_v1_products_product_id_delete(product_id)
        print("The response of StripeProductsApi->delete_product_api_v1_products_product_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeProductsApi->delete_product_api_v1_products_product_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

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

# **get_product_by_id_api_v1_products_product_id_get**
> ProductDto get_product_by_id_api_v1_products_product_id_get(product_id)

Get Product by ID

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.product_dto import ProductDto
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
    api_instance = openapi_client.StripeProductsApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        # Get Product by ID
        api_response = api_instance.get_product_by_id_api_v1_products_product_id_get(product_id)
        print("The response of StripeProductsApi->get_product_by_id_api_v1_products_product_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeProductsApi->get_product_by_id_api_v1_products_product_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

### Return type

[**ProductDto**](ProductDto.md)

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

# **list_products_api_v1_products_get**
> ProductListDto list_products_api_v1_products_get(active=active)

List Products

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.product_list_dto import ProductListDto
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
    api_instance = openapi_client.StripeProductsApi(api_client)
    active = True # bool | Filter active products, defaults to True (optional) (default to True)

    try:
        # List Products
        api_response = api_instance.list_products_api_v1_products_get(active=active)
        print("The response of StripeProductsApi->list_products_api_v1_products_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeProductsApi->list_products_api_v1_products_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**| Filter active products, defaults to True | [optional] [default to True]

### Return type

[**ProductListDto**](ProductListDto.md)

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

# **update_product_api_v1_products_product_id_patch**
> update_product_api_v1_products_product_id_patch(product_id, create_product_dto)

Update a Product

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_product_dto import CreateProductDto
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
    api_instance = openapi_client.StripeProductsApi(api_client)
    product_id = 'product_id_example' # str | 
    create_product_dto = openapi_client.CreateProductDto() # CreateProductDto | 

    try:
        # Update a Product
        api_instance.update_product_api_v1_products_product_id_patch(product_id, create_product_dto)
    except Exception as e:
        print("Exception when calling StripeProductsApi->update_product_api_v1_products_product_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **create_product_dto** | [**CreateProductDto**](CreateProductDto.md)|  | 

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

