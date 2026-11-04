package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.DashboardMetricsDto
import org.openapitools.client.models.HTTPValidationError

interface DashboardApi {

    /**
    * enum for parameter filter
    */
    enum class FilterGetDashboardMetricsApiV1DashboardGet(val value: kotlin.String) {
        @JsonProperty(value = "today") today("today"),
        @JsonProperty(value = "this_week") this_week("this_week"),
        @JsonProperty(value = "last_3_months") last_3_months("last_3_months"),
        @JsonProperty(value = "all") all("all")
    }

    /**
     * Get Dashboard Metrics
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param filter  (optional, default to all)
     * @return [DashboardMetricsDto]
     */
    @GET("api/v1/dashboard/")
    suspend fun getDashboardMetricsApiV1DashboardGet(@Query("filter") filter: FilterGetDashboardMetricsApiV1DashboardGet? = FilterGetDashboardMetricsApiV1DashboardGet.all): Response<DashboardMetricsDto>

}
