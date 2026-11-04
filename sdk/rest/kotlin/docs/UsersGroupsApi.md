# UsersGroupsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addUserToGroupApiV1UsersUserIdGroupsGroupIdPost**](UsersGroupsApi.md#addUserToGroupApiV1UsersUserIdGroupsGroupIdPost) | **POST** api/v1/users/{user_id}/groups/{group_id} | Add User To Group |
| [**createGroupApiV1GroupsPost**](UsersGroupsApi.md#createGroupApiV1GroupsPost) | **POST** api/v1/groups | Create Group |
| [**createOrganizationApiV1OrganizationsPost**](UsersGroupsApi.md#createOrganizationApiV1OrganizationsPost) | **POST** api/v1/organizations | Create Organization |
| [**createUserApiV1UsersPost**](UsersGroupsApi.md#createUserApiV1UsersPost) | **POST** api/v1/users | Create User |
| [**deleteUserApiV1UsersUserIdDelete**](UsersGroupsApi.md#deleteUserApiV1UsersUserIdDelete) | **DELETE** api/v1/users/{user_id} | Delete User |
| [**getGroupApiV1GroupsGroupIdGet**](UsersGroupsApi.md#getGroupApiV1GroupsGroupIdGet) | **GET** api/v1/groups/{group_id} | Get Group |
| [**getOrganizationApiV1OrganizationsOrganizationIdGet**](UsersGroupsApi.md#getOrganizationApiV1OrganizationsOrganizationIdGet) | **GET** api/v1/organizations/{organization_id} | Get Organization |
| [**listGroupsApiV1GroupsGet**](UsersGroupsApi.md#listGroupsApiV1GroupsGet) | **GET** api/v1/groups | List Groups |
| [**listOrganizationsApiV1OrganizationsGet**](UsersGroupsApi.md#listOrganizationsApiV1OrganizationsGet) | **GET** api/v1/organizations | List Organizations |
| [**listUsersApiV1UsersGet**](UsersGroupsApi.md#listUsersApiV1UsersGet) | **GET** api/v1/users | List Users |
| [**updateUserApiV1UsersUserIdPatch**](UsersGroupsApi.md#updateUserApiV1UsersUserIdPatch) | **PATCH** api/v1/users/{user_id} | Update User |



Add User To Group

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val userId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val groupId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.addUserToGroupApiV1UsersUserIdGroupsGroupIdPost(userId, groupId)
}
```

### Parameters
| **userId** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **groupId** | **java.util.UUID**|  | |

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


Create Group

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val groupCreateBody : GroupCreateBody =  // GroupCreateBody | 

launch(Dispatchers.IO) {
    val result : GroupResponse = webService.createGroupApiV1GroupsPost(groupCreateBody)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **groupCreateBody** | [**GroupCreateBody**](GroupCreateBody.md)|  | |

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Create Organization

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val organizationCreateBody : OrganizationCreateBody =  // OrganizationCreateBody | 

launch(Dispatchers.IO) {
    val result : OrganizationResponse = webService.createOrganizationApiV1OrganizationsPost(organizationCreateBody)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organizationCreateBody** | [**OrganizationCreateBody**](OrganizationCreateBody.md)|  | |

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Create User

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val userCreateBody : UserCreateBody =  // UserCreateBody | 

launch(Dispatchers.IO) {
    val result : UserResponse = webService.createUserApiV1UsersPost(userCreateBody)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **userCreateBody** | [**UserCreateBody**](UserCreateBody.md)|  | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Delete User

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val userId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    webService.deleteUserApiV1UsersUserIdDelete(userId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **userId** | **java.util.UUID**|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Group

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val groupId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : GroupResponse = webService.getGroupApiV1GroupsGroupIdGet(groupId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **groupId** | **java.util.UUID**|  | |

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Organization

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val organizationId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 

launch(Dispatchers.IO) {
    val result : OrganizationResponse = webService.getOrganizationApiV1OrganizationsOrganizationIdGet(organizationId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organizationId** | **java.util.UUID**|  | |

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List Groups

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val limit : kotlin.Int = 56 // kotlin.Int | 
val offset : kotlin.Int = 56 // kotlin.Int | 
val q : kotlin.String = q_example // kotlin.String | Case-insensitive search on name or description

launch(Dispatchers.IO) {
    val result : GroupListPage = webService.listGroupsApiV1GroupsGet(limit, offset, q)
}
```

### Parameters
| **limit** | **kotlin.Int**|  | [optional] [default to 50] |
| **offset** | **kotlin.Int**|  | [optional] [default to 0] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **q** | **kotlin.String**| Case-insensitive search on name or description | [optional] |

### Return type

[**GroupListPage**](GroupListPage.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List Organizations

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val limit : kotlin.Int = 56 // kotlin.Int | 
val offset : kotlin.Int = 56 // kotlin.Int | 
val q : kotlin.String = q_example // kotlin.String | Case-insensitive search on legal name

launch(Dispatchers.IO) {
    val result : OrganizationListPage = webService.listOrganizationsApiV1OrganizationsGet(limit, offset, q)
}
```

### Parameters
| **limit** | **kotlin.Int**|  | [optional] [default to 50] |
| **offset** | **kotlin.Int**|  | [optional] [default to 0] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **q** | **kotlin.String**| Case-insensitive search on legal name | [optional] |

### Return type

[**OrganizationListPage**](OrganizationListPage.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List Users

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val limit : kotlin.Int = 56 // kotlin.Int | 
val offset : kotlin.Int = 56 // kotlin.Int | 
val q : kotlin.String = q_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : UserListPage = webService.listUsersApiV1UsersGet(limit, offset, q)
}
```

### Parameters
| **limit** | **kotlin.Int**|  | [optional] [default to 50] |
| **offset** | **kotlin.Int**|  | [optional] [default to 0] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **q** | **kotlin.String**|  | [optional] |

### Return type

[**UserListPage**](UserListPage.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Update User

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersGroupsApi::class.java)
val userId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val userUpdateBody : UserUpdateBody =  // UserUpdateBody | 

launch(Dispatchers.IO) {
    val result : UserResponse = webService.updateUserApiV1UsersUserIdPatch(userId, userUpdateBody)
}
```

### Parameters
| **userId** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **userUpdateBody** | [**UserUpdateBody**](UserUpdateBody.md)|  | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

