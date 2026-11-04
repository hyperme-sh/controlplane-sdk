package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.PermissionDto

interface PermissionsApi {
    /**
     * Get Permissions
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.List<PermissionDto>]
     */
    @GET("api/v1/permissions/")
    suspend fun getPermissionsApiV1PermissionsGet(): Response<kotlin.collections.List<PermissionDto>>

}
