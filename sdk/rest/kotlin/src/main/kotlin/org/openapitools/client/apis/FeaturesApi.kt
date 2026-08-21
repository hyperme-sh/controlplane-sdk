package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.Feature

interface FeaturesApi {
    /**
     * List Features
     * List all available features. Requires HOST_MANAGE_TENANTS permission.
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.List<Feature>]
     */
    @GET("api/v1/features/")
    suspend fun listFeaturesApiV1FeaturesGet(): Response<kotlin.collections.List<Feature>>

}
