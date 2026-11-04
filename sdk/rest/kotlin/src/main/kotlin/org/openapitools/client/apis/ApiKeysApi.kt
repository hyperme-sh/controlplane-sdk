package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.ApiKeyCreateRequest
import org.openapitools.client.models.ApiKeyCreatedResponse
import org.openapitools.client.models.ApiKeyResponse
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.InternalValidateRequest
import org.openapitools.client.models.InternalValidateResponse

interface ApiKeysApi {
    /**
     * Create Api Key
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param apiKeyCreateRequest 
     * @return [ApiKeyCreatedResponse]
     */
    @POST("api/v1/api-keys")
    suspend fun createApiKeyApiV1ApiKeysPost(@Body apiKeyCreateRequest: ApiKeyCreateRequest): Response<ApiKeyCreatedResponse>

    /**
     * Internal Validate
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param internalValidateRequest 
     * @param xInternalToken  (optional)
     * @return [InternalValidateResponse]
     */
    @POST("api/v1/internal/validate")
    suspend fun internalValidateApiV1InternalValidatePost(@Body internalValidateRequest: InternalValidateRequest, @Header("X-Internal-Token") xInternalToken: kotlin.String? = null): Response<InternalValidateResponse>

    /**
     * List Api Keys
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.List<ApiKeyResponse>]
     */
    @GET("api/v1/api-keys")
    suspend fun listApiKeysApiV1ApiKeysGet(): Response<kotlin.collections.List<ApiKeyResponse>>

    /**
     * Revoke Api Key
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param keyId 
     * @return [Unit]
     */
    @DELETE("api/v1/api-keys/{key_id}")
    suspend fun revokeApiKeyApiV1ApiKeysKeyIdDelete(@Path("key_id") keyId: java.util.UUID): Response<Unit>

}
