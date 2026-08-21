package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.CreateNotificationBannerSettingDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.NotificationBannerSettingDto

interface NotificationsApi {
    /**
     * Create Notification Banner
     * Create a new notification banner setting.
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param createNotificationBannerSettingDto 
     * @return [kotlin.Any]
     */
    @POST("api/v1/notifications/banner")
    suspend fun createNotificationBannerApiV1NotificationsBannerPost(@Body createNotificationBannerSettingDto: CreateNotificationBannerSettingDto): Response<kotlin.Any>

    /**
     * Get Notification Banner
     * Get the current notification banner information.
     * Responses:
     *  - 200: Successful Response
     *
     * @return [NotificationBannerSettingDto]
     */
    @GET("api/v1/notifications/banner")
    suspend fun getNotificationBannerApiV1NotificationsBannerGet(): Response<NotificationBannerSettingDto>

    /**
     * Update Notification Banner
     * Update an existing notification banner setting.
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param id 
     * @param createNotificationBannerSettingDto 
     * @return [Unit]
     */
    @PUT("api/v1/notifications/banner/{id}")
    suspend fun updateNotificationBannerApiV1NotificationsBannerIdPut(@Path("id") id: kotlin.String, @Body createNotificationBannerSettingDto: CreateNotificationBannerSettingDto): Response<Unit>

}
