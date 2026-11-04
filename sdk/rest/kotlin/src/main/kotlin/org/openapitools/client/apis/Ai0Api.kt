package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.InferenceHistoryPage
import org.openapitools.client.models.TenantUsageSummaryResponse

interface AiApi {
    /**
     * List inference usage history
     * 
     * Responses:
     *  - 200: OK
     *
     * @param limit  (optional, default to 50)
     * @param offset  (optional, default to 0)
     * @param userId  (optional)
     * @return [InferenceHistoryPage]
     */
    @GET("api/v1/ai/usage/history")
    suspend fun apiV1AiUsageHistoryGet(@Query("limit") limit: kotlin.Int? = 50, @Query("offset") offset: kotlin.Int? = 0, @Query("user_id") userId: java.util.UUID? = null): Response<InferenceHistoryPage>

    /**
     * Tenant usage summary
     * 
     * Responses:
     *  - 200: OK
     *
     * @return [TenantUsageSummaryResponse]
     */
    @GET("api/v1/ai/usage/summary")
    suspend fun apiV1AiUsageSummaryGet(): Response<TenantUsageSummaryResponse>

}
