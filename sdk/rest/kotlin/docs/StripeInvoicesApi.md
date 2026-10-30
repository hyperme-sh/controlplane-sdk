# StripeInvoicesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listInvoicesApiV1InvoicesGet**](StripeInvoicesApi.md#listInvoicesApiV1InvoicesGet) | **GET** api/v1/invoices/ | List invoices |



List invoices

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeInvoicesApi::class.java)

launch(Dispatchers.IO) {
    val result : InvoiceListDto = webService.listInvoicesApiV1InvoicesGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InvoiceListDto**](InvoiceListDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

