package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.WalletPaymentChallengeRequest
import org.openapitools.client.models.WalletPaymentHTTPValidationError
import org.openapitools.client.models.WalletPaymentPayoutChallenge
import org.openapitools.client.models.WalletPaymentRegisteredDestination
import org.openapitools.client.models.WalletPaymentSubmitRequest
import org.openapitools.client.models.WalletPaymentUsdcLeasePaymentCreate
import org.openapitools.client.models.WalletPaymentWalletCapabilities
import org.openapitools.client.models.WalletPaymentWalletCheckoutResponse
import org.openapitools.client.models.WalletPaymentWalletDepositStatus
import org.openapitools.client.models.WalletPaymentWalletLeasePaymentResponse

interface WalletPaymentsApi {
    /**
     * Challenge
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param xTenantID Must match the browser tenant session
     * @param walletPaymentChallengeRequest 
     * @return [WalletPaymentPayoutChallenge]
     */
    @POST("api/v1/payments/host-payout-address/challenge")
    suspend fun challengeApiV1PaymentsHostPayoutAddressChallengePost(@Header("X-Tenant-ID") xTenantID: java.util.UUID, @Body walletPaymentChallengeRequest: WalletPaymentChallengeRequest): Response<WalletPaymentPayoutChallenge>

    /**
     * Open Stablecoin Checkout
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param billingRecordId 
     * @param xTenantID 
     * @return [WalletPaymentWalletCheckoutResponse]
     */
    @POST("api/v1/payments/wallet/lease-payments/{billing_record_id}/checkout")
    suspend fun createWalletCheckout(@Path("billing_record_id") billingRecordId: java.util.UUID, @Header("X-Tenant-ID") xTenantID: java.util.UUID): Response<WalletPaymentWalletCheckoutResponse>

    /**
     * Create Deposit
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param billingRecordId 
     * @param xTenantID 
     * @return [WalletPaymentWalletDepositStatus]
     */
    @POST("api/v1/payments/wallet/lease-payments/{billing_record_id}/deposit")
    suspend fun createWalletDeposit(@Path("billing_record_id") billingRecordId: java.util.UUID, @Header("X-Tenant-ID") xTenantID: java.util.UUID): Response<WalletPaymentWalletDepositStatus>

    /**
     * Create Usdc Lease Payment Route
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param xTenantID 
     * @param walletPaymentUsdcLeasePaymentCreate 
     * @param idempotencyKey Reuse the same UUID when retrying the same payment request. (optional)
     * @return [WalletPaymentWalletLeasePaymentResponse]
     */
    @POST("api/v1/payments/wallet/lease-payments")
    suspend fun createWalletLeasePayment(@Header("X-Tenant-ID") xTenantID: java.util.UUID, @Body walletPaymentUsdcLeasePaymentCreate: WalletPaymentUsdcLeasePaymentCreate, @Header("Idempotency-Key") idempotencyKey: java.util.UUID? = null): Response<WalletPaymentWalletLeasePaymentResponse>

    /**
     * Deposit Status
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param billingRecordId 
     * @param xTenantID 
     * @return [WalletPaymentWalletDepositStatus]
     */
    @GET("api/v1/payments/wallet/lease-payments/{billing_record_id}/deposit")
    suspend fun getWalletDeposit(@Path("billing_record_id") billingRecordId: java.util.UUID, @Header("X-Tenant-ID") xTenantID: java.util.UUID): Response<WalletPaymentWalletDepositStatus>

    /**
     * Wallet Capabilities
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @param xTenantID 
     * @return [WalletPaymentWalletCapabilities]
     */
    @GET("api/v1/payments/wallet/capabilities")
    suspend fun getWalletPaymentCapabilities(@Header("X-Tenant-ID") xTenantID: java.util.UUID): Response<WalletPaymentWalletCapabilities>

    /**
     * Submit
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param xTenantID Must match the browser tenant session
     * @param walletPaymentSubmitRequest 
     * @return [WalletPaymentRegisteredDestination]
     */
    @POST("api/v1/payments/host-payout-address")
    suspend fun submitApiV1PaymentsHostPayoutAddressPost(@Header("X-Tenant-ID") xTenantID: java.util.UUID, @Body walletPaymentSubmitRequest: WalletPaymentSubmitRequest): Response<WalletPaymentRegisteredDestination>

}
