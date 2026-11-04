package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.AuditLogListDto
import org.openapitools.client.models.DownloadAuditRequestDto
import org.openapitools.client.models.DownloadResponseDto
import org.openapitools.client.models.HTTPValidationError

interface AuditLogsApi {
    /**
     * Download Audit Logs
     * 
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param downloadAuditRequestDto 
     * @return [DownloadResponseDto]
     */
    @POST("api/v1/audit-logs/download")
    suspend fun downloadAuditLogsApiV1AuditLogsDownloadPost(@Body downloadAuditRequestDto: DownloadAuditRequestDto): Response<DownloadResponseDto>


    /**
    * enum for parameter action
    */
    enum class ActionListAuditLogsApiV1AuditLogsGet(val value: kotlin.String) {
        @JsonProperty(value = "create") create("create"),
        @JsonProperty(value = "update") update("update"),
        @JsonProperty(value = "delete") delete("delete"),
        @JsonProperty(value = "read") read("read"),
        @JsonProperty(value = "login") login("login"),
        @JsonProperty(value = "logout") logout("logout"),
        @JsonProperty(value = "error") error("error"),
        @JsonProperty(value = "download") download("download")
    }

    /**
     * List Audit Logs
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param limit  (optional, default to 10)
     * @param skip  (optional, default to 0)
     * @param action  (optional)
     * @return [AuditLogListDto]
     */
    @GET("api/v1/audit-logs/")
    suspend fun listAuditLogsApiV1AuditLogsGet(@Query("limit") limit: kotlin.Int? = 10, @Query("skip") skip: kotlin.Int? = 0, @Query("action") action: ActionListAuditLogsApiV1AuditLogsGet? = null): Response<AuditLogListDto>

}
