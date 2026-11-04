package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.CreateRoleDto
import org.openapitools.client.models.CreateRoleResponseDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.RoleDto
import org.openapitools.client.models.RoleListDto
import org.openapitools.client.models.UpdateRoleDto

interface RolesApi {
    /**
     * Create Role
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param createRoleDto 
     * @return [CreateRoleResponseDto]
     */
    @POST("api/v1/roles/")
    suspend fun createRoleApiV1RolesPost(@Body createRoleDto: CreateRoleDto): Response<CreateRoleResponseDto>

    /**
     * Delete Role
     * Deletes a role if it is not assigned to any users.
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param roleId 
     * @return [kotlin.Any]
     */
    @DELETE("api/v1/roles/{role_id}")
    suspend fun deleteRoleApiV1RolesRoleIdDelete(@Path("role_id") roleId: kotlin.String): Response<kotlin.Any>

    /**
     * Get Role
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param roleId 
     * @return [RoleDto]
     */
    @GET("api/v1/roles/{role_id}")
    suspend fun getRoleApiV1RolesRoleIdGet(@Path("role_id") roleId: kotlin.String): Response<RoleDto>

    /**
     * List Roles
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param skip  (optional, default to 0)
     * @param limit  (optional, default to 10)
     * @return [RoleListDto]
     */
    @GET("api/v1/roles/")
    suspend fun listRolesApiV1RolesGet(@Query("skip") skip: kotlin.Int? = 0, @Query("limit") limit: kotlin.Int? = 10): Response<RoleListDto>

    /**
     * Search Role By Name
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param name 
     * @return [kotlin.collections.List<RoleDto>]
     */
    @GET("api/v1/roles/search_by_name")
    suspend fun searchRoleByNameApiV1RolesSearchByNameGet(@Query("name") name: kotlin.String): Response<kotlin.collections.List<RoleDto>>

    /**
     * Update Role
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param roleId 
     * @param updateRoleDto 
     * @return [RoleDto]
     */
    @PUT("api/v1/roles/{role_id}")
    suspend fun updateRoleApiV1RolesRoleIdPut(@Path("role_id") roleId: kotlin.String, @Body updateRoleDto: UpdateRoleDto): Response<RoleDto>

}
