package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.AvailableStorageProviderDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.StorageSettingsDto

interface StorageSettingsApi {
    /**
     * Configure Storage
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param storageSettingsDto 
     * @return [kotlin.Any]
     */
    @POST("api/v1/storage/configure")
    suspend fun configureStorageApiV1StorageConfigurePost(@Body storageSettingsDto: StorageSettingsDto): Response<kotlin.Any>

    /**
     * Get Available Providers
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.List<kotlin.collections.Map<kotlin.String, kotlin.String>>]
     */
    @GET("api/v1/storage/available")
    suspend fun getAvailableProvidersApiV1StorageAvailableGet(): Response<kotlin.collections.List<kotlin.collections.Map<kotlin.String, kotlin.String>>>

    /**
     * Get Storage Settings
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.List<AvailableStorageProviderDto>]
     */
    @GET("api/v1/storage/")
    suspend fun getStorageSettingsApiV1StorageGet(): Response<kotlin.collections.List<AvailableStorageProviderDto>>

    /**
     * Reset Storage
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param storageId 
     * @return [Unit]
     */
    @PATCH("api/v1/storage/{storage_id}/reset")
    suspend fun resetStorageApiV1StorageStorageIdResetPatch(@Path("storage_id") storageId: kotlin.String): Response<Unit>

}
