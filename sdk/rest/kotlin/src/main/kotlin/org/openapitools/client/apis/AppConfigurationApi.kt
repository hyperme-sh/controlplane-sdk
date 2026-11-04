package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.AppConfigurationDto

interface AppConfigurationApi {
    /**
     * Get App Configuration
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [AppConfigurationDto]
     */
    @GET("api/v1/app_configuration/")
    suspend fun getAppConfigurationApiV1AppConfigurationGet(): Response<AppConfigurationDto>

}
