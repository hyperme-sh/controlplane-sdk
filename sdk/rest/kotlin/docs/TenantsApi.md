# TenantsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**activateTrialPlanApiV1TenantsTenantIdActivateTrialPlanPatch**](TenantsApi.md#activateTrialPlanApiV1TenantsTenantIdActivateTrialPlanPatch) | **PATCH** api/v1/tenants/{tenant_id}/activate_trial_plan | Activate Trial Plan |
| [**checkDnsStatusApiV1TenantsTenantIdCheckDnsGet**](TenantsApi.md#checkDnsStatusApiV1TenantsTenantIdCheckDnsGet) | **GET** api/v1/tenants/{tenant_id}/check_dns | Check Dns Status |
| [**checkSubdomainAvailabilityApiV1TenantsCheckSubdomainSubdomainGet**](TenantsApi.md#checkSubdomainAvailabilityApiV1TenantsCheckSubdomainSubdomainGet) | **GET** api/v1/tenants/check_subdomain/{subdomain} | Check Subdomain Availability |
| [**createTenantApiV1TenantsPost**](TenantsApi.md#createTenantApiV1TenantsPost) | **POST** api/v1/tenants/ | Create Tenant |
| [**deleteTenantApiV1TenantsIdDelete**](TenantsApi.md#deleteTenantApiV1TenantsIdDelete) | **DELETE** api/v1/tenants/{id} | Delete Tenant |
| [**getTenantFeaturesApiV1TenantsTenantIdFeaturesGet**](TenantsApi.md#getTenantFeaturesApiV1TenantsTenantIdFeaturesGet) | **GET** api/v1/tenants/{tenant_id}/features | Get Tenant Features |
| [**listTenantsApiV1TenantsGet**](TenantsApi.md#listTenantsApiV1TenantsGet) | **GET** api/v1/tenants/ | List Tenants |
| [**searchByNameApiV1TenantsSearchByNameNameGet**](TenantsApi.md#searchByNameApiV1TenantsSearchByNameNameGet) | **GET** api/v1/tenants/search_by_name/{name} | Search By Name |
| [**searchBySubdomainApiV1TenantsSearchBySubdomainSubdomainGet**](TenantsApi.md#searchBySubdomainApiV1TenantsSearchBySubdomainSubdomainGet) | **GET** api/v1/tenants/search_by_subdomain/{subdomain} | Search By Subdomain |
| [**updateTenantApiV1TenantsTenantIdPut**](TenantsApi.md#updateTenantApiV1TenantsTenantIdPut) | **PUT** api/v1/tenants/{tenant_id} | Update Tenant |
| [**updateTenantDnsRecordApiV1TenantsTenantIdUpdateDnsPost**](TenantsApi.md#updateTenantDnsRecordApiV1TenantsTenantIdUpdateDnsPost) | **POST** api/v1/tenants/{tenant_id}/update_dns | Update Tenant Dns Record |
| [**updateTenantFeatureApiV1TenantsTenantIdUpdateFeaturePatch**](TenantsApi.md#updateTenantFeatureApiV1TenantsTenantIdUpdateFeaturePatch) | **PATCH** api/v1/tenants/{tenant_id}/update_feature | Update Tenant Feature |



Activate Trial Plan

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(TenantsApi::class.java)
val tenantId : kotlin.String = tenantId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : UpdateTenantResponseDto = webService.activateTrialPlanApiV1TenantsTenantIdActivateTrialPlanPatch(tenantId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tenantId** | **kotlin.String**|  | |

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Check Dns Status

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(TenantsApi::class.java)
val tenantId : kotlin.String = tenantId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : UpdateTenantResponseDto = webService.checkDnsStatusApiV1TenantsTenantIdCheckDnsGet(tenantId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tenantId** | **kotlin.String**|  | |

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Check Subdomain Availability

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(TenantsApi::class.java)
val subdomain : kotlin.String = subdomain_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : SubdomainAvailabilityDto = webService.checkSubdomainAvailabilityApiV1TenantsCheckSubdomainSubdomainGet(subdomain)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **subdomain** | **kotlin.String**|  | |

### Return type

[**SubdomainAvailabilityDto**](SubdomainAvailabilityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Create Tenant

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(TenantsApi::class.java)
val createTenantDto : CreateTenantDto =  // CreateTenantDto | 

launch(Dispatchers.IO) {
    val result : CreateTenantResponseDto = webService.createTenantApiV1TenantsPost(createTenantDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createTenantDto** | [**CreateTenantDto**](CreateTenantDto.md)|  | |

### Return type

[**CreateTenantResponseDto**](CreateTenantResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Delete Tenant

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(TenantsApi::class.java)
val id : kotlin.String = id_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.deleteTenantApiV1TenantsIdDelete(id)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **kotlin.String**|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Tenant Features

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(TenantsApi::class.java)
val tenantId : kotlin.String = tenantId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<FeatureDto> = webService.getTenantFeaturesApiV1TenantsTenantIdFeaturesGet(tenantId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tenantId** | **kotlin.String**|  | |

### Return type

[**kotlin.collections.List&lt;FeatureDto&gt;**](FeatureDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List Tenants

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(TenantsApi::class.java)
val skip : kotlin.Int = 56 // kotlin.Int | 
val limit : kotlin.Int = 56 // kotlin.Int | 

launch(Dispatchers.IO) {
    val result : TenantListDto = webService.listTenantsApiV1TenantsGet(skip, limit)
}
```

### Parameters
| **skip** | **kotlin.Int**|  | [optional] [default to 0] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **kotlin.Int**|  | [optional] [default to 10] |

### Return type

[**TenantListDto**](TenantListDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Search By Name

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(TenantsApi::class.java)
val name : kotlin.String = name_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : TenantDto = webService.searchByNameApiV1TenantsSearchByNameNameGet(name)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **kotlin.String**|  | |

### Return type

[**TenantDto**](TenantDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Search By Subdomain

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(TenantsApi::class.java)
val subdomain : kotlin.String = subdomain_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : TenantDto = webService.searchBySubdomainApiV1TenantsSearchBySubdomainSubdomainGet(subdomain)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **subdomain** | **kotlin.String**|  | |

### Return type

[**TenantDto**](TenantDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Update Tenant

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(TenantsApi::class.java)
val tenantId : kotlin.String = tenantId_example // kotlin.String | 
val updateTenantDto : UpdateTenantDto =  // UpdateTenantDto | 

launch(Dispatchers.IO) {
    webService.updateTenantApiV1TenantsTenantIdPut(tenantId, updateTenantDto)
}
```

### Parameters
| **tenantId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **updateTenantDto** | [**UpdateTenantDto**](UpdateTenantDto.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Update Tenant Dns Record

When bringing your own domain you must map the DNS records for your custom domain to point to our main domain.                 You can do this by adding a CNAME record in your domain&#39;s DNS settings.                 Here is an example of how to set it up:                 Type: CNAME                 Name: app                 Value: fsrapp.com

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(TenantsApi::class.java)
val tenantId : kotlin.String = tenantId_example // kotlin.String | 
val updateTenantDto : UpdateTenantDto =  // UpdateTenantDto | 

launch(Dispatchers.IO) {
    val result : UpdateTenantResponseDto = webService.updateTenantDnsRecordApiV1TenantsTenantIdUpdateDnsPost(tenantId, updateTenantDto)
}
```

### Parameters
| **tenantId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **updateTenantDto** | [**UpdateTenantDto**](UpdateTenantDto.md)|  | |

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Update Tenant Feature

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(TenantsApi::class.java)
val tenantId : kotlin.String = tenantId_example // kotlin.String | 
val featureDto : FeatureDto =  // FeatureDto | 

launch(Dispatchers.IO) {
    val result : UpdateTenantResponseDto = webService.updateTenantFeatureApiV1TenantsTenantIdUpdateFeaturePatch(tenantId, featureDto)
}
```

### Parameters
| **tenantId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **featureDto** | [**FeatureDto**](FeatureDto.md)|  | |

### Return type

[**UpdateTenantResponseDto**](UpdateTenantResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

