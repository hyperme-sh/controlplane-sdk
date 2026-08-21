# openapi_client.AuditLogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_audit_logs_api_v1_audit_logs_download_post**](AuditLogsApi.md#download_audit_logs_api_v1_audit_logs_download_post) | **POST** /api/v1/audit-logs/download | Download Audit Logs
[**list_audit_logs_api_v1_audit_logs_get**](AuditLogsApi.md#list_audit_logs_api_v1_audit_logs_get) | **GET** /api/v1/audit-logs/ | List Audit Logs


# **download_audit_logs_api_v1_audit_logs_download_post**
> DownloadResponseDto download_audit_logs_api_v1_audit_logs_download_post(download_audit_request_dto)

Download Audit Logs

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.download_audit_request_dto import DownloadAuditRequestDto
from openapi_client.models.download_response_dto import DownloadResponseDto
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
    api_instance = openapi_client.AuditLogsApi(api_client)
    download_audit_request_dto = openapi_client.DownloadAuditRequestDto() # DownloadAuditRequestDto | 

    try:
        # Download Audit Logs
        api_response = api_instance.download_audit_logs_api_v1_audit_logs_download_post(download_audit_request_dto)
        print("The response of AuditLogsApi->download_audit_logs_api_v1_audit_logs_download_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogsApi->download_audit_logs_api_v1_audit_logs_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_audit_request_dto** | [**DownloadAuditRequestDto**](DownloadAuditRequestDto.md)|  | 

### Return type

[**DownloadResponseDto**](DownloadResponseDto.md)

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

# **list_audit_logs_api_v1_audit_logs_get**
> AuditLogListDto list_audit_logs_api_v1_audit_logs_get(limit=limit, skip=skip, action=action)

List Audit Logs

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.audit_log_list_dto import AuditLogListDto
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
    api_instance = openapi_client.AuditLogsApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    skip = 0 # int |  (optional) (default to 0)
    action = 'action_example' # str |  (optional)

    try:
        # List Audit Logs
        api_response = api_instance.list_audit_logs_api_v1_audit_logs_get(limit=limit, skip=skip, action=action)
        print("The response of AuditLogsApi->list_audit_logs_api_v1_audit_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogsApi->list_audit_logs_api_v1_audit_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**|  | [optional] [default to 0]
 **action** | **str**|  | [optional] 

### Return type

[**AuditLogListDto**](AuditLogListDto.md)

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

