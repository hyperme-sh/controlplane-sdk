# StripeAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureStripeSettingApiV1ConfigurationsStripePost**](StripeAPI.md#configurestripesettingapiv1configurationsstripepost) | **POST** /api/v1/configurations/stripe | Configure Stripe Setting
[**getStripeSettingsApiV1ConfigurationsStripeGet**](StripeAPI.md#getstripesettingsapiv1configurationsstripeget) | **GET** /api/v1/configurations/stripe | Get Stripe Settings
[**stripeWebhookApiV1ConfigurationsStripeWebhooksPost**](StripeAPI.md#stripewebhookapiv1configurationsstripewebhookspost) | **POST** /api/v1/configurations/stripe/webhooks | Stripe Webhook


# **configureStripeSettingApiV1ConfigurationsStripePost**
```swift
    open class func configureStripeSettingApiV1ConfigurationsStripePost(createStripeSettingDto: CreateStripeSettingDto, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Configure Stripe Setting

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let createStripeSettingDto = CreateStripeSettingDto(defaultCurrency: "defaultCurrency_example", stripeWebhookSecret: "stripeWebhookSecret_example", mode: "mode_example", trialPeriodDays: 123, stripeSecretKey: "stripeSecretKey_example", tenantId: "tenantId_example") // CreateStripeSettingDto | 

// Configure Stripe Setting
StripeAPI.configureStripeSettingApiV1ConfigurationsStripePost(createStripeSettingDto: createStripeSettingDto) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createStripeSettingDto** | [**CreateStripeSettingDto**](CreateStripeSettingDto.md) |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getStripeSettingsApiV1ConfigurationsStripeGet**
```swift
    open class func getStripeSettingsApiV1ConfigurationsStripeGet(completion: @escaping (_ data: StripeSettingDto?, _ error: Error?) -> Void)
```

Get Stripe Settings

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get Stripe Settings
StripeAPI.getStripeSettingsApiV1ConfigurationsStripeGet() { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stripeWebhookApiV1ConfigurationsStripeWebhooksPost**
```swift
    open class func stripeWebhookApiV1ConfigurationsStripeWebhooksPost(completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Stripe Webhook

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Stripe Webhook
StripeAPI.stripeWebhookApiV1ConfigurationsStripeWebhooksPost() { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

