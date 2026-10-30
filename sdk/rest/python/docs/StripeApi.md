# openapi_client.StripeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_stripe_setting_api_v1_configurations_stripe_post**](StripeApi.md#configure_stripe_setting_api_v1_configurations_stripe_post) | **POST** /api/v1/configurations/stripe | Configure Stripe Setting
[**get_stripe_settings_api_v1_configurations_stripe_get**](StripeApi.md#get_stripe_settings_api_v1_configurations_stripe_get) | **GET** /api/v1/configurations/stripe | Get Stripe Settings
[**stripe_webhook_api_v1_configurations_stripe_webhooks_post**](StripeApi.md#stripe_webhook_api_v1_configurations_stripe_webhooks_post) | **POST** /api/v1/configurations/stripe/webhooks | Stripe Webhook


# **configure_stripe_setting_api_v1_configurations_stripe_post**
> object configure_stripe_setting_api_v1_configurations_stripe_post(create_stripe_setting_dto)

Configure Stripe Setting

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.create_stripe_setting_dto import CreateStripeSettingDto
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
    api_instance = openapi_client.StripeApi(api_client)
    create_stripe_setting_dto = openapi_client.CreateStripeSettingDto() # CreateStripeSettingDto | 

    try:
        # Configure Stripe Setting
        api_response = api_instance.configure_stripe_setting_api_v1_configurations_stripe_post(create_stripe_setting_dto)
        print("The response of StripeApi->configure_stripe_setting_api_v1_configurations_stripe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->configure_stripe_setting_api_v1_configurations_stripe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stripe_setting_dto** | [**CreateStripeSettingDto**](CreateStripeSettingDto.md)|  | 

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

# **get_stripe_settings_api_v1_configurations_stripe_get**
> StripeSettingDto get_stripe_settings_api_v1_configurations_stripe_get()

Get Stripe Settings

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.stripe_setting_dto import StripeSettingDto
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
    api_instance = openapi_client.StripeApi(api_client)

    try:
        # Get Stripe Settings
        api_response = api_instance.get_stripe_settings_api_v1_configurations_stripe_get()
        print("The response of StripeApi->get_stripe_settings_api_v1_configurations_stripe_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->get_stripe_settings_api_v1_configurations_stripe_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StripeSettingDto**](StripeSettingDto.md)

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

# **stripe_webhook_api_v1_configurations_stripe_webhooks_post**
> object stripe_webhook_api_v1_configurations_stripe_webhooks_post()

Stripe Webhook

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
    api_instance = openapi_client.StripeApi(api_client)

    try:
        # Stripe Webhook
        api_response = api_instance.stripe_webhook_api_v1_configurations_stripe_webhooks_post()
        print("The response of StripeApi->stripe_webhook_api_v1_configurations_stripe_webhooks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->stripe_webhook_api_v1_configurations_stripe_webhooks_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

