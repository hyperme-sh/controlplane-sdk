package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.CreateUserDto
import org.openapitools.client.models.CreateUserResponseDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.UserDto
import org.openapitools.client.models.UserListDto
import org.openapitools.client.models.UserProfileImageUpdateDto
import org.openapitools.client.models.UserRoleUpdateRequestDto

interface UsersApi {
    /**
     * Create user (deprecated)
     * Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param createUserDto 
     * @return [CreateUserResponseDto]
     */
    @Deprecated("This api was deprecated")
    @POST("api/v1/users/")
    suspend fun createUserApiV1UsersPost(@Body createUserDto: CreateUserDto): Response<CreateUserResponseDto>

    /**
     * Get profile image URL (deprecated)
     * Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param imageKey 
     * @return [UserProfileImageUpdateDto]
     */
    @Deprecated("This api was deprecated")
    @GET("api/v1/users/profile/{image_key}")
    suspend fun getProfileImageApiV1UsersProfileImageKeyGet(@Path("image_key") imageKey: kotlin.String): Response<UserProfileImageUpdateDto>

    /**
     * List users (deprecated)
     * Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param skip  (optional, default to 0)
     * @param limit  (optional, default to 10)
     * @return [UserListDto]
     */
    @Deprecated("This api was deprecated")
    @GET("api/v1/users/")
    suspend fun listUsersApiV1UsersGet(@Query("skip") skip: kotlin.Int? = 0, @Query("limit") limit: kotlin.Int? = 10): Response<UserListDto>

    /**
     * Assign user role (deprecated)
     * Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param userId 
     * @param userRoleUpdateRequestDto 
     * @return [UserDto]
     */
    @Deprecated("This api was deprecated")
    @PATCH("api/v1/users/{user_id}/assign_role")
    suspend fun patchUserApiV1UsersUserIdAssignRolePatch(@Path("user_id") userId: kotlin.String, @Body userRoleUpdateRequestDto: UserRoleUpdateRequestDto): Response<UserDto>

    /**
     * Remove user role (deprecated)
     * Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param userId 
     * @param userRoleUpdateRequestDto 
     * @return [UserDto]
     */
    @Deprecated("This api was deprecated")
    @PATCH("api/v1/users/{user_id}/remove_role")
    suspend fun removeUserRoleApiV1UsersUserIdRemoveRolePatch(@Path("user_id") userId: kotlin.String, @Body userRoleUpdateRequestDto: UserRoleUpdateRequestDto): Response<UserDto>

    /**
     * Update profile picture (deprecated)
     * Prefer the dedicated user-service: same paths under &#x60;/api/v1/users&#x60; (e.g. &#x60;docker compose&#x60; service &#x60;user-service&#x60;, host port 8002). This monolith route remains for backward compatibility and will be removed later.
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param userId 
     * @param file 
     * @return [UserProfileImageUpdateDto]
     */
    @Deprecated("This api was deprecated")
    @Multipart
    @PUT("api/v1/users/{user_id}/update_profile_picture")
    suspend fun updateProfilePictureApiV1UsersUserIdUpdateProfilePicturePut(@Path("user_id") userId: kotlin.String, @Part("file") file: kotlin.String): Response<UserProfileImageUpdateDto>

}
