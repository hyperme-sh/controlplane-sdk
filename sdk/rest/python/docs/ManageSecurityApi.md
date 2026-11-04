# openapi_client.ManageSecurityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_registered_passkey_api_v1_security_passkeys_credential_id_delete**](ManageSecurityApi.md#delete_registered_passkey_api_v1_security_passkeys_credential_id_delete) | **DELETE** /api/v1/security/passkeys/{credential_id} | Delete Registered Passkey
[**get_registered_passkeys_api_v1_security_passkeys_get**](ManageSecurityApi.md#get_registered_passkeys_api_v1_security_passkeys_get) | **GET** /api/v1/security/passkeys | Get Registered Passkeys


# **delete_registered_passkey_api_v1_security_passkeys_credential_id_delete**
> delete_registered_passkey_api_v1_security_passkeys_credential_id_delete(credential_id)

Delete Registered Passkey

Endpoint to delete a registered passkey for the current user.

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
    api_instance = openapi_client.ManageSecurityApi(api_client)
    credential_id = 'credential_id_example' # str | 

    try:
        # Delete Registered Passkey
        api_instance.delete_registered_passkey_api_v1_security_passkeys_credential_id_delete(credential_id)
    except Exception as e:
        print("Exception when calling ManageSecurityApi->delete_registered_passkey_api_v1_security_passkeys_credential_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registered_passkeys_api_v1_security_passkeys_get**
> List[RegisteredPasskeyCredentialsDto] get_registered_passkeys_api_v1_security_passkeys_get()

Get Registered Passkeys

Endpoint to retrieve registered passkeys for the current user.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.registered_passkey_credentials_dto import RegisteredPasskeyCredentialsDto
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
    api_instance = openapi_client.ManageSecurityApi(api_client)

    try:
        # Get Registered Passkeys
        api_response = api_instance.get_registered_passkeys_api_v1_security_passkeys_get()
        print("The response of ManageSecurityApi->get_registered_passkeys_api_v1_security_passkeys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageSecurityApi->get_registered_passkeys_api_v1_security_passkeys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RegisteredPasskeyCredentialsDto]**](RegisteredPasskeyCredentialsDto.md)

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

