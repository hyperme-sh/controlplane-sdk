# UsersAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUserApiV1UsersPost**](UsersAPI.md#createuserapiv1userspost) | **POST** /api/v1/users/ | Create user (deprecated)
[**getProfileImageApiV1UsersProfileImageKeyGet**](UsersAPI.md#getprofileimageapiv1usersprofileimagekeyget) | **GET** /api/v1/users/profile/{image_key} | Get profile image URL (deprecated)
[**listUsersApiV1UsersGet**](UsersAPI.md#listusersapiv1usersget) | **GET** /api/v1/users/ | List users (deprecated)
[**patchUserApiV1UsersUserIdAssignRolePatch**](UsersAPI.md#patchuserapiv1usersuseridassignrolepatch) | **PATCH** /api/v1/users/{user_id}/assign_role | Assign user role (deprecated)
[**removeUserRoleApiV1UsersUserIdRemoveRolePatch**](UsersAPI.md#removeuserroleapiv1usersuseridremoverolepatch) | **PATCH** /api/v1/users/{user_id}/remove_role | Remove user role (deprecated)
[**updateProfilePictureApiV1UsersUserIdUpdateProfilePicturePut**](UsersAPI.md#updateprofilepictureapiv1usersuseridupdateprofilepictureput) | **PUT** /api/v1/users/{user_id}/update_profile_picture | Update profile picture (deprecated)


# **createUserApiV1UsersPost**
```swift
    open class func createUserApiV1UsersPost(createUserDto: CreateUserDto, completion: @escaping (_ data: CreateUserResponseDto?, _ error: Error?) -> Void)
```

Create user (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let createUserDto = CreateUserDto(firstName: "firstName_example", lastName: "lastName_example", email: "email_example", gender: Gender(), tenantId: "tenantId_example", roleId: "roleId_example", ssoProviderId: "ssoProviderId_example", password: "password_example", subDomain: "subDomain_example", keycloakSub: "keycloakSub_example") // CreateUserDto | 

// Create user (deprecated)
UsersAPI.createUserApiV1UsersPost(createUserDto: createUserDto) { (response, error) in
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
 **createUserDto** | [**CreateUserDto**](CreateUserDto.md) |  | 

### Return type

[**CreateUserResponseDto**](CreateUserResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getProfileImageApiV1UsersProfileImageKeyGet**
```swift
    open class func getProfileImageApiV1UsersProfileImageKeyGet(imageKey: String, completion: @escaping (_ data: UserProfileImageUpdateDto?, _ error: Error?) -> Void)
```

Get profile image URL (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let imageKey = "imageKey_example" // String | 

// Get profile image URL (deprecated)
UsersAPI.getProfileImageApiV1UsersProfileImageKeyGet(imageKey: imageKey) { (response, error) in
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
 **imageKey** | **String** |  | 

### Return type

[**UserProfileImageUpdateDto**](UserProfileImageUpdateDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listUsersApiV1UsersGet**
```swift
    open class func listUsersApiV1UsersGet(skip: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: UserListDto?, _ error: Error?) -> Void)
```

List users (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let skip = 987 // Int |  (optional) (default to 0)
let limit = 987 // Int |  (optional) (default to 10)

// List users (deprecated)
UsersAPI.listUsersApiV1UsersGet(skip: skip, limit: limit) { (response, error) in
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

[**UserListDto**](UserListDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchUserApiV1UsersUserIdAssignRolePatch**
```swift
    open class func patchUserApiV1UsersUserIdAssignRolePatch(userId: String, userRoleUpdateRequestDto: UserRoleUpdateRequestDto, completion: @escaping (_ data: UserDto?, _ error: Error?) -> Void)
```

Assign user role (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let userId = "userId_example" // String | 
let userRoleUpdateRequestDto = UserRoleUpdateRequestDto(roleId: "roleId_example") // UserRoleUpdateRequestDto | 

// Assign user role (deprecated)
UsersAPI.patchUserApiV1UsersUserIdAssignRolePatch(userId: userId, userRoleUpdateRequestDto: userRoleUpdateRequestDto) { (response, error) in
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
 **userId** | **String** |  | 
 **userRoleUpdateRequestDto** | [**UserRoleUpdateRequestDto**](UserRoleUpdateRequestDto.md) |  | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removeUserRoleApiV1UsersUserIdRemoveRolePatch**
```swift
    open class func removeUserRoleApiV1UsersUserIdRemoveRolePatch(userId: String, userRoleUpdateRequestDto: UserRoleUpdateRequestDto, completion: @escaping (_ data: UserDto?, _ error: Error?) -> Void)
```

Remove user role (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let userId = "userId_example" // String | 
let userRoleUpdateRequestDto = UserRoleUpdateRequestDto(roleId: "roleId_example") // UserRoleUpdateRequestDto | 

// Remove user role (deprecated)
UsersAPI.removeUserRoleApiV1UsersUserIdRemoveRolePatch(userId: userId, userRoleUpdateRequestDto: userRoleUpdateRequestDto) { (response, error) in
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
 **userId** | **String** |  | 
 **userRoleUpdateRequestDto** | [**UserRoleUpdateRequestDto**](UserRoleUpdateRequestDto.md) |  | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateProfilePictureApiV1UsersUserIdUpdateProfilePicturePut**
```swift
    open class func updateProfilePictureApiV1UsersUserIdUpdateProfilePicturePut(userId: String, file: String, completion: @escaping (_ data: UserProfileImageUpdateDto?, _ error: Error?) -> Void)
```

Update profile picture (deprecated)

Prefer the dedicated user-service: same paths under `/api/v1/users` (e.g. `docker compose` service `user-service`, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let userId = "userId_example" // String | 
let file = "file_example" // String | 

// Update profile picture (deprecated)
UsersAPI.updateProfilePictureApiV1UsersUserIdUpdateProfilePicturePut(userId: userId, file: file) { (response, error) in
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
 **userId** | **String** |  | 
 **file** | **String** |  | 

### Return type

[**UserProfileImageUpdateDto**](UserProfileImageUpdateDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

