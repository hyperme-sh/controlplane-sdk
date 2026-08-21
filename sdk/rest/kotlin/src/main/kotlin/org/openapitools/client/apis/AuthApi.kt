package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.AuthMeResponse
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.LoginStartRequest
import org.openapitools.client.models.LoginStartResponse
import org.openapitools.client.models.RefreshTokenRequest
import org.openapitools.client.models.TokenBundleResponse

interface AuthApi {
    /**
     * OAuth2 authorization code callback
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param code 
     * @param state  (optional)
     * @return [TokenBundleResponse]
     */
    @GET("auth/callback")
    suspend fun authCallbackAuthCallbackGet(@Query("code") code: kotlin.String, @Query("state") state: kotlin.String? = null): Response<TokenBundleResponse>

    /**
     * Start OIDC login
     * Returns Keycloak authorization URL; optional identity_provider_hint selects broker (Google, Entra, GitHub, …).
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param loginStartRequest  (optional)
     * @return [LoginStartResponse]
     */
    @POST("auth/login")
    suspend fun authLoginAuthLoginPost(@Body loginStartRequest: LoginStartRequest? = null): Response<LoginStartResponse>

    /**
     * Auth Me
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [AuthMeResponse]
     */
    @GET("auth/me")
    suspend fun authMeAuthMeGet(): Response<AuthMeResponse>

    /**
     * Refresh access token
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param refreshTokenRequest 
     * @return [TokenBundleResponse]
     */
    @POST("auth/refresh")
    suspend fun authRefreshAuthRefreshPost(@Body refreshTokenRequest: RefreshTokenRequest): Response<TokenBundleResponse>

    /**
     * Example route using get_current_tenant dependency
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.Map<kotlin.String, kotlin.Any>]
     */
    @GET("auth/tenant")
    suspend fun authTenantProbeAuthTenantGet(): Response<kotlin.collections.Map<kotlin.String, kotlin.Any>>

}
