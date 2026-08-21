# openapi_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_api_v1_users_post**](UsersApi.md#create_user_api_v1_users_post) | **POST** /api/v1/users/ | Create user (deprecated)
[**get_profile_image_api_v1_users_profile_image_key_get**](UsersApi.md#get_profile_image_api_v1_users_profile_image_key_get) | **GET** /api/v1/users/profile/{image_key} | Get profile image URL (deprecated)
[**list_users_api_v1_users_get**](UsersApi.md#list_users_api_v1_users_get) | **GET** /api/v1/users/ | List users (deprecated)
[**patch_user_api_v1_users_user_id_assign_role_patch**](UsersApi.md#patch_user_api_v1_users_user_id_assign_role_patch) | **PATCH** /api/v1/users/{user_id}/assign_role | Assign user role (deprecated)
[**remove_user_role_api_v1_users_user_id_remove_role_patch**](UsersApi.md#remove_user_role_api_v1_users_user_id_remove_role_patch) | **PATCH** /api/v1/users/{user_id}/remove_role | Remove user role (deprecated)
[**update_profile_picture_api_v1_users_user_id_update_profile_picture_put**](UsersApi.md#update_profile_picture_api_v1_users_user_id_update_profile_picture_put) | **PUT** /api/v1/users/{user_id}/update_profile_picture | Update profile picture (deprecated)


# **create_user_api_v1_users_post**
> CreateUserResponseDto create_user_api_v1_users_post(create_user_dto)

Create user (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_user_dto import CreateUserDto
from openapi_client.models.create_user_response_dto import CreateUserResponseDto
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
    api_instance = openapi_client.UsersApi(api_client)
    create_user_dto = openapi_client.CreateUserDto() # CreateUserDto | 

    try:
        # Create user (deprecated)
        api_response = api_instance.create_user_api_v1_users_post(create_user_dto)
        print("The response of UsersApi->create_user_api_v1_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_api_v1_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_dto** | [**CreateUserDto**](CreateUserDto.md)|  | 

### Return type

[**CreateUserResponseDto**](CreateUserResponseDto.md)

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

# **get_profile_image_api_v1_users_profile_image_key_get**
> UserProfileImageUpdateDto get_profile_image_api_v1_users_profile_image_key_get(image_key)

Get profile image URL (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.user_profile_image_update_dto import UserProfileImageUpdateDto
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
    api_instance = openapi_client.UsersApi(api_client)
    image_key = 'image_key_example' # str | 

    try:
        # Get profile image URL (deprecated)
        api_response = api_instance.get_profile_image_api_v1_users_profile_image_key_get(image_key)
        print("The response of UsersApi->get_profile_image_api_v1_users_profile_image_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_profile_image_api_v1_users_profile_image_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_key** | **str**|  | 

### Return type

[**UserProfileImageUpdateDto**](UserProfileImageUpdateDto.md)

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

# **list_users_api_v1_users_get**
> UserListDto list_users_api_v1_users_get(skip=skip, limit=limit)

List users (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.user_list_dto import UserListDto
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
    api_instance = openapi_client.UsersApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # List users (deprecated)
        api_response = api_instance.list_users_api_v1_users_get(skip=skip, limit=limit)
        print("The response of UsersApi->list_users_api_v1_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_users_api_v1_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**UserListDto**](UserListDto.md)

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

# **patch_user_api_v1_users_user_id_assign_role_patch**
> UserDto patch_user_api_v1_users_user_id_assign_role_patch(user_id, user_role_update_request_dto)

Assign user role (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.user_dto import UserDto
from openapi_client.models.user_role_update_request_dto import UserRoleUpdateRequestDto
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
    api_instance = openapi_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    user_role_update_request_dto = openapi_client.UserRoleUpdateRequestDto() # UserRoleUpdateRequestDto | 

    try:
        # Assign user role (deprecated)
        api_response = api_instance.patch_user_api_v1_users_user_id_assign_role_patch(user_id, user_role_update_request_dto)
        print("The response of UsersApi->patch_user_api_v1_users_user_id_assign_role_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->patch_user_api_v1_users_user_id_assign_role_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_role_update_request_dto** | [**UserRoleUpdateRequestDto**](UserRoleUpdateRequestDto.md)|  | 

### Return type

[**UserDto**](UserDto.md)

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

# **remove_user_role_api_v1_users_user_id_remove_role_patch**
> UserDto remove_user_role_api_v1_users_user_id_remove_role_patch(user_id, user_role_update_request_dto)

Remove user role (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.user_dto import UserDto
from openapi_client.models.user_role_update_request_dto import UserRoleUpdateRequestDto
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
    api_instance = openapi_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    user_role_update_request_dto = openapi_client.UserRoleUpdateRequestDto() # UserRoleUpdateRequestDto | 

    try:
        # Remove user role (deprecated)
        api_response = api_instance.remove_user_role_api_v1_users_user_id_remove_role_patch(user_id, user_role_update_request_dto)
        print("The response of UsersApi->remove_user_role_api_v1_users_user_id_remove_role_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->remove_user_role_api_v1_users_user_id_remove_role_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_role_update_request_dto** | [**UserRoleUpdateRequestDto**](UserRoleUpdateRequestDto.md)|  | 

### Return type

[**UserDto**](UserDto.md)

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

# **update_profile_picture_api_v1_users_user_id_update_profile_picture_put**
> UserProfileImageUpdateDto update_profile_picture_api_v1_users_user_id_update_profile_picture_put(user_id, file)

Update profile picture (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.user_profile_image_update_dto import UserProfileImageUpdateDto
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
    api_instance = openapi_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    file = 'file_example' # str | 

    try:
        # Update profile picture (deprecated)
        api_response = api_instance.update_profile_picture_api_v1_users_user_id_update_profile_picture_put(user_id, file)
        print("The response of UsersApi->update_profile_picture_api_v1_users_user_id_update_profile_picture_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_profile_picture_api_v1_users_user_id_update_profile_picture_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **file** | **str**|  | 

### Return type

[**UserProfileImageUpdateDto**](UserProfileImageUpdateDto.md)

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

