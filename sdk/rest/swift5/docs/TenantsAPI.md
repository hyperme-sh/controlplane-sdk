# TenantsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateTrialPlanApiV1TenantsTenantIdActivateTrialPlanPatch**](TenantsAPI.md#activatetrialplanapiv1tenantstenantidactivatetrialplanpatch) | **PATCH** /api/v1/tenants/{tenant_id}/activate_trial_plan | Activate Trial Plan
[**checkDnsStatusApiV1TenantsTenantIdCheckDnsGet**](TenantsAPI.md#checkdnsstatusapiv1tenantstenantidcheckdnsget) | **GET** /api/v1/tenants/{tenant_id}/check_dns | Check Dns Status
[**checkSubdomainAvailabilityApiV1TenantsCheckSubdomainSubdomainGet**](TenantsAPI.md#checksubdomainavailabilityapiv1tenantschecksubdomainsubdomainget) | **GET** /api/v1/tenants/check_subdomain/{subdomain} | Check Subdomain Availability
[**createTenantApiV1TenantsPost**](TenantsAPI.md#createtenantapiv1tenantspost) | **POST** /api/v1/tenants/ | Create Tenant
[**deleteTenantApiV1TenantsIdDelete**](TenantsAPI.md#deletetenantapiv1tenantsiddelete) | **DELETE** /api/v1/tenants/{id} | Delete Tenant
[**getTenantFeaturesApiV1TenantsTenantIdFeaturesGet**](TenantsAPI.md#gettenantfeaturesapiv1tenantstenantidfeaturesget) | **GET** /api/v1/tenants/{tenant_id}/features | Get Tenant Features
[**listTenantsApiV1TenantsGet**](TenantsAPI.md#listtenantsapiv1tenantsget) | **GET** /api/v1/tenants/ | List Tenants
[**searchByNameApiV1TenantsSearchByNameNameGet**](TenantsAPI.md#searchbynameapiv1tenantssearchbynamenameget) | **GET** /api/v1/tenants/search_by_name/{name} | Search By Name
[**searchBySubdomainApiV1TenantsSearchBySubdomainSubdomainGet**](TenantsAPI.md#searchbysubdomainapiv1tenantssearchbysubdomainsubdomainget) | **GET** /api/v1/tenants/search_by_subdomain/{subdomain} | Search By Subdomain
[**updateTenantApiV1TenantsTenantIdPut**](TenantsAPI.md#updatetenantapiv1tenantstenantidput) | **PUT** /api/v1/tenants/{tenant_id} | Update Tenant
[**updateTenantDnsRecordApiV1TenantsTenantIdUpdateDnsPost**](TenantsAPI.md#updatetenantdnsrecordapiv1tenantstenantidupdatednspost) | **POST** /api/v1/tenants/{tenant_id}/update_dns | Update Tenant Dns Record
[**updateTenantFeatureApiV1TenantsTenantIdUpdateFeaturePatch**](TenantsAPI.md#updatetenantfeatureapiv1tenantstenantidupdatefeaturepatch) | **PATCH** /api/v1/tenants/{tenant_id}/update_feature | Update Tenant Feature


# **activateTrialPlanApiV1TenantsTenantIdActivateTrialPlanPatch**
```swift
    open class func activateTrialPlanApiV1TenantsTenantIdActivateTrialPlanPatch(tenantId: String, completion: @escaping (_ data: UpdateTenantResponseDto?, _ error: Error?) -> Void)
```

Activate Trial Plan

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let tenantId = "tenantId_example" // String | 

// Activate Trial Plan
TenantsAPI.activateTrialPlanApiV1TenantsTenantIdActivateTrialPlanPatch(tenantId: tenantId) { (response, error) in
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
 **tenantId** | **String** |  | 

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkDnsStatusApiV1TenantsTenantIdCheckDnsGet**
```swift
    open class func checkDnsStatusApiV1TenantsTenantIdCheckDnsGet(tenantId: String, completion: @escaping (_ data: UpdateTenantResponseDto?, _ error: Error?) -> Void)
```

Check Dns Status

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let tenantId = "tenantId_example" // String | 

// Check Dns Status
TenantsAPI.checkDnsStatusApiV1TenantsTenantIdCheckDnsGet(tenantId: tenantId) { (response, error) in
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
 **tenantId** | **String** |  | 

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkSubdomainAvailabilityApiV1TenantsCheckSubdomainSubdomainGet**
```swift
    open class func checkSubdomainAvailabilityApiV1TenantsCheckSubdomainSubdomainGet(subdomain: String, completion: @escaping (_ data: SubdomainAvailabilityDto?, _ error: Error?) -> Void)
```

Check Subdomain Availability

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let subdomain = "subdomain_example" // String | 

// Check Subdomain Availability
TenantsAPI.checkSubdomainAvailabilityApiV1TenantsCheckSubdomainSubdomainGet(subdomain: subdomain) { (response, error) in
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
 **subdomain** | **String** |  | 

### Return type

[**SubdomainAvailabilityDto**](SubdomainAvailabilityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createTenantApiV1TenantsPost**
```swift
    open class func createTenantApiV1TenantsPost(createTenantDto: CreateTenantDto, completion: @escaping (_ data: CreateTenantResponseDto?, _ error: Error?) -> Void)
```

Create Tenant

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let createTenantDto = CreateTenantDto(name: "name_example", subdomain: "subdomain_example", adminEmail: "adminEmail_example", adminPassword: "adminPassword_example", firstName: "firstName_example", lastName: "lastName_example", gender: Gender()) // CreateTenantDto | 

// Create Tenant
TenantsAPI.createTenantApiV1TenantsPost(createTenantDto: createTenantDto) { (response, error) in
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
 **createTenantDto** | [**CreateTenantDto**](CreateTenantDto.md) |  | 

### Return type

[**CreateTenantResponseDto**](CreateTenantResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteTenantApiV1TenantsIdDelete**
```swift
    open class func deleteTenantApiV1TenantsIdDelete(id: String, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Delete Tenant

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let id = "id_example" // String | 

// Delete Tenant
TenantsAPI.deleteTenantApiV1TenantsIdDelete(id: id) { (response, error) in
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
 **id** | **String** |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getTenantFeaturesApiV1TenantsTenantIdFeaturesGet**
```swift
    open class func getTenantFeaturesApiV1TenantsTenantIdFeaturesGet(tenantId: String, completion: @escaping (_ data: [FeatureDto]?, _ error: Error?) -> Void)
```

Get Tenant Features

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let tenantId = "tenantId_example" // String | 

// Get Tenant Features
TenantsAPI.getTenantFeaturesApiV1TenantsTenantIdFeaturesGet(tenantId: tenantId) { (response, error) in
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
 **tenantId** | **String** |  | 

### Return type

[**[FeatureDto]**](FeatureDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listTenantsApiV1TenantsGet**
```swift
    open class func listTenantsApiV1TenantsGet(skip: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: TenantListDto?, _ error: Error?) -> Void)
```

List Tenants

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let skip = 987 // Int |  (optional) (default to 0)
let limit = 987 // Int |  (optional) (default to 10)

// List Tenants
TenantsAPI.listTenantsApiV1TenantsGet(skip: skip, limit: limit) { (response, error) in
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
 **skip** | **Int** |  | [optional] [default to 0]
 **limit** | **Int** |  | [optional] [default to 10]

### Return type

[**TenantListDto**](TenantListDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchByNameApiV1TenantsSearchByNameNameGet**
```swift
    open class func searchByNameApiV1TenantsSearchByNameNameGet(name: String, completion: @escaping (_ data: TenantDto?, _ error: Error?) -> Void)
```

Search By Name

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let name = "name_example" // String | 

// Search By Name
TenantsAPI.searchByNameApiV1TenantsSearchByNameNameGet(name: name) { (response, error) in
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
 **name** | **String** |  | 

### Return type

[**TenantDto**](TenantDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchBySubdomainApiV1TenantsSearchBySubdomainSubdomainGet**
```swift
    open class func searchBySubdomainApiV1TenantsSearchBySubdomainSubdomainGet(subdomain: String, completion: @escaping (_ data: TenantDto?, _ error: Error?) -> Void)
```

Search By Subdomain

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let subdomain = "subdomain_example" // String | 

// Search By Subdomain
TenantsAPI.searchBySubdomainApiV1TenantsSearchBySubdomainSubdomainGet(subdomain: subdomain) { (response, error) in
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
 **subdomain** | **String** |  | 

### Return type

[**TenantDto**](TenantDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateTenantApiV1TenantsTenantIdPut**
```swift
    open class func updateTenantApiV1TenantsTenantIdPut(tenantId: String, updateTenantDto: UpdateTenantDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Update Tenant

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let tenantId = "tenantId_example" // String | 
let updateTenantDto = UpdateTenantDto(isActive: false, customDomain: "customDomain_example", subscriptionId: "subscriptionId_example", customDomainStatus: "customDomainStatus_example") // UpdateTenantDto | 

// Update Tenant
TenantsAPI.updateTenantApiV1TenantsTenantIdPut(tenantId: tenantId, updateTenantDto: updateTenantDto) { (response, error) in
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
 **tenantId** | **String** |  | 
 **updateTenantDto** | [**UpdateTenantDto**](UpdateTenantDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateTenantDnsRecordApiV1TenantsTenantIdUpdateDnsPost**
```swift
    open class func updateTenantDnsRecordApiV1TenantsTenantIdUpdateDnsPost(tenantId: String, updateTenantDto: UpdateTenantDto, completion: @escaping (_ data: UpdateTenantResponseDto?, _ error: Error?) -> Void)
```

Update Tenant Dns Record

When bringing your own domain you must map the DNS records for your custom domain to point to our main domain.                 You can do this by adding a CNAME record in your domain's DNS settings.                 Here is an example of how to set it up:                 Type: CNAME                 Name: app                 Value: fsrapp.com

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let tenantId = "tenantId_example" // String | 
let updateTenantDto = UpdateTenantDto(isActive: false, customDomain: "customDomain_example", subscriptionId: "subscriptionId_example", customDomainStatus: "customDomainStatus_example") // UpdateTenantDto | 

// Update Tenant Dns Record
TenantsAPI.updateTenantDnsRecordApiV1TenantsTenantIdUpdateDnsPost(tenantId: tenantId, updateTenantDto: updateTenantDto) { (response, error) in
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
 **tenantId** | **String** |  | 
 **updateTenantDto** | [**UpdateTenantDto**](UpdateTenantDto.md) |  | 

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateTenantFeatureApiV1TenantsTenantIdUpdateFeaturePatch**
```swift
    open class func updateTenantFeatureApiV1TenantsTenantIdUpdateFeaturePatch(tenantId: String, featureDto: FeatureDto, completion: @escaping (_ data: UpdateTenantResponseDto?, _ error: Error?) -> Void)
```

Update Tenant Feature

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let tenantId = "tenantId_example" // String | 
let featureDto = FeatureDto(name: Feature(), enabled: false) // FeatureDto | 

// Update Tenant Feature
TenantsAPI.updateTenantFeatureApiV1TenantsTenantIdUpdateFeaturePatch(tenantId: tenantId, featureDto: featureDto) { (response, error) in
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
 **tenantId** | **String** |  | 
 **featureDto** | [**FeatureDto**](FeatureDto.md) |  | 

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

