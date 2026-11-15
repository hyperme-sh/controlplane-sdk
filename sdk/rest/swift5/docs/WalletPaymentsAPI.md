# WalletPaymentsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**challengeApiV1PaymentsHostPayoutAddressChallengePost**](WalletPaymentsAPI.md#challengeapiv1paymentshostpayoutaddresschallengepost) | **POST** /api/v1/payments/host-payout-address/challenge | Challenge
[**createWalletCheckout**](WalletPaymentsAPI.md#createwalletcheckout) | **POST** /api/v1/payments/wallet/lease-payments/{billing_record_id}/checkout | Open Stablecoin Checkout
[**createWalletDeposit**](WalletPaymentsAPI.md#createwalletdeposit) | **POST** /api/v1/payments/wallet/lease-payments/{billing_record_id}/deposit | Create Deposit
[**createWalletLeasePayment**](WalletPaymentsAPI.md#createwalletleasepayment) | **POST** /api/v1/payments/wallet/lease-payments | Create Usdc Lease Payment Route
[**getWalletDeposit**](WalletPaymentsAPI.md#getwalletdeposit) | **GET** /api/v1/payments/wallet/lease-payments/{billing_record_id}/deposit | Deposit Status
[**getWalletPaymentCapabilities**](WalletPaymentsAPI.md#getwalletpaymentcapabilities) | **GET** /api/v1/payments/wallet/capabilities | Wallet Capabilities
[**submitApiV1PaymentsHostPayoutAddressPost**](WalletPaymentsAPI.md#submitapiv1paymentshostpayoutaddresspost) | **POST** /api/v1/payments/host-payout-address | Submit


# **challengeApiV1PaymentsHostPayoutAddressChallengePost**
```swift
    open class func challengeApiV1PaymentsHostPayoutAddressChallengePost(xTenantID: UUID, walletPaymentChallengeRequest: WalletPaymentChallengeRequest, completion: @escaping (_ data: WalletPaymentPayoutChallenge?, _ error: Error?) -> Void)
```

Challenge

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let xTenantID = 987 // UUID | Must match the browser tenant session
let walletPaymentChallengeRequest = WalletPaymentChallengeRequest(address: "address_example", chainId: 123) // WalletPaymentChallengeRequest | 

// Challenge
WalletPaymentsAPI.challengeApiV1PaymentsHostPayoutAddressChallengePost(xTenantID: xTenantID, walletPaymentChallengeRequest: walletPaymentChallengeRequest) { (response, error) in
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
 **xTenantID** | **UUID** | Must match the browser tenant session | 
 **walletPaymentChallengeRequest** | [**WalletPaymentChallengeRequest**](WalletPaymentChallengeRequest.md) |  | 

### Return type

[**WalletPaymentPayoutChallenge**](WalletPaymentPayoutChallenge.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createWalletCheckout**
```swift
    open class func createWalletCheckout(billingRecordId: UUID, xTenantID: UUID, completion: @escaping (_ data: WalletPaymentWalletCheckoutResponse?, _ error: Error?) -> Void)
```

Open Stablecoin Checkout

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let billingRecordId = 987 // UUID | 
let xTenantID = 987 // UUID | 

// Open Stablecoin Checkout
WalletPaymentsAPI.createWalletCheckout(billingRecordId: billingRecordId, xTenantID: xTenantID) { (response, error) in
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
 **billingRecordId** | **UUID** |  | 
 **xTenantID** | **UUID** |  | 

### Return type

[**WalletPaymentWalletCheckoutResponse**](WalletPaymentWalletCheckoutResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createWalletDeposit**
```swift
    open class func createWalletDeposit(billingRecordId: UUID, xTenantID: UUID, completion: @escaping (_ data: WalletPaymentWalletDepositStatus?, _ error: Error?) -> Void)
```

Create Deposit

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let billingRecordId = 987 // UUID | 
let xTenantID = 987 // UUID | 

// Create Deposit
WalletPaymentsAPI.createWalletDeposit(billingRecordId: billingRecordId, xTenantID: xTenantID) { (response, error) in
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
 **billingRecordId** | **UUID** |  | 
 **xTenantID** | **UUID** |  | 

### Return type

[**WalletPaymentWalletDepositStatus**](WalletPaymentWalletDepositStatus.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createWalletLeasePayment**
```swift
    open class func createWalletLeasePayment(xTenantID: UUID, walletPaymentUsdcLeasePaymentCreate: WalletPaymentUsdcLeasePaymentCreate, idempotencyKey: UUID? = nil, completion: @escaping (_ data: WalletPaymentWalletLeasePaymentResponse?, _ error: Error?) -> Void)
```

Create Usdc Lease Payment Route

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let xTenantID = 987 // UUID | 
let walletPaymentUsdcLeasePaymentCreate = WalletPaymentUsdcLeasePaymentCreate(amountCents: 123, listingId: 123, metadata: "TODO") // WalletPaymentUsdcLeasePaymentCreate | 
let idempotencyKey = 987 // UUID | Reuse the same UUID when retrying the same payment request. (optional)

// Create Usdc Lease Payment Route
WalletPaymentsAPI.createWalletLeasePayment(xTenantID: xTenantID, walletPaymentUsdcLeasePaymentCreate: walletPaymentUsdcLeasePaymentCreate, idempotencyKey: idempotencyKey) { (response, error) in
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
 **xTenantID** | **UUID** |  | 
 **walletPaymentUsdcLeasePaymentCreate** | [**WalletPaymentUsdcLeasePaymentCreate**](WalletPaymentUsdcLeasePaymentCreate.md) |  | 
 **idempotencyKey** | **UUID** | Reuse the same UUID when retrying the same payment request. | [optional] 

### Return type

[**WalletPaymentWalletLeasePaymentResponse**](WalletPaymentWalletLeasePaymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getWalletDeposit**
```swift
    open class func getWalletDeposit(billingRecordId: UUID, xTenantID: UUID, completion: @escaping (_ data: WalletPaymentWalletDepositStatus?, _ error: Error?) -> Void)
```

Deposit Status

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let billingRecordId = 987 // UUID | 
let xTenantID = 987 // UUID | 

// Deposit Status
WalletPaymentsAPI.getWalletDeposit(billingRecordId: billingRecordId, xTenantID: xTenantID) { (response, error) in
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
 **billingRecordId** | **UUID** |  | 
 **xTenantID** | **UUID** |  | 

### Return type

[**WalletPaymentWalletDepositStatus**](WalletPaymentWalletDepositStatus.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getWalletPaymentCapabilities**
```swift
    open class func getWalletPaymentCapabilities(xTenantID: UUID, completion: @escaping (_ data: WalletPaymentWalletCapabilities?, _ error: Error?) -> Void)
```

Wallet Capabilities

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let xTenantID = 987 // UUID | 

// Wallet Capabilities
WalletPaymentsAPI.getWalletPaymentCapabilities(xTenantID: xTenantID) { (response, error) in
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
 **xTenantID** | **UUID** |  | 

### Return type

[**WalletPaymentWalletCapabilities**](WalletPaymentWalletCapabilities.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submitApiV1PaymentsHostPayoutAddressPost**
```swift
    open class func submitApiV1PaymentsHostPayoutAddressPost(xTenantID: UUID, walletPaymentSubmitRequest: WalletPaymentSubmitRequest, completion: @escaping (_ data: WalletPaymentRegisteredDestination?, _ error: Error?) -> Void)
```

Submit

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let xTenantID = 987 // UUID | Must match the browser tenant session
let walletPaymentSubmitRequest = WalletPaymentSubmitRequest(message: "message_example", nonce: "nonce_example", signature: "signature_example") // WalletPaymentSubmitRequest | 

// Submit
WalletPaymentsAPI.submitApiV1PaymentsHostPayoutAddressPost(xTenantID: xTenantID, walletPaymentSubmitRequest: walletPaymentSubmitRequest) { (response, error) in
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
 **xTenantID** | **UUID** | Must match the browser tenant session | 
 **walletPaymentSubmitRequest** | [**WalletPaymentSubmitRequest**](WalletPaymentSubmitRequest.md) |  | 

### Return type

[**WalletPaymentRegisteredDestination**](WalletPaymentRegisteredDestination.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

