package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.WalletAuthHTTPValidationError
import org.openapitools.client.models.WalletAuthSiweBindRequest
import org.openapitools.client.models.WalletAuthSiweNonceRequest
import org.openapitools.client.models.WalletAuthSiweNonceResponse
import org.openapitools.client.models.WalletAuthWalletBindingResponse

interface WalletAuthApi {
    /**
     * Bind one SIWE wallet onto the identified Keycloak person
     * Verifies EIP-4361 and stores the recovered address only. Not a second login. Signature is not stored or returned.
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param walletAuthSiweBindRequest 
     * @return [WalletAuthWalletBindingResponse]
     */
    @POST("auth/siwe/bind")
    suspend fun authSiweBindAuthSiweBindPost(@Body walletAuthSiweBindRequest: WalletAuthSiweBindRequest): Response<WalletAuthWalletBindingResponse>

    /**
     * Wallet bound to the identified Keycloak person
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [WalletAuthWalletBindingResponse]
     */
    @GET("auth/siwe/me")
    suspend fun authSiweMeAuthSiweMeGet(): Response<WalletAuthWalletBindingResponse>

    /**
     * Issue an EIP-4361 nonce for the identified Keycloak person
     * Keycloak OIDC remains the login. This nonce is only for binding one wallet to that same person. Password grant stays off.
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param walletAuthSiweNonceRequest 
     * @return [WalletAuthSiweNonceResponse]
     */
    @POST("auth/siwe/nonce")
    suspend fun authSiweNonceAuthSiweNoncePost(@Body walletAuthSiweNonceRequest: WalletAuthSiweNonceRequest): Response<WalletAuthSiweNonceResponse>

}
