# StripeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**configureStripeSettingApiV1ConfigurationsStripePost**](StripeApi.md#configureStripeSettingApiV1ConfigurationsStripePost) | **POST** api/v1/configurations/stripe | Configure Stripe Setting |
| [**getStripeSettingsApiV1ConfigurationsStripeGet**](StripeApi.md#getStripeSettingsApiV1ConfigurationsStripeGet) | **GET** api/v1/configurations/stripe | Get Stripe Settings |
| [**stripeWebhookApiV1ConfigurationsStripeWebhooksPost**](StripeApi.md#stripeWebhookApiV1ConfigurationsStripeWebhooksPost) | **POST** api/v1/configurations/stripe/webhooks | Stripe Webhook |



Configure Stripe Setting

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeApi::class.java)
val createStripeSettingDto : CreateStripeSettingDto =  // CreateStripeSettingDto | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.configureStripeSettingApiV1ConfigurationsStripePost(createStripeSettingDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createStripeSettingDto** | [**CreateStripeSettingDto**](CreateStripeSettingDto.md)|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Get Stripe Settings

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeApi::class.java)

launch(Dispatchers.IO) {
    val result : StripeSettingDto = webService.getStripeSettingsApiV1ConfigurationsStripeGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StripeSettingDto**](StripeSettingDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Stripe Webhook

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.stripeWebhookApiV1ConfigurationsStripeWebhooksPost()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

