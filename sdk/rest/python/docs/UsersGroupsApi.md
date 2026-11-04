# openapi_client.UsersGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_group_api_v1_users_user_id_groups_group_id_post**](UsersGroupsApi.md#add_user_to_group_api_v1_users_user_id_groups_group_id_post) | **POST** /api/v1/users/{user_id}/groups/{group_id} | Add User To Group
[**create_group_api_v1_groups_post**](UsersGroupsApi.md#create_group_api_v1_groups_post) | **POST** /api/v1/groups | Create Group
[**create_organization_api_v1_organizations_post**](UsersGroupsApi.md#create_organization_api_v1_organizations_post) | **POST** /api/v1/organizations | Create Organization
[**create_user_api_v1_users_post**](UsersGroupsApi.md#create_user_api_v1_users_post) | **POST** /api/v1/users | Create User
[**delete_user_api_v1_users_user_id_delete**](UsersGroupsApi.md#delete_user_api_v1_users_user_id_delete) | **DELETE** /api/v1/users/{user_id} | Delete User
[**get_group_api_v1_groups_group_id_get**](UsersGroupsApi.md#get_group_api_v1_groups_group_id_get) | **GET** /api/v1/groups/{group_id} | Get Group
[**get_organization_api_v1_organizations_organization_id_get**](UsersGroupsApi.md#get_organization_api_v1_organizations_organization_id_get) | **GET** /api/v1/organizations/{organization_id} | Get Organization
[**list_groups_api_v1_groups_get**](UsersGroupsApi.md#list_groups_api_v1_groups_get) | **GET** /api/v1/groups | List Groups
[**list_organizations_api_v1_organizations_get**](UsersGroupsApi.md#list_organizations_api_v1_organizations_get) | **GET** /api/v1/organizations | List Organizations
[**list_users_api_v1_users_get**](UsersGroupsApi.md#list_users_api_v1_users_get) | **GET** /api/v1/users | List Users
[**update_user_api_v1_users_user_id_patch**](UsersGroupsApi.md#update_user_api_v1_users_user_id_patch) | **PATCH** /api/v1/users/{user_id} | Update User


# **add_user_to_group_api_v1_users_user_id_groups_group_id_post**
> object add_user_to_group_api_v1_users_user_id_groups_group_id_post(user_id, group_id)

Add User To Group

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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    user_id = 'user_id_example' # str | 
    group_id = 'group_id_example' # str | 

    try:
        # Add User To Group
        api_response = api_instance.add_user_to_group_api_v1_users_user_id_groups_group_id_post(user_id, group_id)
        print("The response of UsersGroupsApi->add_user_to_group_api_v1_users_user_id_groups_group_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->add_user_to_group_api_v1_users_user_id_groups_group_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **group_id** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_api_v1_groups_post**
> GroupResponse create_group_api_v1_groups_post(group_create_body)

Create Group

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.group_create_body import GroupCreateBody
from openapi_client.models.group_response import GroupResponse
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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    group_create_body = openapi_client.GroupCreateBody() # GroupCreateBody | 

    try:
        # Create Group
        api_response = api_instance.create_group_api_v1_groups_post(group_create_body)
        print("The response of UsersGroupsApi->create_group_api_v1_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->create_group_api_v1_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_create_body** | [**GroupCreateBody**](GroupCreateBody.md)|  | 

### Return type

[**GroupResponse**](GroupResponse.md)

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

# **create_organization_api_v1_organizations_post**
> OrganizationResponse create_organization_api_v1_organizations_post(organization_create_body)

Create Organization

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.organization_create_body import OrganizationCreateBody
from openapi_client.models.organization_response import OrganizationResponse
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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    organization_create_body = openapi_client.OrganizationCreateBody() # OrganizationCreateBody | 

    try:
        # Create Organization
        api_response = api_instance.create_organization_api_v1_organizations_post(organization_create_body)
        print("The response of UsersGroupsApi->create_organization_api_v1_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->create_organization_api_v1_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_create_body** | [**OrganizationCreateBody**](OrganizationCreateBody.md)|  | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

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

# **create_user_api_v1_users_post**
> UserResponse create_user_api_v1_users_post(user_create_body)

Create User

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.user_create_body import UserCreateBody
from openapi_client.models.user_response import UserResponse
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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    user_create_body = openapi_client.UserCreateBody() # UserCreateBody | 

    try:
        # Create User
        api_response = api_instance.create_user_api_v1_users_post(user_create_body)
        print("The response of UsersGroupsApi->create_user_api_v1_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->create_user_api_v1_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_body** | [**UserCreateBody**](UserCreateBody.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **delete_user_api_v1_users_user_id_delete**
> delete_user_api_v1_users_user_id_delete(user_id)

Delete User

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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Delete User
        api_instance.delete_user_api_v1_users_user_id_delete(user_id)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->delete_user_api_v1_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

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

# **get_group_api_v1_groups_group_id_get**
> GroupResponse get_group_api_v1_groups_group_id_get(group_id)

Get Group

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.group_response import GroupResponse
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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    group_id = 'group_id_example' # str | 

    try:
        # Get Group
        api_response = api_instance.get_group_api_v1_groups_group_id_get(group_id)
        print("The response of UsersGroupsApi->get_group_api_v1_groups_group_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->get_group_api_v1_groups_group_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_api_v1_organizations_organization_id_get**
> OrganizationResponse get_organization_api_v1_organizations_organization_id_get(organization_id)

Get Organization

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.organization_response import OrganizationResponse
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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get Organization
        api_response = api_instance.get_organization_api_v1_organizations_organization_id_get(organization_id)
        print("The response of UsersGroupsApi->get_organization_api_v1_organizations_organization_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->get_organization_api_v1_organizations_organization_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Organization not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups_api_v1_groups_get**
> GroupListPage list_groups_api_v1_groups_get(limit=limit, offset=offset, q=q)

List Groups

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.group_list_page import GroupListPage
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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    q = 'q_example' # str | Case-insensitive search on name or description (optional)

    try:
        # List Groups
        api_response = api_instance.list_groups_api_v1_groups_get(limit=limit, offset=offset, q=q)
        print("The response of UsersGroupsApi->list_groups_api_v1_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->list_groups_api_v1_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **q** | **str**| Case-insensitive search on name or description | [optional] 

### Return type

[**GroupListPage**](GroupListPage.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organizations_api_v1_organizations_get**
> OrganizationListPage list_organizations_api_v1_organizations_get(limit=limit, offset=offset, q=q)

List Organizations

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.organization_list_page import OrganizationListPage
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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    q = 'q_example' # str | Case-insensitive search on legal name (optional)

    try:
        # List Organizations
        api_response = api_instance.list_organizations_api_v1_organizations_get(limit=limit, offset=offset, q=q)
        print("The response of UsersGroupsApi->list_organizations_api_v1_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->list_organizations_api_v1_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **q** | **str**| Case-insensitive search on legal name | [optional] 

### Return type

[**OrganizationListPage**](OrganizationListPage.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_api_v1_users_get**
> UserListPage list_users_api_v1_users_get(limit=limit, offset=offset, q=q)

List Users

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.user_list_page import UserListPage
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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    q = 'q_example' # str |  (optional)

    try:
        # List Users
        api_response = api_instance.list_users_api_v1_users_get(limit=limit, offset=offset, q=q)
        print("The response of UsersGroupsApi->list_users_api_v1_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->list_users_api_v1_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **q** | **str**|  | [optional] 

### Return type

[**UserListPage**](UserListPage.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_api_v1_users_user_id_patch**
> UserResponse update_user_api_v1_users_user_id_patch(user_id, user_update_body)

Update User

### Example

* Bearer Authentication (HTTPBearer):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.user_response import UserResponse
from openapi_client.models.user_update_body import UserUpdateBody
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
    api_instance = openapi_client.UsersGroupsApi(api_client)
    user_id = 'user_id_example' # str | 
    user_update_body = openapi_client.UserUpdateBody() # UserUpdateBody | 

    try:
        # Update User
        api_response = api_instance.update_user_api_v1_users_user_id_patch(user_id, user_update_body)
        print("The response of UsersGroupsApi->update_user_api_v1_users_user_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersGroupsApi->update_user_api_v1_users_user_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_update_body** | [**UserUpdateBody**](UserUpdateBody.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

