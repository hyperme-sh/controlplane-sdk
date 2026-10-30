package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.ChangeEmailConfirmRequestDto
import org.openapitools.client.models.ChangeEmailRequestDto
import org.openapitools.client.models.ChangeEmailResponseDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.MeResponseDto

interface AccountApi {
    /**
     * Change Email
     * 
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param changeEmailRequestDto 
     * @return [kotlin.Any]
     */
    @PATCH("api/v1/account/change_email_request")
    suspend fun changeEmailApiV1AccountChangeEmailRequestPatch(@Body changeEmailRequestDto: ChangeEmailRequestDto): Response<kotlin.Any>

    /**
     * Change Email Confirmation
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param changeEmailConfirmRequestDto 
     * @return [ChangeEmailResponseDto]
     */
    @PATCH("api/v1/account/change_email_confirmation")
    suspend fun changeEmailConfirmationApiV1AccountChangeEmailConfirmationPatch(@Body changeEmailConfirmRequestDto: ChangeEmailConfirmRequestDto): Response<ChangeEmailResponseDto>

    /**
     * Logout
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.Any]
     */
    @GET("api/v1/account/logout")
    suspend fun logoutApiV1AccountLogoutGet(): Response<kotlin.Any>

    /**
     * Read Users Me
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [MeResponseDto]
     */
    @GET("api/v1/account/me")
    suspend fun readUsersMeApiV1AccountMeGet(): Response<MeResponseDto>

    /**
     * Resend Activation Email
     * Removed: activation is handled by Keycloak.
     * Responses:
     *  - 410: Successful Response
     *
     * @return [Unit]
     */
    @POST("api/v1/account/resend_activation_email")
    suspend fun resendActivationEmailApiV1AccountResendActivationEmailPost(): Response<Unit>

}
