# RolesAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRoleApiV1RolesPost**](RolesAPI.md#createroleapiv1rolespost) | **POST** /api/v1/roles/ | Create Role
[**deleteRoleApiV1RolesRoleIdDelete**](RolesAPI.md#deleteroleapiv1rolesroleiddelete) | **DELETE** /api/v1/roles/{role_id} | Delete Role
[**getRoleApiV1RolesRoleIdGet**](RolesAPI.md#getroleapiv1rolesroleidget) | **GET** /api/v1/roles/{role_id} | Get Role
[**listRolesApiV1RolesGet**](RolesAPI.md#listrolesapiv1rolesget) | **GET** /api/v1/roles/ | List Roles
[**searchRoleByNameApiV1RolesSearchByNameGet**](RolesAPI.md#searchrolebynameapiv1rolessearchbynameget) | **GET** /api/v1/roles/search_by_name | Search Role By Name
[**updateRoleApiV1RolesRoleIdPut**](RolesAPI.md#updateroleapiv1rolesroleidput) | **PUT** /api/v1/roles/{role_id} | Update Role


# **createRoleApiV1RolesPost**
```swift
    open class func createRoleApiV1RolesPost(createRoleDto: CreateRoleDto, completion: @escaping (_ data: CreateRoleResponseDto?, _ error: Error?) -> Void)
```

Create Role

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let createRoleDto = CreateRoleDto(name: "name_example", description: "description_example", tenantId: "tenantId_example") // CreateRoleDto | 

// Create Role
RolesAPI.createRoleApiV1RolesPost(createRoleDto: createRoleDto) { (response, error) in
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
 **createRoleDto** | [**CreateRoleDto**](CreateRoleDto.md) |  | 

### Return type

[**CreateRoleResponseDto**](CreateRoleResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteRoleApiV1RolesRoleIdDelete**
```swift
    open class func deleteRoleApiV1RolesRoleIdDelete(roleId: String, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Delete Role

Deletes a role if it is not assigned to any users.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let roleId = "roleId_example" // String | 

// Delete Role
RolesAPI.deleteRoleApiV1RolesRoleIdDelete(roleId: roleId) { (response, error) in
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
 **roleId** | **String** |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getRoleApiV1RolesRoleIdGet**
```swift
    open class func getRoleApiV1RolesRoleIdGet(roleId: String, completion: @escaping (_ data: RoleDto?, _ error: Error?) -> Void)
```

Get Role

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let roleId = "roleId_example" // String | 

// Get Role
RolesAPI.getRoleApiV1RolesRoleIdGet(roleId: roleId) { (response, error) in
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
 **roleId** | **String** |  | 

### Return type

[**RoleDto**](RoleDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listRolesApiV1RolesGet**
```swift
    open class func listRolesApiV1RolesGet(skip: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: RoleListDto?, _ error: Error?) -> Void)
```

List Roles

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let skip = 987 // Int |  (optional) (default to 0)
let limit = 987 // Int |  (optional) (default to 10)

// List Roles
RolesAPI.listRolesApiV1RolesGet(skip: skip, limit: limit) { (response, error) in
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

[**RoleListDto**](RoleListDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchRoleByNameApiV1RolesSearchByNameGet**
```swift
    open class func searchRoleByNameApiV1RolesSearchByNameGet(name: String, completion: @escaping (_ data: [RoleDto]?, _ error: Error?) -> Void)
```

Search Role By Name

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let name = "name_example" // String | 

// Search Role By Name
RolesAPI.searchRoleByNameApiV1RolesSearchByNameGet(name: name) { (response, error) in
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

[**[RoleDto]**](RoleDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateRoleApiV1RolesRoleIdPut**
```swift
    open class func updateRoleApiV1RolesRoleIdPut(roleId: String, updateRoleDto: UpdateRoleDto, completion: @escaping (_ data: RoleDto?, _ error: Error?) -> Void)
```

Update Role

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let roleId = "roleId_example" // String | 
let updateRoleDto = UpdateRoleDto(name: "name_example", description: "description_example", tenantId: "tenantId_example", permissions: [Permission()]) // UpdateRoleDto | 

// Update Role
RolesAPI.updateRoleApiV1RolesRoleIdPut(roleId: roleId, updateRoleDto: updateRoleDto) { (response, error) in
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
 **roleId** | **String** |  | 
 **updateRoleDto** | [**UpdateRoleDto**](UpdateRoleDto.md) |  | 

### Return type

[**RoleDto**](RoleDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

