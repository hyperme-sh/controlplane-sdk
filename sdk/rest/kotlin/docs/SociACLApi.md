# SociACLApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**sociaclCreateShareApiV1AclSociaclSharesPost**](SociACLApi.md#sociaclCreateShareApiV1AclSociaclSharesPost) | **POST** api/v1/acl/sociacl/shares | Sociacl Create Share |
| [**sociaclEvaluateApiV1AclSociaclEvaluatePost**](SociACLApi.md#sociaclEvaluateApiV1AclSociaclEvaluatePost) | **POST** api/v1/acl/sociacl/evaluate | Sociacl Evaluate |
| [**sociaclRecoveryCreateApiV1AclSociaclRecoverySessionsPost**](SociACLApi.md#sociaclRecoveryCreateApiV1AclSociaclRecoverySessionsPost) | **POST** api/v1/acl/sociacl/recovery/sessions | Sociacl Recovery Create |
| [**sociaclRecoveryProofApiV1AclSociaclRecoverySessionsSessionIdProofPost**](SociACLApi.md#sociaclRecoveryProofApiV1AclSociaclRecoverySessionsSessionIdProofPost) | **POST** api/v1/acl/sociacl/recovery/sessions/{session_id}/proof | Sociacl Recovery Proof |
| [**sociaclResolveShareApiV1AclSociaclSharesByTokenTokenGet**](SociACLApi.md#sociaclResolveShareApiV1AclSociaclSharesByTokenTokenGet) | **GET** api/v1/acl/sociacl/shares/by-token/{token} | Sociacl Resolve Share |



Sociacl Create Share

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(SociACLApi::class.java)
val sociACLShareLinkCreate : SociACLShareLinkCreate =  // SociACLShareLinkCreate | 

launch(Dispatchers.IO) {
    val result : SociaclShareCreatedResponse = webService.sociaclCreateShareApiV1AclSociaclSharesPost(sociACLShareLinkCreate)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sociACLShareLinkCreate** | [**SociACLShareLinkCreate**](SociACLShareLinkCreate.md)|  | |

### Return type

[**SociaclShareCreatedResponse**](SociaclShareCreatedResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Sociacl Evaluate

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(SociACLApi::class.java)
val sociACLEvaluateRequest : SociACLEvaluateRequest =  // SociACLEvaluateRequest | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.sociaclEvaluateApiV1AclSociaclEvaluatePost(sociACLEvaluateRequest)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sociACLEvaluateRequest** | [**SociACLEvaluateRequest**](SociACLEvaluateRequest.md)|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Sociacl Recovery Create

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(SociACLApi::class.java)
val recoverySessionCreate : RecoverySessionCreate =  // RecoverySessionCreate | 

launch(Dispatchers.IO) {
    val result : RecoverySessionResponse = webService.sociaclRecoveryCreateApiV1AclSociaclRecoverySessionsPost(recoverySessionCreate)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **recoverySessionCreate** | [**RecoverySessionCreate**](RecoverySessionCreate.md)|  | |

### Return type

[**RecoverySessionResponse**](RecoverySessionResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Sociacl Recovery Proof

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(SociACLApi::class.java)
val sessionId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val recoveryProofRequest : RecoveryProofRequest =  // RecoveryProofRequest | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.sociaclRecoveryProofApiV1AclSociaclRecoverySessionsSessionIdProofPost(sessionId, recoveryProofRequest)
}
```

### Parameters
| **sessionId** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **recoveryProofRequest** | [**RecoveryProofRequest**](RecoveryProofRequest.md)|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Sociacl Resolve Share

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
val webService = apiClient.createWebservice(SociACLApi::class.java)
val token : kotlin.String = token_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : SociACLShareLinkPublic = webService.sociaclResolveShareApiV1AclSociaclSharesByTokenTokenGet(token)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **token** | **kotlin.String**|  | |

### Return type

[**SociACLShareLinkPublic**](SociACLShareLinkPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

