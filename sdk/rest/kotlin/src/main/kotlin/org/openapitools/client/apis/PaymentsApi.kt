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
import org.openapitools.client.models.StripeCheckoutSessionCreate
import org.openapitools.client.models.StripeCheckoutSessionResponse

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
     * Create Checkout Session
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param stripeCheckoutSessionCreate 
     * @return [StripeCheckoutSessionResponse]
     */
    @POST("api/v1/payments/stripe/checkout-sessions")
    suspend fun createCheckoutSessionApiV1PaymentsStripeCheckoutSessionsPost(@Body stripeCheckoutSessionCreate: StripeCheckoutSessionCreate): Response<StripeCheckoutSessionResponse>

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
