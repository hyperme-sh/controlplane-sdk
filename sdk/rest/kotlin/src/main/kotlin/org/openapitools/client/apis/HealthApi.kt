package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.HealthCheckResponseDto

interface HealthApi {
    /**
     * Health Check
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [HealthCheckResponseDto]
     */
    @GET("api/v1/health/")
    suspend fun healthCheckApiV1HealthGet(): Response<HealthCheckResponseDto>

}
