# ACLAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPolicyApiV1AclPoliciesPost**](ACLAPI.md#createpolicyapiv1aclpoliciespost) | **POST** /api/v1/acl/policies | Create Policy
[**enforceCheckApiV1AclEnforcePost**](ACLAPI.md#enforcecheckapiv1aclenforcepost) | **POST** /api/v1/acl/enforce | Enforce Check
[**listPoliciesApiV1AclPoliciesGet**](ACLAPI.md#listpoliciesapiv1aclpoliciesget) | **GET** /api/v1/acl/policies | List Policies
[**protectedPingApiV1AclProtectedPingGet**](ACLAPI.md#protectedpingapiv1aclprotectedpingget) | **GET** /api/v1/acl/protected-ping | Protected Ping
[**removePolicyApiV1AclPoliciesDelete**](ACLAPI.md#removepolicyapiv1aclpoliciesdelete) | **DELETE** /api/v1/acl/policies | Remove Policy


# **createPolicyApiV1AclPoliciesPost**
```swift
    open class func createPolicyApiV1AclPoliciesPost(policyRuleCreate: PolicyRuleCreate, completion: @escaping (_ data: PolicyRowResponse?, _ error: Error?) -> Void)
```

Create Policy

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let policyRuleCreate = PolicyRuleCreate(ptype: "ptype_example", rule: ["rule_example"]) // PolicyRuleCreate | 

// Create Policy
ACLAPI.createPolicyApiV1AclPoliciesPost(policyRuleCreate: policyRuleCreate) { (response, error) in
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
 **policyRuleCreate** | [**PolicyRuleCreate**](PolicyRuleCreate.md) |  | 

### Return type

[**PolicyRowResponse**](PolicyRowResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enforceCheckApiV1AclEnforcePost**
```swift
    open class func enforceCheckApiV1AclEnforcePost(enforceRequest: EnforceRequest, completion: @escaping (_ data: EnforceResponse?, _ error: Error?) -> Void)
```

Enforce Check

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let enforceRequest = EnforceRequest(model: "model_example", sub: "sub_example", obj: "obj_example", act: "act_example", extra: "extra_example") // EnforceRequest | 

// Enforce Check
ACLAPI.enforceCheckApiV1AclEnforcePost(enforceRequest: enforceRequest) { (response, error) in
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
 **enforceRequest** | [**EnforceRequest**](EnforceRequest.md) |  | 

### Return type

[**EnforceResponse**](EnforceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listPoliciesApiV1AclPoliciesGet**
```swift
    open class func listPoliciesApiV1AclPoliciesGet(completion: @escaping (_ data: [PolicyRowResponse]?, _ error: Error?) -> Void)
```

List Policies

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// List Policies
ACLAPI.listPoliciesApiV1AclPoliciesGet() { (response, error) in
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

[**[PolicyRowResponse]**](PolicyRowResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protectedPingApiV1AclProtectedPingGet**
```swift
    open class func protectedPingApiV1AclProtectedPingGet(completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Protected Ping

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Protected Ping
ACLAPI.protectedPingApiV1AclProtectedPingGet() { (response, error) in
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

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removePolicyApiV1AclPoliciesDelete**
```swift
    open class func removePolicyApiV1AclPoliciesDelete(policyRuleDelete: PolicyRuleDelete, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Remove Policy

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let policyRuleDelete = PolicyRuleDelete(ptype: "ptype_example", rule: ["rule_example"]) // PolicyRuleDelete | 

// Remove Policy
ACLAPI.removePolicyApiV1AclPoliciesDelete(policyRuleDelete: policyRuleDelete) { (response, error) in
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
 **policyRuleDelete** | [**PolicyRuleDelete**](PolicyRuleDelete.md) |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

