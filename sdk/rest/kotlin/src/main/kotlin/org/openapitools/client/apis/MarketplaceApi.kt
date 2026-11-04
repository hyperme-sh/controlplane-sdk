package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.ListingCreateBody
import org.openapitools.client.models.ListingResponse
import org.openapitools.client.models.ListingUpdateBody
import org.openapitools.client.models.PurchaseListingBody
import org.openapitools.client.models.PurchaseResponse

interface MarketplaceApi {
    /**
     * Create Listing
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param listingCreateBody 
     * @return [ListingResponse]
     */
    @POST("api/v1/marketplace/listings")
    suspend fun createListingApiV1MarketplaceListingsPost(@Body listingCreateBody: ListingCreateBody): Response<ListingResponse>

    /**
     * Delete Listing
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param listingId 
     * @return [Unit]
     */
    @DELETE("api/v1/marketplace/listings/{listing_id}")
    suspend fun deleteListingApiV1MarketplaceListingsListingIdDelete(@Path("listing_id") listingId: java.util.UUID): Response<Unit>

    /**
     * Get Listing
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param listingId 
     * @return [ListingResponse]
     */
    @GET("api/v1/marketplace/listings/{listing_id}")
    suspend fun getListingApiV1MarketplaceListingsListingIdGet(@Path("listing_id") listingId: java.util.UUID): Response<ListingResponse>

    /**
     * List Listings
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param publicOnly  (optional, default to false)
     * @return [kotlin.collections.List<ListingResponse>]
     */
    @GET("api/v1/marketplace/listings")
    suspend fun listListingsApiV1MarketplaceListingsGet(@Query("public_only") publicOnly: kotlin.Boolean? = false): Response<kotlin.collections.List<ListingResponse>>

    /**
     * Purchase Listing
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param listingId 
     * @param purchaseListingBody  (optional)
     * @return [PurchaseResponse]
     */
    @POST("api/v1/marketplace/listings/{listing_id}/purchase")
    suspend fun purchaseListingApiV1MarketplaceListingsListingIdPurchasePost(@Path("listing_id") listingId: java.util.UUID, @Body purchaseListingBody: PurchaseListingBody? = null): Response<PurchaseResponse>

    /**
     * Update Listing
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param listingId 
     * @param listingUpdateBody 
     * @return [ListingResponse]
     */
    @PATCH("api/v1/marketplace/listings/{listing_id}")
    suspend fun updateListingApiV1MarketplaceListingsListingIdPatch(@Path("listing_id") listingId: java.util.UUID, @Body listingUpdateBody: ListingUpdateBody): Response<ListingResponse>

}
