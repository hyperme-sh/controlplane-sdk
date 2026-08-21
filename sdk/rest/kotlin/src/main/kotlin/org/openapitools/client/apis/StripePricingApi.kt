package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.CreatePricingDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.PricingListDto
import org.openapitools.client.models.UpdatePricingDto

interface StripePricingApi {
    /**
     * Create Pricing
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param createPricingDto 
     * @return [kotlin.Any]
     */
    @POST("api/v1/prices/")
    suspend fun createPricingApiV1PricesPost(@Body createPricingDto: CreatePricingDto): Response<kotlin.Any>

    /**
     * Get Pricing List
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [PricingListDto]
     */
    @GET("api/v1/prices/")
    suspend fun getPricingListApiV1PricesGet(): Response<PricingListDto>

    /**
     * Update Pricing
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param priceId 
     * @param updatePricingDto 
     * @return [Unit]
     */
    @PATCH("api/v1/prices/{price_id}")
    suspend fun updatePricingApiV1PricesPriceIdPatch(@Path("price_id") priceId: kotlin.String, @Body updatePricingDto: UpdatePricingDto): Response<Unit>

}
