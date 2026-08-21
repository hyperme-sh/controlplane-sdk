package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.BillingRecordListDto
import org.openapitools.client.models.CheckoutRequestDto
import org.openapitools.client.models.CheckoutResponseDto
import org.openapitools.client.models.HTTPValidationError

interface StripeCheckoutApi {
    /**
     * Create Host Checkout Session
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param checkoutRequestDto 
     * @return [CheckoutResponseDto]
     */
    @POST("api/v1/checkouts/host/{tenant_id}/tenant")
    suspend fun createHostCheckoutSessionApiV1CheckoutsHostTenantIdTenantPost(@Body checkoutRequestDto: CheckoutRequestDto): Response<CheckoutResponseDto>

    /**
     * Create Tenant Checkout Session
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param checkoutRequestDto 
     * @return [CheckoutResponseDto]
     */
    @POST("api/v1/checkouts/tenant/subscription")
    suspend fun createTenantCheckoutSessionApiV1CheckoutsTenantSubscriptionPost(@Body checkoutRequestDto: CheckoutRequestDto): Response<CheckoutResponseDto>

    /**
     * Host Checkout Success
     * 
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param tenantId 
     * @return [kotlin.Any]
     */
    @POST("api/v1/checkouts/host/payment/cancel")
    suspend fun hostCheckoutSuccessApiV1CheckoutsHostPaymentCancelPost(@Query("tenant_id") tenantId: kotlin.String): Response<kotlin.Any>

    /**
     * Host Checkout Success
     * 
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param sessionId 
     * @param tenantId 
     * @return [kotlin.Any]
     */
    @POST("api/v1/checkouts/host/payment/success")
    suspend fun hostCheckoutSuccessApiV1CheckoutsHostPaymentSuccessPost(@Query("session_id") sessionId: kotlin.String, @Query("tenant_id") tenantId: kotlin.String): Response<kotlin.Any>

    /**
     * List Checkout Records
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param skip  (optional, default to 0)
     * @param limit  (optional, default to 100)
     * @return [BillingRecordListDto]
     */
    @GET("api/v1/checkouts/all")
    suspend fun listCheckoutRecordsApiV1CheckoutsAllGet(@Query("skip") skip: kotlin.Int? = 0, @Query("limit") limit: kotlin.Int? = 100): Response<BillingRecordListDto>

    /**
     * Tenant Checkout Canceled
     * 
     * Responses:
     *  - 202: Successful Response
     *
     * @return [kotlin.Any]
     */
    @POST("api/v1/checkouts/tenant/payment/cancel")
    suspend fun tenantCheckoutCanceledApiV1CheckoutsTenantPaymentCancelPost(): Response<kotlin.Any>

    /**
     * Tenant Checkout Success
     * 
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param sessionId 
     * @return [kotlin.Any]
     */
    @POST("api/v1/checkouts/tenant/payment/success")
    suspend fun tenantCheckoutSuccessApiV1CheckoutsTenantPaymentSuccessPost(@Query("session_id") sessionId: kotlin.String): Response<kotlin.Any>

}
