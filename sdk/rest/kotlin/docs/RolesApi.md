# RolesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createRoleApiV1RolesPost**](RolesApi.md#createRoleApiV1RolesPost) | **POST** api/v1/roles/ | Create Role |
| [**deleteRoleApiV1RolesRoleIdDelete**](RolesApi.md#deleteRoleApiV1RolesRoleIdDelete) | **DELETE** api/v1/roles/{role_id} | Delete Role |
| [**getRoleApiV1RolesRoleIdGet**](RolesApi.md#getRoleApiV1RolesRoleIdGet) | **GET** api/v1/roles/{role_id} | Get Role |
| [**listRolesApiV1RolesGet**](RolesApi.md#listRolesApiV1RolesGet) | **GET** api/v1/roles/ | List Roles |
| [**searchRoleByNameApiV1RolesSearchByNameGet**](RolesApi.md#searchRoleByNameApiV1RolesSearchByNameGet) | **GET** api/v1/roles/search_by_name | Search Role By Name |
| [**updateRoleApiV1RolesRoleIdPut**](RolesApi.md#updateRoleApiV1RolesRoleIdPut) | **PUT** api/v1/roles/{role_id} | Update Role |



Create Role

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(RolesApi::class.java)
val createRoleDto : CreateRoleDto =  // CreateRoleDto | 

launch(Dispatchers.IO) {
    val result : CreateRoleResponseDto = webService.createRoleApiV1RolesPost(createRoleDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createRoleDto** | [**CreateRoleDto**](CreateRoleDto.md)|  | |

### Return type

[**CreateRoleResponseDto**](CreateRoleResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Delete Role

Deletes a role if it is not assigned to any users.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(RolesApi::class.java)
val roleId : kotlin.String = roleId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.deleteRoleApiV1RolesRoleIdDelete(roleId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **roleId** | **kotlin.String**|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Role

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(RolesApi::class.java)
val roleId : kotlin.String = roleId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : RoleDto = webService.getRoleApiV1RolesRoleIdGet(roleId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **roleId** | **kotlin.String**|  | |

### Return type

[**RoleDto**](RoleDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List Roles

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(RolesApi::class.java)
val skip : kotlin.Int = 56 // kotlin.Int | 
val limit : kotlin.Int = 56 // kotlin.Int | 

launch(Dispatchers.IO) {
    val result : RoleListDto = webService.listRolesApiV1RolesGet(skip, limit)
}
```

### Parameters
| **skip** | **kotlin.Int**|  | [optional] [default to 0] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **kotlin.Int**|  | [optional] [default to 10] |

### Return type

[**RoleListDto**](RoleListDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Search Role By Name

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(RolesApi::class.java)
val name : kotlin.String = name_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<RoleDto> = webService.searchRoleByNameApiV1RolesSearchByNameGet(name)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **kotlin.String**|  | |

### Return type

[**kotlin.collections.List&lt;RoleDto&gt;**](RoleDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Update Role

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(RolesApi::class.java)
val roleId : kotlin.String = roleId_example // kotlin.String | 
val updateRoleDto : UpdateRoleDto =  // UpdateRoleDto | 

launch(Dispatchers.IO) {
    val result : RoleDto = webService.updateRoleApiV1RolesRoleIdPut(roleId, updateRoleDto)
}
```

### Parameters
| **roleId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **updateRoleDto** | [**UpdateRoleDto**](UpdateRoleDto.md)|  | |

### Return type

[**RoleDto**](RoleDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

