package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.GroupCreateBody
import org.openapitools.client.models.GroupListPage
import org.openapitools.client.models.GroupResponse
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.OrganizationCreateBody
import org.openapitools.client.models.OrganizationListPage
import org.openapitools.client.models.OrganizationResponse
import org.openapitools.client.models.UserCreateBody
import org.openapitools.client.models.UserListPage
import org.openapitools.client.models.UserResponse
import org.openapitools.client.models.UserUpdateBody

interface UsersGroupsApi {
    /**
     * Add User To Group
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param userId 
     * @param groupId 
     * @return [kotlin.Any]
     */
    @POST("api/v1/users/{user_id}/groups/{group_id}")
    suspend fun addUserToGroupApiV1UsersUserIdGroupsGroupIdPost(@Path("user_id") userId: java.util.UUID, @Path("group_id") groupId: java.util.UUID): Response<kotlin.Any>

    /**
     * Create Group
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param groupCreateBody 
     * @return [GroupResponse]
     */
    @POST("api/v1/groups")
    suspend fun createGroupApiV1GroupsPost(@Body groupCreateBody: GroupCreateBody): Response<GroupResponse>

    /**
     * Create Organization
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param organizationCreateBody 
     * @return [OrganizationResponse]
     */
    @POST("api/v1/organizations")
    suspend fun createOrganizationApiV1OrganizationsPost(@Body organizationCreateBody: OrganizationCreateBody): Response<OrganizationResponse>

    /**
     * Create User
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param userCreateBody 
     * @return [UserResponse]
     */
    @POST("api/v1/users")
    suspend fun createUserApiV1UsersPost(@Body userCreateBody: UserCreateBody): Response<UserResponse>

    /**
     * Delete User
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param userId 
     * @return [Unit]
     */
    @DELETE("api/v1/users/{user_id}")
    suspend fun deleteUserApiV1UsersUserIdDelete(@Path("user_id") userId: java.util.UUID): Response<Unit>

    /**
     * Get Group
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 404: Group not found
     *
     * @param groupId 
     * @return [GroupResponse]
     */
    @GET("api/v1/groups/{group_id}")
    suspend fun getGroupApiV1GroupsGroupIdGet(@Path("group_id") groupId: java.util.UUID): Response<GroupResponse>

    /**
     * Get Organization
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 404: Organization not found
     *
     * @param organizationId 
     * @return [OrganizationResponse]
     */
    @GET("api/v1/organizations/{organization_id}")
    suspend fun getOrganizationApiV1OrganizationsOrganizationIdGet(@Path("organization_id") organizationId: java.util.UUID): Response<OrganizationResponse>

    /**
     * List Groups
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @param limit  (optional, default to 50)
     * @param offset  (optional, default to 0)
     * @param q Case-insensitive search on name or description (optional)
     * @return [GroupListPage]
     */
    @GET("api/v1/groups")
    suspend fun listGroupsApiV1GroupsGet(@Query("limit") limit: kotlin.Int? = 50, @Query("offset") offset: kotlin.Int? = 0, @Query("q") q: kotlin.String? = null): Response<GroupListPage>

    /**
     * List Organizations
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @param limit  (optional, default to 50)
     * @param offset  (optional, default to 0)
     * @param q Case-insensitive search on legal name (optional)
     * @return [OrganizationListPage]
     */
    @GET("api/v1/organizations")
    suspend fun listOrganizationsApiV1OrganizationsGet(@Query("limit") limit: kotlin.Int? = 50, @Query("offset") offset: kotlin.Int? = 0, @Query("q") q: kotlin.String? = null): Response<OrganizationListPage>

    /**
     * List Users
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @param limit  (optional, default to 50)
     * @param offset  (optional, default to 0)
     * @param q  (optional)
     * @return [UserListPage]
     */
    @GET("api/v1/users")
    suspend fun listUsersApiV1UsersGet(@Query("limit") limit: kotlin.Int? = 50, @Query("offset") offset: kotlin.Int? = 0, @Query("q") q: kotlin.String? = null): Response<UserListPage>

    /**
     * Update User
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param userId 
     * @param userUpdateBody 
     * @return [UserResponse]
     */
    @PATCH("api/v1/users/{user_id}")
    suspend fun updateUserApiV1UsersUserIdPatch(@Path("user_id") userId: java.util.UUID, @Body userUpdateBody: UserUpdateBody): Response<UserResponse>

}
