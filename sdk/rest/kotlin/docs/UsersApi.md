# UsersApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createUserApiV1UsersPost**](UsersApi.md#createUserApiV1UsersPost) | **POST** api/v1/users/ | Create user (deprecated) |
| [**getProfileImageApiV1UsersProfileImageKeyGet**](UsersApi.md#getProfileImageApiV1UsersProfileImageKeyGet) | **GET** api/v1/users/profile/{image_key} | Get profile image URL (deprecated) |
| [**listUsersApiV1UsersGet**](UsersApi.md#listUsersApiV1UsersGet) | **GET** api/v1/users/ | List users (deprecated) |
| [**patchUserApiV1UsersUserIdAssignRolePatch**](UsersApi.md#patchUserApiV1UsersUserIdAssignRolePatch) | **PATCH** api/v1/users/{user_id}/assign_role | Assign user role (deprecated) |
| [**removeUserRoleApiV1UsersUserIdRemoveRolePatch**](UsersApi.md#removeUserRoleApiV1UsersUserIdRemoveRolePatch) | **PATCH** api/v1/users/{user_id}/remove_role | Remove user role (deprecated) |
| [**updateProfilePictureApiV1UsersUserIdUpdateProfilePicturePut**](UsersApi.md#updateProfilePictureApiV1UsersUserIdUpdateProfilePicturePut) | **PUT** api/v1/users/{user_id}/update_profile_picture | Update profile picture (deprecated) |



Create user (deprecated)

Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersApi::class.java)
val createUserDto : CreateUserDto =  // CreateUserDto | 

launch(Dispatchers.IO) {
    val result : CreateUserResponseDto = webService.createUserApiV1UsersPost(createUserDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createUserDto** | [**CreateUserDto**](CreateUserDto.md)|  | |

### Return type

[**CreateUserResponseDto**](CreateUserResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Get profile image URL (deprecated)

Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersApi::class.java)
val imageKey : kotlin.String = imageKey_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : UserProfileImageUpdateDto = webService.getProfileImageApiV1UsersProfileImageKeyGet(imageKey)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **imageKey** | **kotlin.String**|  | |

### Return type

[**UserProfileImageUpdateDto**](UserProfileImageUpdateDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


List users (deprecated)

Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersApi::class.java)
val skip : kotlin.Int = 56 // kotlin.Int | 
val limit : kotlin.Int = 56 // kotlin.Int | 

launch(Dispatchers.IO) {
    val result : UserListDto = webService.listUsersApiV1UsersGet(skip, limit)
}
```

### Parameters
| **skip** | **kotlin.Int**|  | [optional] [default to 0] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **kotlin.Int**|  | [optional] [default to 10] |

### Return type

[**UserListDto**](UserListDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Assign user role (deprecated)

Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersApi::class.java)
val userId : kotlin.String = userId_example // kotlin.String | 
val userRoleUpdateRequestDto : UserRoleUpdateRequestDto =  // UserRoleUpdateRequestDto | 

launch(Dispatchers.IO) {
    val result : UserDto = webService.patchUserApiV1UsersUserIdAssignRolePatch(userId, userRoleUpdateRequestDto)
}
```

### Parameters
| **userId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **userRoleUpdateRequestDto** | [**UserRoleUpdateRequestDto**](UserRoleUpdateRequestDto.md)|  | |

### Return type

[**UserDto**](UserDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Remove user role (deprecated)

Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersApi::class.java)
val userId : kotlin.String = userId_example // kotlin.String | 
val userRoleUpdateRequestDto : UserRoleUpdateRequestDto =  // UserRoleUpdateRequestDto | 

launch(Dispatchers.IO) {
    val result : UserDto = webService.removeUserRoleApiV1UsersUserIdRemoveRolePatch(userId, userRoleUpdateRequestDto)
}
```

### Parameters
| **userId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **userRoleUpdateRequestDto** | [**UserRoleUpdateRequestDto**](UserRoleUpdateRequestDto.md)|  | |

### Return type

[**UserDto**](UserDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Update profile picture (deprecated)

Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(UsersApi::class.java)
val userId : kotlin.String = userId_example // kotlin.String | 
val file : kotlin.String = file_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : UserProfileImageUpdateDto = webService.updateProfilePictureApiV1UsersUserIdUpdateProfilePicturePut(userId, file)
}
```

### Parameters
| **userId** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **file** | **kotlin.String**|  | |

### Return type

[**UserProfileImageUpdateDto**](UserProfileImageUpdateDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

