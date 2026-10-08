package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.BudgetAllocateRequest
import org.openapitools.client.models.CryptoBudgetCreateRequest
import org.openapitools.client.models.CryptoBudgetListPage
import org.openapitools.client.models.CryptoBudgetResponse
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.UsdcLeasePaymentCreate
import org.openapitools.client.models.UsdcLeasePaymentResponse

interface PaymentsApi {
    /**
     * Allocate Budget
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param budgetId 
     * @param budgetAllocateRequest 
     * @return [CryptoBudgetResponse]
     */
    @POST("api/v1/budgets/{budget_id}/allocate")
    suspend fun allocateBudgetApiV1BudgetsBudgetIdAllocatePost(@Path("budget_id") budgetId: java.util.UUID, @Body budgetAllocateRequest: BudgetAllocateRequest): Response<CryptoBudgetResponse>

    /**
     * List crypto budgets
     * 
     * Responses:
     *  - 200: OK
     *
     * @param limit  (optional, default to 50)
     * @param offset  (optional, default to 0)
     * @return [CryptoBudgetListPage]
     */
    @GET("api/v1/budgets")
    suspend fun apiV1BudgetsGet(@Query("limit") limit: kotlin.Int? = 50, @Query("offset") offset: kotlin.Int? = 0): Response<CryptoBudgetListPage>

    /**
     * Create Crypto Budget
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param cryptoBudgetCreateRequest 
     * @return [CryptoBudgetResponse]
     */
    @POST("api/v1/budgets")
    suspend fun createCryptoBudgetApiV1BudgetsPost(@Body cryptoBudgetCreateRequest: CryptoBudgetCreateRequest): Response<CryptoBudgetResponse>

    /**
     * Open a USDC payment for a lease
     * Accepts a tenant-session JWT (human after switch-tenant) or a gateway exchange JWT from a purpose&#x3D;service key or a renter key minted via the org-admin API. Not a portal paste. Not a KV-stashed portal JWT. Raw Keycloak without tenant_id is 403. No card is charged. The renter pays the amount in USDC on Base.
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param usdcLeasePaymentCreate 
     * @return [UsdcLeasePaymentResponse]
     */
    @POST("api/v1/payments/usdc/lease-payments")
    suspend fun createUsdcLeasePaymentRouteApiV1PaymentsUsdcLeasePaymentsPost(@Body usdcLeasePaymentCreate: UsdcLeasePaymentCreate): Response<UsdcLeasePaymentResponse>

    /**
     * Get Crypto Budget
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param budgetId 
     * @return [CryptoBudgetResponse]
     */
    @GET("api/v1/budgets/{budget_id}")
    suspend fun getCryptoBudgetApiV1BudgetsBudgetIdGet(@Path("budget_id") budgetId: java.util.UUID): Response<CryptoBudgetResponse>

    /**
     * Settle a lease payment from the test-network credit
     * Available only where the deployment is Base Sepolia with Stripe in test mode. Marks the pending USDC payment succeeded and publishes payment.succeeded.v1, the same event a confirmed chain transfer publishes. Not available on Base mainnet.
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param billingRecordId 
     * @return [UsdcLeasePaymentResponse]
     */
    @POST("api/v1/payments/usdc/lease-payments/{billing_record_id}/test-credit")
    suspend fun settleUsdcTestCreditApiV1PaymentsUsdcLeasePaymentsBillingRecordIdTestCreditPost(@Path("billing_record_id") billingRecordId: java.util.UUID): Response<UsdcLeasePaymentResponse>

    /**
     * Stripe Webhook
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.Any]
     */
    @POST("api/v1/payments/stripe/webhook")
    suspend fun stripeWebhookApiV1PaymentsStripeWebhookPost(): Response<kotlin.Any>

}
