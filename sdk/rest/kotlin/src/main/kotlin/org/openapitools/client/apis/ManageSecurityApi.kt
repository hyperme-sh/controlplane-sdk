package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.RegisteredPasskeyCredentialsDto

interface ManageSecurityApi {
    /**
     * Delete Registered Passkey
     * Endpoint to delete a registered passkey for the current user.
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param credentialId 
     * @return [Unit]
     */
    @DELETE("api/v1/security/passkeys/{credential_id}")
    suspend fun deleteRegisteredPasskeyApiV1SecurityPasskeysCredentialIdDelete(@Path("credential_id") credentialId: kotlin.String): Response<Unit>

    /**
     * Get Registered Passkeys
     * Endpoint to retrieve registered passkeys for the current user.
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.List<RegisteredPasskeyCredentialsDto>]
     */
    @GET("api/v1/security/passkeys")
    suspend fun getRegisteredPasskeysApiV1SecurityPasskeysGet(): Response<kotlin.collections.List<RegisteredPasskeyCredentialsDto>>

}
