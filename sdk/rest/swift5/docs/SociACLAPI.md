# SociACLAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sociaclCreateShareApiV1AclSociaclSharesPost**](SociACLAPI.md#sociaclcreateshareapiv1aclsociaclsharespost) | **POST** /api/v1/acl/sociacl/shares | Sociacl Create Share
[**sociaclEvaluateApiV1AclSociaclEvaluatePost**](SociACLAPI.md#sociaclevaluateapiv1aclsociaclevaluatepost) | **POST** /api/v1/acl/sociacl/evaluate | Sociacl Evaluate
[**sociaclRecoveryCreateApiV1AclSociaclRecoverySessionsPost**](SociACLAPI.md#sociaclrecoverycreateapiv1aclsociaclrecoverysessionspost) | **POST** /api/v1/acl/sociacl/recovery/sessions | Sociacl Recovery Create
[**sociaclRecoveryProofApiV1AclSociaclRecoverySessionsSessionIdProofPost**](SociACLAPI.md#sociaclrecoveryproofapiv1aclsociaclrecoverysessionssessionidproofpost) | **POST** /api/v1/acl/sociacl/recovery/sessions/{session_id}/proof | Sociacl Recovery Proof
[**sociaclResolveShareApiV1AclSociaclSharesByTokenTokenGet**](SociACLAPI.md#sociaclresolveshareapiv1aclsociaclsharesbytokentokenget) | **GET** /api/v1/acl/sociacl/shares/by-token/{token} | Sociacl Resolve Share


# **sociaclCreateShareApiV1AclSociaclSharesPost**
```swift
    open class func sociaclCreateShareApiV1AclSociaclSharesPost(sociACLShareLinkCreate: SociACLShareLinkCreate, completion: @escaping (_ data: SociaclShareCreatedResponse?, _ error: Error?) -> Void)
```

Sociacl Create Share

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let sociACLShareLinkCreate = SociACLShareLinkCreate(resourceKind: SociACLResourceKind(), ownerUserId: 123, groupId: 123, resourceDescriptor: "TODO", predicate: SociACLPredicate(minVerificationLevel: 123, minVouchCount: 123, maxDistanceKm: 123, requiredPoliticalTolerance: PoliticalViewCategory(), memberOfGroupId: 123, crossNetworkHandleAllowlist: ["crossNetworkHandleAllowlist_example"], crossNetworkHandleBlocklist: ["crossNetworkHandleBlocklist_example"]), mode: SociACLShareMode(), expiresAt: "expiresAt_example", maxUses: 123) // SociACLShareLinkCreate | 

// Sociacl Create Share
SociACLAPI.sociaclCreateShareApiV1AclSociaclSharesPost(sociACLShareLinkCreate: sociACLShareLinkCreate) { (response, error) in
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
 **sociACLShareLinkCreate** | [**SociACLShareLinkCreate**](SociACLShareLinkCreate.md) |  | 

### Return type

[**SociaclShareCreatedResponse**](SociaclShareCreatedResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sociaclEvaluateApiV1AclSociaclEvaluatePost**
```swift
    open class func sociaclEvaluateApiV1AclSociaclEvaluatePost(sociACLEvaluateRequest: SociACLEvaluateRequest, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Sociacl Evaluate

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let sociACLEvaluateRequest = SociACLEvaluateRequest(token: "token_example", context: SociACLRequestContext(sub: "sub_example", politicalView: PoliticalViewCategory(), verificationLevel: 123, vouchCount: 123, vouchSource: "vouchSource_example", crossNetworkHandle: "crossNetworkHandle_example", distanceKm: 123, distanceSource: SociACLDistanceSource()), ownerAttributes: SociACLAttributes(politicalView: nil, sexualOrientation: SexualOrientationCategory(), verificationLevel: 123, notes: "notes_example")) // SociACLEvaluateRequest | 

// Sociacl Evaluate
SociACLAPI.sociaclEvaluateApiV1AclSociaclEvaluatePost(sociACLEvaluateRequest: sociACLEvaluateRequest) { (response, error) in
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
 **sociACLEvaluateRequest** | [**SociACLEvaluateRequest**](SociACLEvaluateRequest.md) |  | 

### Return type

**AnyCodable**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sociaclRecoveryCreateApiV1AclSociaclRecoverySessionsPost**
```swift
    open class func sociaclRecoveryCreateApiV1AclSociaclRecoverySessionsPost(recoverySessionCreate: RecoverySessionCreate, completion: @escaping (_ data: RecoverySessionResponse?, _ error: Error?) -> Void)
```

Sociacl Recovery Create

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let recoverySessionCreate = RecoverySessionCreate(idempotencyKey: "idempotencyKey_example", metadata: "TODO") // RecoverySessionCreate | 

// Sociacl Recovery Create
SociACLAPI.sociaclRecoveryCreateApiV1AclSociaclRecoverySessionsPost(recoverySessionCreate: recoverySessionCreate) { (response, error) in
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
 **recoverySessionCreate** | [**RecoverySessionCreate**](RecoverySessionCreate.md) |  | 

### Return type

[**RecoverySessionResponse**](RecoverySessionResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sociaclRecoveryProofApiV1AclSociaclRecoverySessionsSessionIdProofPost**
```swift
    open class func sociaclRecoveryProofApiV1AclSociaclRecoverySessionsSessionIdProofPost(sessionId: UUID, recoveryProofRequest: RecoveryProofRequest, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Sociacl Recovery Proof

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let sessionId = 987 // UUID | 
let recoveryProofRequest = RecoveryProofRequest(proofType: "proofType_example", payload: "TODO") // RecoveryProofRequest | 

// Sociacl Recovery Proof
SociACLAPI.sociaclRecoveryProofApiV1AclSociaclRecoverySessionsSessionIdProofPost(sessionId: sessionId, recoveryProofRequest: recoveryProofRequest) { (response, error) in
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
 **sessionId** | **UUID** |  | 
 **recoveryProofRequest** | [**RecoveryProofRequest**](RecoveryProofRequest.md) |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sociaclResolveShareApiV1AclSociaclSharesByTokenTokenGet**
```swift
    open class func sociaclResolveShareApiV1AclSociaclSharesByTokenTokenGet(token: String, completion: @escaping (_ data: SociACLShareLinkPublic?, _ error: Error?) -> Void)
```

Sociacl Resolve Share

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let token = "token_example" // String | 

// Sociacl Resolve Share
SociACLAPI.sociaclResolveShareApiV1AclSociaclSharesByTokenTokenGet(token: token) { (response, error) in
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
 **token** | **String** |  | 

### Return type

[**SociACLShareLinkPublic**](SociACLShareLinkPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

