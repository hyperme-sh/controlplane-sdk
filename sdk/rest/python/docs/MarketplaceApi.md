# openapi_client.MarketplaceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_listing_api_v1_marketplace_listings_post**](MarketplaceApi.md#create_listing_api_v1_marketplace_listings_post) | **POST** /api/v1/marketplace/listings | Create Listing
[**delete_listing_api_v1_marketplace_listings_listing_id_delete**](MarketplaceApi.md#delete_listing_api_v1_marketplace_listings_listing_id_delete) | **DELETE** /api/v1/marketplace/listings/{listing_id} | Delete Listing
[**get_listing_api_v1_marketplace_listings_listing_id_get**](MarketplaceApi.md#get_listing_api_v1_marketplace_listings_listing_id_get) | **GET** /api/v1/marketplace/listings/{listing_id} | Get Listing
[**list_listings_api_v1_marketplace_listings_get**](MarketplaceApi.md#list_listings_api_v1_marketplace_listings_get) | **GET** /api/v1/marketplace/listings | List Listings
[**purchase_listing_api_v1_marketplace_listings_listing_id_purchase_post**](MarketplaceApi.md#purchase_listing_api_v1_marketplace_listings_listing_id_purchase_post) | **POST** /api/v1/marketplace/listings/{listing_id}/purchase | Purchase Listing
[**update_listing_api_v1_marketplace_listings_listing_id_patch**](MarketplaceApi.md#update_listing_api_v1_marketplace_listings_listing_id_patch) | **PATCH** /api/v1/marketplace/listings/{listing_id} | Update Listing


# **create_listing_api_v1_marketplace_listings_post**
> ListingResponse create_listing_api_v1_marketplace_listings_post(listing_create_body)

Create Listing

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.listing_create_body import ListingCreateBody
from openapi_client.models.listing_response import ListingResponse
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
    api_instance = openapi_client.MarketplaceApi(api_client)
    listing_create_body = openapi_client.ListingCreateBody() # ListingCreateBody | 

    try:
        # Create Listing
        api_response = api_instance.create_listing_api_v1_marketplace_listings_post(listing_create_body)
        print("The response of MarketplaceApi->create_listing_api_v1_marketplace_listings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->create_listing_api_v1_marketplace_listings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_create_body** | [**ListingCreateBody**](ListingCreateBody.md)|  | 

### Return type

[**ListingResponse**](ListingResponse.md)

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

# **delete_listing_api_v1_marketplace_listings_listing_id_delete**
> delete_listing_api_v1_marketplace_listings_listing_id_delete(listing_id)

Delete Listing

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
    api_instance = openapi_client.MarketplaceApi(api_client)
    listing_id = 'listing_id_example' # str | 

    try:
        # Delete Listing
        api_instance.delete_listing_api_v1_marketplace_listings_listing_id_delete(listing_id)
    except Exception as e:
        print("Exception when calling MarketplaceApi->delete_listing_api_v1_marketplace_listings_listing_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_api_v1_marketplace_listings_listing_id_get**
> ListingResponse get_listing_api_v1_marketplace_listings_listing_id_get(listing_id)

Get Listing

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.listing_response import ListingResponse
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
    api_instance = openapi_client.MarketplaceApi(api_client)
    listing_id = 'listing_id_example' # str | 

    try:
        # Get Listing
        api_response = api_instance.get_listing_api_v1_marketplace_listings_listing_id_get(listing_id)
        print("The response of MarketplaceApi->get_listing_api_v1_marketplace_listings_listing_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_listing_api_v1_marketplace_listings_listing_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **str**|  | 

### Return type

[**ListingResponse**](ListingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_listings_api_v1_marketplace_listings_get**
> List[ListingResponse] list_listings_api_v1_marketplace_listings_get(public_only=public_only)

List Listings

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.listing_response import ListingResponse
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
    api_instance = openapi_client.MarketplaceApi(api_client)
    public_only = False # bool |  (optional) (default to False)

    try:
        # List Listings
        api_response = api_instance.list_listings_api_v1_marketplace_listings_get(public_only=public_only)
        print("The response of MarketplaceApi->list_listings_api_v1_marketplace_listings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->list_listings_api_v1_marketplace_listings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_only** | **bool**|  | [optional] [default to False]

### Return type

[**List[ListingResponse]**](ListingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_listing_api_v1_marketplace_listings_listing_id_purchase_post**
> PurchaseResponse purchase_listing_api_v1_marketplace_listings_listing_id_purchase_post(listing_id, purchase_listing_body=purchase_listing_body)

Purchase Listing

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.purchase_listing_body import PurchaseListingBody
from openapi_client.models.purchase_response import PurchaseResponse
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
    api_instance = openapi_client.MarketplaceApi(api_client)
    listing_id = 'listing_id_example' # str | 
    purchase_listing_body = openapi_client.PurchaseListingBody() # PurchaseListingBody |  (optional)

    try:
        # Purchase Listing
        api_response = api_instance.purchase_listing_api_v1_marketplace_listings_listing_id_purchase_post(listing_id, purchase_listing_body=purchase_listing_body)
        print("The response of MarketplaceApi->purchase_listing_api_v1_marketplace_listings_listing_id_purchase_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->purchase_listing_api_v1_marketplace_listings_listing_id_purchase_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **str**|  | 
 **purchase_listing_body** | [**PurchaseListingBody**](PurchaseListingBody.md)|  | [optional] 

### Return type

[**PurchaseResponse**](PurchaseResponse.md)

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

# **update_listing_api_v1_marketplace_listings_listing_id_patch**
> ListingResponse update_listing_api_v1_marketplace_listings_listing_id_patch(listing_id, listing_update_body)

Update Listing

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.listing_response import ListingResponse
from openapi_client.models.listing_update_body import ListingUpdateBody
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
    api_instance = openapi_client.MarketplaceApi(api_client)
    listing_id = 'listing_id_example' # str | 
    listing_update_body = openapi_client.ListingUpdateBody() # ListingUpdateBody | 

    try:
        # Update Listing
        api_response = api_instance.update_listing_api_v1_marketplace_listings_listing_id_patch(listing_id, listing_update_body)
        print("The response of MarketplaceApi->update_listing_api_v1_marketplace_listings_listing_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->update_listing_api_v1_marketplace_listings_listing_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **str**|  | 
 **listing_update_body** | [**ListingUpdateBody**](ListingUpdateBody.md)|  | 

### Return type

[**ListingResponse**](ListingResponse.md)

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

