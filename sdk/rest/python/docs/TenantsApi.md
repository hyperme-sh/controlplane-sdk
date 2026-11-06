# openapi_client.TenantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_dns_status_api_v1_tenants_tenant_id_check_dns_get**](TenantsApi.md#check_dns_status_api_v1_tenants_tenant_id_check_dns_get) | **GET** /api/v1/tenants/{tenant_id}/check_dns | Check Dns Status
[**check_subdomain_availability_api_v1_tenants_check_subdomain_subdomain_get**](TenantsApi.md#check_subdomain_availability_api_v1_tenants_check_subdomain_subdomain_get) | **GET** /api/v1/tenants/check_subdomain/{subdomain} | Check Subdomain Availability
[**create_tenant_api_v1_tenants_post**](TenantsApi.md#create_tenant_api_v1_tenants_post) | **POST** /api/v1/tenants/ | Create Tenant
[**delete_tenant_api_v1_tenants_id_delete**](TenantsApi.md#delete_tenant_api_v1_tenants_id_delete) | **DELETE** /api/v1/tenants/{id} | Delete Tenant
[**get_tenant_features_api_v1_tenants_tenant_id_features_get**](TenantsApi.md#get_tenant_features_api_v1_tenants_tenant_id_features_get) | **GET** /api/v1/tenants/{tenant_id}/features | Get Tenant Features
[**list_tenants_api_v1_tenants_get**](TenantsApi.md#list_tenants_api_v1_tenants_get) | **GET** /api/v1/tenants/ | List Tenants
[**search_by_name_api_v1_tenants_search_by_name_name_get**](TenantsApi.md#search_by_name_api_v1_tenants_search_by_name_name_get) | **GET** /api/v1/tenants/search_by_name/{name} | Search By Name
[**search_by_subdomain_api_v1_tenants_search_by_subdomain_subdomain_get**](TenantsApi.md#search_by_subdomain_api_v1_tenants_search_by_subdomain_subdomain_get) | **GET** /api/v1/tenants/search_by_subdomain/{subdomain} | Search By Subdomain
[**update_tenant_api_v1_tenants_tenant_id_put**](TenantsApi.md#update_tenant_api_v1_tenants_tenant_id_put) | **PUT** /api/v1/tenants/{tenant_id} | Update Tenant
[**update_tenant_dns_record_api_v1_tenants_tenant_id_update_dns_post**](TenantsApi.md#update_tenant_dns_record_api_v1_tenants_tenant_id_update_dns_post) | **POST** /api/v1/tenants/{tenant_id}/update_dns | Update Tenant Dns Record
[**update_tenant_feature_api_v1_tenants_tenant_id_update_feature_patch**](TenantsApi.md#update_tenant_feature_api_v1_tenants_tenant_id_update_feature_patch) | **PATCH** /api/v1/tenants/{tenant_id}/update_feature | Update Tenant Feature


# **check_dns_status_api_v1_tenants_tenant_id_check_dns_get**
> UpdateTenantResponseDto check_dns_status_api_v1_tenants_tenant_id_check_dns_get(tenant_id)

Check Dns Status

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.update_tenant_response_dto import UpdateTenantResponseDto
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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Check Dns Status
        api_response = api_instance.check_dns_status_api_v1_tenants_tenant_id_check_dns_get(tenant_id)
        print("The response of TenantsApi->check_dns_status_api_v1_tenants_tenant_id_check_dns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->check_dns_status_api_v1_tenants_tenant_id_check_dns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

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

# **check_subdomain_availability_api_v1_tenants_check_subdomain_subdomain_get**
> SubdomainAvailabilityDto check_subdomain_availability_api_v1_tenants_check_subdomain_subdomain_get(subdomain)

Check Subdomain Availability

### Example


```python
import openapi_client
from openapi_client.models.subdomain_availability_dto import SubdomainAvailabilityDto
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
    api_instance = openapi_client.TenantsApi(api_client)
    subdomain = 'subdomain_example' # str | 

    try:
        # Check Subdomain Availability
        api_response = api_instance.check_subdomain_availability_api_v1_tenants_check_subdomain_subdomain_get(subdomain)
        print("The response of TenantsApi->check_subdomain_availability_api_v1_tenants_check_subdomain_subdomain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->check_subdomain_availability_api_v1_tenants_check_subdomain_subdomain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomain** | **str**|  | 

### Return type

[**SubdomainAvailabilityDto**](SubdomainAvailabilityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tenant_api_v1_tenants_post**
> CreateTenantResponseDto create_tenant_api_v1_tenants_post(create_tenant_dto)

Create Tenant

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_tenant_dto import CreateTenantDto
from openapi_client.models.create_tenant_response_dto import CreateTenantResponseDto
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
    api_instance = openapi_client.TenantsApi(api_client)
    create_tenant_dto = openapi_client.CreateTenantDto() # CreateTenantDto | 

    try:
        # Create Tenant
        api_response = api_instance.create_tenant_api_v1_tenants_post(create_tenant_dto)
        print("The response of TenantsApi->create_tenant_api_v1_tenants_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->create_tenant_api_v1_tenants_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_dto** | [**CreateTenantDto**](CreateTenantDto.md)|  | 

### Return type

[**CreateTenantResponseDto**](CreateTenantResponseDto.md)

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

# **delete_tenant_api_v1_tenants_id_delete**
> object delete_tenant_api_v1_tenants_id_delete(id)

Delete Tenant

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
    api_instance = openapi_client.TenantsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Tenant
        api_response = api_instance.delete_tenant_api_v1_tenants_id_delete(id)
        print("The response of TenantsApi->delete_tenant_api_v1_tenants_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->delete_tenant_api_v1_tenants_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_tenant_features_api_v1_tenants_tenant_id_features_get**
> List[FeatureDto] get_tenant_features_api_v1_tenants_tenant_id_features_get(tenant_id)

Get Tenant Features

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.feature_dto import FeatureDto
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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get Tenant Features
        api_response = api_instance.get_tenant_features_api_v1_tenants_tenant_id_features_get(tenant_id)
        print("The response of TenantsApi->get_tenant_features_api_v1_tenants_tenant_id_features_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_features_api_v1_tenants_tenant_id_features_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**List[FeatureDto]**](FeatureDto.md)

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

# **list_tenants_api_v1_tenants_get**
> TenantListDto list_tenants_api_v1_tenants_get(skip=skip, limit=limit)

List Tenants

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.tenant_list_dto import TenantListDto
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
    api_instance = openapi_client.TenantsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # List Tenants
        api_response = api_instance.list_tenants_api_v1_tenants_get(skip=skip, limit=limit)
        print("The response of TenantsApi->list_tenants_api_v1_tenants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->list_tenants_api_v1_tenants_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**TenantListDto**](TenantListDto.md)

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

# **search_by_name_api_v1_tenants_search_by_name_name_get**
> TenantDto search_by_name_api_v1_tenants_search_by_name_name_get(name)

Search By Name

### Example


```python
import openapi_client
from openapi_client.models.tenant_dto import TenantDto
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
    api_instance = openapi_client.TenantsApi(api_client)
    name = 'name_example' # str | 

    try:
        # Search By Name
        api_response = api_instance.search_by_name_api_v1_tenants_search_by_name_name_get(name)
        print("The response of TenantsApi->search_by_name_api_v1_tenants_search_by_name_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->search_by_name_api_v1_tenants_search_by_name_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**TenantDto**](TenantDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_by_subdomain_api_v1_tenants_search_by_subdomain_subdomain_get**
> TenantDto search_by_subdomain_api_v1_tenants_search_by_subdomain_subdomain_get(subdomain)

Search By Subdomain

### Example


```python
import openapi_client
from openapi_client.models.tenant_dto import TenantDto
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
    api_instance = openapi_client.TenantsApi(api_client)
    subdomain = 'subdomain_example' # str | 

    try:
        # Search By Subdomain
        api_response = api_instance.search_by_subdomain_api_v1_tenants_search_by_subdomain_subdomain_get(subdomain)
        print("The response of TenantsApi->search_by_subdomain_api_v1_tenants_search_by_subdomain_subdomain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->search_by_subdomain_api_v1_tenants_search_by_subdomain_subdomain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomain** | **str**|  | 

### Return type

[**TenantDto**](TenantDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_api_v1_tenants_tenant_id_put**
> update_tenant_api_v1_tenants_tenant_id_put(tenant_id, update_tenant_dto)

Update Tenant

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.update_tenant_dto import UpdateTenantDto
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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    update_tenant_dto = openapi_client.UpdateTenantDto() # UpdateTenantDto | 

    try:
        # Update Tenant
        api_instance.update_tenant_api_v1_tenants_tenant_id_put(tenant_id, update_tenant_dto)
    except Exception as e:
        print("Exception when calling TenantsApi->update_tenant_api_v1_tenants_tenant_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **update_tenant_dto** | [**UpdateTenantDto**](UpdateTenantDto.md)|  | 

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

# **update_tenant_dns_record_api_v1_tenants_tenant_id_update_dns_post**
> UpdateTenantResponseDto update_tenant_dns_record_api_v1_tenants_tenant_id_update_dns_post(tenant_id, update_tenant_dto)

Update Tenant Dns Record

When bringing your own domain you must map the DNS records for your custom domain to point to our main domain.                 You can do this by adding a CNAME record in your domain's DNS settings.                 Here is an example of how to set it up:                 Type: CNAME                 Name: app                 Value: fsrapp.com

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.update_tenant_dto import UpdateTenantDto
from openapi_client.models.update_tenant_response_dto import UpdateTenantResponseDto
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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    update_tenant_dto = openapi_client.UpdateTenantDto() # UpdateTenantDto | 

    try:
        # Update Tenant Dns Record
        api_response = api_instance.update_tenant_dns_record_api_v1_tenants_tenant_id_update_dns_post(tenant_id, update_tenant_dto)
        print("The response of TenantsApi->update_tenant_dns_record_api_v1_tenants_tenant_id_update_dns_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->update_tenant_dns_record_api_v1_tenants_tenant_id_update_dns_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **update_tenant_dto** | [**UpdateTenantDto**](UpdateTenantDto.md)|  | 

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_feature_api_v1_tenants_tenant_id_update_feature_patch**
> UpdateTenantResponseDto update_tenant_feature_api_v1_tenants_tenant_id_update_feature_patch(tenant_id, feature_dto)

Update Tenant Feature

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.feature_dto import FeatureDto
from openapi_client.models.update_tenant_response_dto import UpdateTenantResponseDto
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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    feature_dto = openapi_client.FeatureDto() # FeatureDto | 

    try:
        # Update Tenant Feature
        api_response = api_instance.update_tenant_feature_api_v1_tenants_tenant_id_update_feature_patch(tenant_id, feature_dto)
        print("The response of TenantsApi->update_tenant_feature_api_v1_tenants_tenant_id_update_feature_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->update_tenant_feature_api_v1_tenants_tenant_id_update_feature_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **feature_dto** | [**FeatureDto**](FeatureDto.md)|  | 

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

