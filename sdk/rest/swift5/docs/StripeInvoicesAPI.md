# StripeInvoicesAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listInvoicesApiV1InvoicesGet**](StripeInvoicesAPI.md#listinvoicesapiv1invoicesget) | **GET** /api/v1/invoices/ | List invoices


# **listInvoicesApiV1InvoicesGet**
```swift
    open class func listInvoicesApiV1InvoicesGet(completion: @escaping (_ data: InvoiceListDto?, _ error: Error?) -> Void)
```

List invoices

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// List invoices
StripeInvoicesAPI.listInvoicesApiV1InvoicesGet() { (response, error) in
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

[**InvoiceListDto**](InvoiceListDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

