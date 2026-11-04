# UsersGroupsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addUserToGroupApiV1UsersUserIdGroupsGroupIdPost**](UsersGroupsAPI.md#addusertogroupapiv1usersuseridgroupsgroupidpost) | **POST** /api/v1/users/{user_id}/groups/{group_id} | Add User To Group
[**createGroupApiV1GroupsPost**](UsersGroupsAPI.md#creategroupapiv1groupspost) | **POST** /api/v1/groups | Create Group
[**createOrganizationApiV1OrganizationsPost**](UsersGroupsAPI.md#createorganizationapiv1organizationspost) | **POST** /api/v1/organizations | Create Organization
[**createUserApiV1UsersPost**](UsersGroupsAPI.md#createuserapiv1userspost) | **POST** /api/v1/users | Create User
[**deleteUserApiV1UsersUserIdDelete**](UsersGroupsAPI.md#deleteuserapiv1usersuseriddelete) | **DELETE** /api/v1/users/{user_id} | Delete User
[**getGroupApiV1GroupsGroupIdGet**](UsersGroupsAPI.md#getgroupapiv1groupsgroupidget) | **GET** /api/v1/groups/{group_id} | Get Group
[**getOrganizationApiV1OrganizationsOrganizationIdGet**](UsersGroupsAPI.md#getorganizationapiv1organizationsorganizationidget) | **GET** /api/v1/organizations/{organization_id} | Get Organization
[**listGroupsApiV1GroupsGet**](UsersGroupsAPI.md#listgroupsapiv1groupsget) | **GET** /api/v1/groups | List Groups
[**listOrganizationsApiV1OrganizationsGet**](UsersGroupsAPI.md#listorganizationsapiv1organizationsget) | **GET** /api/v1/organizations | List Organizations
[**listUsersApiV1UsersGet**](UsersGroupsAPI.md#listusersapiv1usersget) | **GET** /api/v1/users | List Users
[**updateUserApiV1UsersUserIdPatch**](UsersGroupsAPI.md#updateuserapiv1usersuseridpatch) | **PATCH** /api/v1/users/{user_id} | Update User


# **addUserToGroupApiV1UsersUserIdGroupsGroupIdPost**
```swift
    open class func addUserToGroupApiV1UsersUserIdGroupsGroupIdPost(userId: UUID, groupId: UUID, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Add User To Group

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let userId = 987 // UUID | 
let groupId = 987 // UUID | 

// Add User To Group
UsersGroupsAPI.addUserToGroupApiV1UsersUserIdGroupsGroupIdPost(userId: userId, groupId: groupId) { (response, error) in
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
 **userId** | **UUID** |  | 
 **groupId** | **UUID** |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createGroupApiV1GroupsPost**
```swift
    open class func createGroupApiV1GroupsPost(groupCreateBody: GroupCreateBody, completion: @escaping (_ data: GroupResponse?, _ error: Error?) -> Void)
```

Create Group

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let groupCreateBody = GroupCreateBody(name: "name_example", description: "description_example", roleId: 123) // GroupCreateBody | 

// Create Group
UsersGroupsAPI.createGroupApiV1GroupsPost(groupCreateBody: groupCreateBody) { (response, error) in
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
 **groupCreateBody** | [**GroupCreateBody**](GroupCreateBody.md) |  | 

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createOrganizationApiV1OrganizationsPost**
```swift
    open class func createOrganizationApiV1OrganizationsPost(organizationCreateBody: OrganizationCreateBody, completion: @escaping (_ data: OrganizationResponse?, _ error: Error?) -> Void)
```

Create Organization

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let organizationCreateBody = OrganizationCreateBody(legalName: "legalName_example") // OrganizationCreateBody | 

// Create Organization
UsersGroupsAPI.createOrganizationApiV1OrganizationsPost(organizationCreateBody: organizationCreateBody) { (response, error) in
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
 **organizationCreateBody** | [**OrganizationCreateBody**](OrganizationCreateBody.md) |  | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createUserApiV1UsersPost**
```swift
    open class func createUserApiV1UsersPost(userCreateBody: UserCreateBody, completion: @escaping (_ data: UserResponse?, _ error: Error?) -> Void)
```

Create User

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let userCreateBody = UserCreateBody(email: "email_example", firstName: "firstName_example", lastName: "lastName_example", gender: "gender_example", isActive: false) // UserCreateBody | 

// Create User
UsersGroupsAPI.createUserApiV1UsersPost(userCreateBody: userCreateBody) { (response, error) in
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
 **userCreateBody** | [**UserCreateBody**](UserCreateBody.md) |  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteUserApiV1UsersUserIdDelete**
```swift
    open class func deleteUserApiV1UsersUserIdDelete(userId: UUID, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Delete User

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let userId = 987 // UUID | 

// Delete User
UsersGroupsAPI.deleteUserApiV1UsersUserIdDelete(userId: userId) { (response, error) in
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
 **userId** | **UUID** |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getGroupApiV1GroupsGroupIdGet**
```swift
    open class func getGroupApiV1GroupsGroupIdGet(groupId: UUID, completion: @escaping (_ data: GroupResponse?, _ error: Error?) -> Void)
```

Get Group

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let groupId = 987 // UUID | 

// Get Group
UsersGroupsAPI.getGroupApiV1GroupsGroupIdGet(groupId: groupId) { (response, error) in
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
 **groupId** | **UUID** |  | 

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getOrganizationApiV1OrganizationsOrganizationIdGet**
```swift
    open class func getOrganizationApiV1OrganizationsOrganizationIdGet(organizationId: UUID, completion: @escaping (_ data: OrganizationResponse?, _ error: Error?) -> Void)
```

Get Organization

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let organizationId = 987 // UUID | 

// Get Organization
UsersGroupsAPI.getOrganizationApiV1OrganizationsOrganizationIdGet(organizationId: organizationId) { (response, error) in
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
 **organizationId** | **UUID** |  | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listGroupsApiV1GroupsGet**
```swift
    open class func listGroupsApiV1GroupsGet(limit: Int? = nil, offset: Int? = nil, q: String? = nil, completion: @escaping (_ data: GroupListPage?, _ error: Error?) -> Void)
```

List Groups

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let limit = 987 // Int |  (optional) (default to 50)
let offset = 987 // Int |  (optional) (default to 0)
let q = "q_example" // String | Case-insensitive search on name or description (optional)

// List Groups
UsersGroupsAPI.listGroupsApiV1GroupsGet(limit: limit, offset: offset, q: q) { (response, error) in
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
 **limit** | **Int** |  | [optional] [default to 50]
 **offset** | **Int** |  | [optional] [default to 0]
 **q** | **String** | Case-insensitive search on name or description | [optional] 

### Return type

[**GroupListPage**](GroupListPage.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listOrganizationsApiV1OrganizationsGet**
```swift
    open class func listOrganizationsApiV1OrganizationsGet(limit: Int? = nil, offset: Int? = nil, q: String? = nil, completion: @escaping (_ data: OrganizationListPage?, _ error: Error?) -> Void)
```

List Organizations

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let limit = 987 // Int |  (optional) (default to 50)
let offset = 987 // Int |  (optional) (default to 0)
let q = "q_example" // String | Case-insensitive search on legal name (optional)

// List Organizations
UsersGroupsAPI.listOrganizationsApiV1OrganizationsGet(limit: limit, offset: offset, q: q) { (response, error) in
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
 **limit** | **Int** |  | [optional] [default to 50]
 **offset** | **Int** |  | [optional] [default to 0]
 **q** | **String** | Case-insensitive search on legal name | [optional] 

### Return type

[**OrganizationListPage**](OrganizationListPage.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listUsersApiV1UsersGet**
```swift
    open class func listUsersApiV1UsersGet(limit: Int? = nil, offset: Int? = nil, q: String? = nil, completion: @escaping (_ data: UserListPage?, _ error: Error?) -> Void)
```

List Users

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let limit = 987 // Int |  (optional) (default to 50)
let offset = 987 // Int |  (optional) (default to 0)
let q = "q_example" // String |  (optional)

// List Users
UsersGroupsAPI.listUsersApiV1UsersGet(limit: limit, offset: offset, q: q) { (response, error) in
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
 **limit** | **Int** |  | [optional] [default to 50]
 **offset** | **Int** |  | [optional] [default to 0]
 **q** | **String** |  | [optional] 

### Return type

[**UserListPage**](UserListPage.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateUserApiV1UsersUserIdPatch**
```swift
    open class func updateUserApiV1UsersUserIdPatch(userId: UUID, userUpdateBody: UserUpdateBody, completion: @escaping (_ data: UserResponse?, _ error: Error?) -> Void)
```

Update User

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let userId = 987 // UUID | 
let userUpdateBody = UserUpdateBody(firstName: "firstName_example", lastName: "lastName_example", sociaclAttributes: SociACLAttributes(politicalView: PoliticalViewCategory(), sexualOrientation: SexualOrientationCategory(), verificationLevel: 123, notes: "notes_example")) // UserUpdateBody | 

// Update User
UsersGroupsAPI.updateUserApiV1UsersUserIdPatch(userId: userId, userUpdateBody: userUpdateBody) { (response, error) in
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
 **userId** | **UUID** |  | 
 **userUpdateBody** | [**UserUpdateBody**](UserUpdateBody.md) |  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

