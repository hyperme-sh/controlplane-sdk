# StripeBillingApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createPlanApiV1BillingPlansPost**](StripeBillingApi.md#createPlanApiV1BillingPlansPost) | **POST** api/v1/billing/plans | Create a new plan |
| [**deletePlanApiV1BillingPlansPlanIdDelete**](StripeBillingApi.md#deletePlanApiV1BillingPlansPlanIdDelete) | **DELETE** api/v1/billing/plans/{plan_id} | Delete existing plan |
| [**getPlanApiV1BillingPlansPlanIdGet**](StripeBillingApi.md#getPlanApiV1BillingPlansPlanIdGet) | **GET** api/v1/billing/plans/{plan_id} | Retrieve a plan details |
| [**listPlansApiV1BillingPlansGet**](StripeBillingApi.md#listPlansApiV1BillingPlansGet) | **GET** api/v1/billing/plans | List available plans |
| [**updatePlanApiV1BillingPlansPlanIdPatch**](StripeBillingApi.md#updatePlanApiV1BillingPlansPlanIdPatch) | **PATCH** api/v1/billing/plans/{plan_id} | Update a existing plan |



Create a new plan

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeBillingApi::class.java)
val createPlanDto : CreatePlanDto =  // CreatePlanDto | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.createPlanApiV1BillingPlansPost(createPlanDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createPlanDto** | [**CreatePlanDto**](CreatePlanDto.md)|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Delete existing plan

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeBillingApi::class.java)
val planId : kotlin.String = planId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.deletePlanApiV1BillingPlansPlanIdDelete(planId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **planId** | **kotlin.String**|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Retrieve a plan details

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeBillingApi::class.java)
val planId : kotlin.String = planId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : PlanDto = webService.getPlanApiV1BillingPlansPlanIdGet(planId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **planId** | **kotlin.String**|  | |

### Return type

[**PlanDto**](PlanDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List available plans

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeBillingApi::class.java)

launch(Dispatchers.IO) {
    val result : PlanListDto = webService.listPlansApiV1BillingPlansGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PlanListDto**](PlanListDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Update a existing plan

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(StripeBillingApi::class.java)
val planId : kotlin.String = planId_example // kotlin.String | 
val updatePlanDto : UpdatePlanDto =  // UpdatePlanDto | 

launch(Dispatchers.IO) {
    webService.updatePlanApiV1BillingPlansPlanIdPatch(planId, updatePlanDto)
}
```

### Parameters
| **planId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **updatePlanDto** | [**UpdatePlanDto**](UpdatePlanDto.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

