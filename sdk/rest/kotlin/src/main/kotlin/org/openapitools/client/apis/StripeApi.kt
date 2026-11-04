package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.CreateStripeSettingDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.StripeSettingDto

interface StripeApi {
    /**
     * Configure Stripe Setting
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param createStripeSettingDto 
     * @return [kotlin.Any]
     */
    @POST("api/v1/configurations/stripe")
    suspend fun configureStripeSettingApiV1ConfigurationsStripePost(@Body createStripeSettingDto: CreateStripeSettingDto): Response<kotlin.Any>

    /**
     * Get Stripe Settings
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [StripeSettingDto]
     */
    @GET("api/v1/configurations/stripe")
    suspend fun getStripeSettingsApiV1ConfigurationsStripeGet(): Response<StripeSettingDto>

    /**
     * Stripe Webhook
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.Any]
     */
    @POST("api/v1/configurations/stripe/webhooks")
    suspend fun stripeWebhookApiV1ConfigurationsStripeWebhooksPost(): Response<kotlin.Any>

}
