package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.UpdateBrandingDto

interface BrandingApi {
    /**
     * Partial Update Branding
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param brandingId 
     * @param updateBrandingDto 
     * @return [Unit]
     */
    @PATCH("api/v1/brandings/{branding_id}")
    suspend fun partialUpdateBrandingApiV1BrandingsBrandingIdPatch(@Path("branding_id") brandingId: kotlin.String, @Body updateBrandingDto: UpdateBrandingDto): Response<Unit>

    /**
     * Update Branding
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param updateBrandingDto 
     * @return [Unit]
     */
    @POST("api/v1/brandings/")
    suspend fun updateBrandingApiV1BrandingsPost(@Body updateBrandingDto: UpdateBrandingDto): Response<Unit>

    /**
     * Upload Logo
     * 
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param file 
     * @return [kotlin.Any]
     */
    @Multipart
    @PUT("api/v1/brandings/logo")
    suspend fun uploadLogoApiV1BrandingsLogoPut(@Part("file") file: kotlin.String): Response<kotlin.Any>

}
