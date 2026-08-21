package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.CreatePlanDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.PlanDto
import org.openapitools.client.models.PlanListDto
import org.openapitools.client.models.UpdatePlanDto

interface StripeBillingApi {
    /**
     * Create a new plan
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param createPlanDto 
     * @return [kotlin.Any]
     */
    @POST("api/v1/billing/plans")
    suspend fun createPlanApiV1BillingPlansPost(@Body createPlanDto: CreatePlanDto): Response<kotlin.Any>

    /**
     * Delete existing plan
     * 
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param planId 
     * @return [kotlin.Any]
     */
    @DELETE("api/v1/billing/plans/{plan_id}")
    suspend fun deletePlanApiV1BillingPlansPlanIdDelete(@Path("plan_id") planId: kotlin.String): Response<kotlin.Any>

    /**
     * Retrieve a plan details
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param planId 
     * @return [PlanDto]
     */
    @GET("api/v1/billing/plans/{plan_id}")
    suspend fun getPlanApiV1BillingPlansPlanIdGet(@Path("plan_id") planId: kotlin.String): Response<PlanDto>

    /**
     * List available plans
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [PlanListDto]
     */
    @GET("api/v1/billing/plans")
    suspend fun listPlansApiV1BillingPlansGet(): Response<PlanListDto>

    /**
     * Update a existing plan
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param planId 
     * @param updatePlanDto 
     * @return [Unit]
     */
    @PATCH("api/v1/billing/plans/{plan_id}")
    suspend fun updatePlanApiV1BillingPlansPlanIdPatch(@Path("plan_id") planId: kotlin.String, @Body updatePlanDto: UpdatePlanDto): Response<Unit>

}
