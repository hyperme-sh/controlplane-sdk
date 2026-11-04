# openapi_client.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_api_v1_roles_post**](RolesApi.md#create_role_api_v1_roles_post) | **POST** /api/v1/roles/ | Create Role
[**delete_role_api_v1_roles_role_id_delete**](RolesApi.md#delete_role_api_v1_roles_role_id_delete) | **DELETE** /api/v1/roles/{role_id} | Delete Role
[**get_role_api_v1_roles_role_id_get**](RolesApi.md#get_role_api_v1_roles_role_id_get) | **GET** /api/v1/roles/{role_id} | Get Role
[**list_roles_api_v1_roles_get**](RolesApi.md#list_roles_api_v1_roles_get) | **GET** /api/v1/roles/ | List Roles
[**search_role_by_name_api_v1_roles_search_by_name_get**](RolesApi.md#search_role_by_name_api_v1_roles_search_by_name_get) | **GET** /api/v1/roles/search_by_name | Search Role By Name
[**update_role_api_v1_roles_role_id_put**](RolesApi.md#update_role_api_v1_roles_role_id_put) | **PUT** /api/v1/roles/{role_id} | Update Role


# **create_role_api_v1_roles_post**
> CreateRoleResponseDto create_role_api_v1_roles_post(create_role_dto)

Create Role

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_role_dto import CreateRoleDto
from openapi_client.models.create_role_response_dto import CreateRoleResponseDto
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
    api_instance = openapi_client.RolesApi(api_client)
    create_role_dto = openapi_client.CreateRoleDto() # CreateRoleDto | 

    try:
        # Create Role
        api_response = api_instance.create_role_api_v1_roles_post(create_role_dto)
        print("The response of RolesApi->create_role_api_v1_roles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_role_api_v1_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_role_dto** | [**CreateRoleDto**](CreateRoleDto.md)|  | 

### Return type

[**CreateRoleResponseDto**](CreateRoleResponseDto.md)

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

# **delete_role_api_v1_roles_role_id_delete**
> object delete_role_api_v1_roles_role_id_delete(role_id)

Delete Role

Deletes a role if it is not assigned to any users.

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
    api_instance = openapi_client.RolesApi(api_client)
    role_id = 'role_id_example' # str | 

    try:
        # Delete Role
        api_response = api_instance.delete_role_api_v1_roles_role_id_delete(role_id)
        print("The response of RolesApi->delete_role_api_v1_roles_role_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role_api_v1_roles_role_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  | 

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

# **get_role_api_v1_roles_role_id_get**
> RoleDto get_role_api_v1_roles_role_id_get(role_id)

Get Role

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.role_dto import RoleDto
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
    api_instance = openapi_client.RolesApi(api_client)
    role_id = 'role_id_example' # str | 

    try:
        # Get Role
        api_response = api_instance.get_role_api_v1_roles_role_id_get(role_id)
        print("The response of RolesApi->get_role_api_v1_roles_role_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_api_v1_roles_role_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  | 

### Return type

[**RoleDto**](RoleDto.md)

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

# **list_roles_api_v1_roles_get**
> RoleListDto list_roles_api_v1_roles_get(skip=skip, limit=limit)

List Roles

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.role_list_dto import RoleListDto
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
    api_instance = openapi_client.RolesApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # List Roles
        api_response = api_instance.list_roles_api_v1_roles_get(skip=skip, limit=limit)
        print("The response of RolesApi->list_roles_api_v1_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->list_roles_api_v1_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**RoleListDto**](RoleListDto.md)

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

# **search_role_by_name_api_v1_roles_search_by_name_get**
> List[RoleDto] search_role_by_name_api_v1_roles_search_by_name_get(name)

Search Role By Name

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.role_dto import RoleDto
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
    api_instance = openapi_client.RolesApi(api_client)
    name = 'name_example' # str | 

    try:
        # Search Role By Name
        api_response = api_instance.search_role_by_name_api_v1_roles_search_by_name_get(name)
        print("The response of RolesApi->search_role_by_name_api_v1_roles_search_by_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->search_role_by_name_api_v1_roles_search_by_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**List[RoleDto]**](RoleDto.md)

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

# **update_role_api_v1_roles_role_id_put**
> RoleDto update_role_api_v1_roles_role_id_put(role_id, update_role_dto)

Update Role

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.role_dto import RoleDto
from openapi_client.models.update_role_dto import UpdateRoleDto
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
    api_instance = openapi_client.RolesApi(api_client)
    role_id = 'role_id_example' # str | 
    update_role_dto = openapi_client.UpdateRoleDto() # UpdateRoleDto | 

    try:
        # Update Role
        api_response = api_instance.update_role_api_v1_roles_role_id_put(role_id, update_role_dto)
        print("The response of RolesApi->update_role_api_v1_roles_role_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->update_role_api_v1_roles_role_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  | 
 **update_role_dto** | [**UpdateRoleDto**](UpdateRoleDto.md)|  | 

### Return type

[**RoleDto**](RoleDto.md)

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

