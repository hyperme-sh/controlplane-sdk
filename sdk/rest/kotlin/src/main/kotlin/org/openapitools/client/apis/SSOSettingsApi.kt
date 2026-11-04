package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.CreateSSOSettingsDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.ReadSSOSettingsDto
import org.openapitools.client.models.SSOSettingsListDto
import org.openapitools.client.models.SSOSettingsResponseDto
import org.openapitools.client.models.UpdateSSOSettingsDto

interface SSOSettingsApi {
    /**
     * Create Sso Settings
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param createSSOSettingsDto 
     * @return [SSOSettingsResponseDto]
     */
    @POST("api/v1/ssos/")
    suspend fun createSsoSettingsApiV1SsosPost(@Body createSSOSettingsDto: CreateSSOSettingsDto): Response<SSOSettingsResponseDto>

    /**
     * Delete Sso Settings
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param ssoId 
     * @return [kotlin.Boolean]
     */
    @DELETE("api/v1/ssos/{sso_id}")
    suspend fun deleteSsoSettingsApiV1SsosSsoIdDelete(@Path("sso_id") ssoId: kotlin.String): Response<kotlin.Boolean>

    /**
     * Get Available Sso Providers
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.List<kotlin.Any>]
     */
    @GET("api/v1/ssos/available-providers")
    suspend fun getAvailableSsoProvidersApiV1SsosAvailableProvidersGet(): Response<kotlin.collections.List<kotlin.Any>>

    /**
     * Get Sso Settings By Id
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param ssoId 
     * @return [ReadSSOSettingsDto]
     */
    @GET("api/v1/ssos/{sso_id}")
    suspend fun getSsoSettingsByIdApiV1SsosSsoIdGet(@Path("sso_id") ssoId: kotlin.String): Response<ReadSSOSettingsDto>

    /**
     * List
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [SSOSettingsListDto]
     */
    @GET("api/v1/ssos/")
    suspend fun listApiV1SsosGet(): Response<SSOSettingsListDto>

    /**
     * Update Sso Settings
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param ssoId 
     * @param updateSSOSettingsDto 
     * @return [Unit]
     */
    @PATCH("api/v1/ssos/{sso_id}")
    suspend fun updateSsoSettingsApiV1SsosSsoIdPatch(@Path("sso_id") ssoId: kotlin.String, @Body updateSSOSettingsDto: UpdateSSOSettingsDto): Response<Unit>

}
