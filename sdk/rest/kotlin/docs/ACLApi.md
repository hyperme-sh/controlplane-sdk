# ACLApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createPolicyApiV1AclPoliciesPost**](ACLApi.md#createPolicyApiV1AclPoliciesPost) | **POST** api/v1/acl/policies | Create Policy |
| [**enforceCheckApiV1AclEnforcePost**](ACLApi.md#enforceCheckApiV1AclEnforcePost) | **POST** api/v1/acl/enforce | Enforce Check |
| [**listPoliciesApiV1AclPoliciesGet**](ACLApi.md#listPoliciesApiV1AclPoliciesGet) | **GET** api/v1/acl/policies | List Policies |
| [**protectedPingApiV1AclProtectedPingGet**](ACLApi.md#protectedPingApiV1AclProtectedPingGet) | **GET** api/v1/acl/protected-ping | Protected Ping |
| [**removePolicyApiV1AclPoliciesDelete**](ACLApi.md#removePolicyApiV1AclPoliciesDelete) | **DELETE** api/v1/acl/policies | Remove Policy |



Create Policy

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(ACLApi::class.java)
val policyRuleCreate : PolicyRuleCreate =  // PolicyRuleCreate | 

launch(Dispatchers.IO) {
    val result : PolicyRowResponse = webService.createPolicyApiV1AclPoliciesPost(policyRuleCreate)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **policyRuleCreate** | [**PolicyRuleCreate**](PolicyRuleCreate.md)|  | |

### Return type

[**PolicyRowResponse**](PolicyRowResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Enforce Check

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(ACLApi::class.java)
val enforceRequest : EnforceRequest =  // EnforceRequest | 

launch(Dispatchers.IO) {
    val result : EnforceResponse = webService.enforceCheckApiV1AclEnforcePost(enforceRequest)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **enforceRequest** | [**EnforceRequest**](EnforceRequest.md)|  | |

### Return type

[**EnforceResponse**](EnforceResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


List Policies

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(ACLApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<PolicyRowResponse> = webService.listPoliciesApiV1AclPoliciesGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;PolicyRowResponse&gt;**](PolicyRowResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Protected Ping

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(ACLApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.protectedPingApiV1AclProtectedPingGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Remove Policy

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(ACLApi::class.java)
val policyRuleDelete : PolicyRuleDelete =  // PolicyRuleDelete | 

launch(Dispatchers.IO) {
    webService.removePolicyApiV1AclPoliciesDelete(policyRuleDelete)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **policyRuleDelete** | [**PolicyRuleDelete**](PolicyRuleDelete.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

