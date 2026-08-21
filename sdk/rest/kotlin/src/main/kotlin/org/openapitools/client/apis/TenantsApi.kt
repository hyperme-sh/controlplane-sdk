package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.CreateTenantDto
import org.openapitools.client.models.CreateTenantResponseDto
import org.openapitools.client.models.FeatureDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.SubdomainAvailabilityDto
import org.openapitools.client.models.TenantDto
import org.openapitools.client.models.TenantListDto
import org.openapitools.client.models.UpdateTenantDto
import org.openapitools.client.models.UpdateTenantResponseDto

interface TenantsApi {
    /**
     * Activate Trial Plan
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param tenantId 
     * @return [UpdateTenantResponseDto]
     */
    @PATCH("api/v1/tenants/{tenant_id}/activate_trial_plan")
    suspend fun activateTrialPlanApiV1TenantsTenantIdActivateTrialPlanPatch(@Path("tenant_id") tenantId: kotlin.String): Response<UpdateTenantResponseDto>

    /**
     * Check Dns Status
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param tenantId 
     * @return [UpdateTenantResponseDto]
     */
    @GET("api/v1/tenants/{tenant_id}/check_dns")
    suspend fun checkDnsStatusApiV1TenantsTenantIdCheckDnsGet(@Path("tenant_id") tenantId: kotlin.String): Response<UpdateTenantResponseDto>

    /**
     * Check Subdomain Availability
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param subdomain 
     * @return [SubdomainAvailabilityDto]
     */
    @GET("api/v1/tenants/check_subdomain/{subdomain}")
    suspend fun checkSubdomainAvailabilityApiV1TenantsCheckSubdomainSubdomainGet(@Path("subdomain") subdomain: kotlin.String): Response<SubdomainAvailabilityDto>

    /**
     * Create Tenant
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param createTenantDto 
     * @return [CreateTenantResponseDto]
     */
    @POST("api/v1/tenants/")
    suspend fun createTenantApiV1TenantsPost(@Body createTenantDto: CreateTenantDto): Response<CreateTenantResponseDto>

    /**
     * Delete Tenant
     * 
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param id 
     * @return [kotlin.Any]
     */
    @DELETE("api/v1/tenants/{id}")
    suspend fun deleteTenantApiV1TenantsIdDelete(@Path("id") id: kotlin.String): Response<kotlin.Any>

    /**
     * Get Tenant Features
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param tenantId 
     * @return [kotlin.collections.List<FeatureDto>]
     */
    @GET("api/v1/tenants/{tenant_id}/features")
    suspend fun getTenantFeaturesApiV1TenantsTenantIdFeaturesGet(@Path("tenant_id") tenantId: kotlin.String): Response<kotlin.collections.List<FeatureDto>>

    /**
     * List Tenants
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param skip  (optional, default to 0)
     * @param limit  (optional, default to 10)
     * @return [TenantListDto]
     */
    @GET("api/v1/tenants/")
    suspend fun listTenantsApiV1TenantsGet(@Query("skip") skip: kotlin.Int? = 0, @Query("limit") limit: kotlin.Int? = 10): Response<TenantListDto>

    /**
     * Search By Name
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param name 
     * @return [TenantDto]
     */
    @GET("api/v1/tenants/search_by_name/{name}")
    suspend fun searchByNameApiV1TenantsSearchByNameNameGet(@Path("name") name: kotlin.String): Response<TenantDto>

    /**
     * Search By Subdomain
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param subdomain 
     * @return [TenantDto]
     */
    @GET("api/v1/tenants/search_by_subdomain/{subdomain}")
    suspend fun searchBySubdomainApiV1TenantsSearchBySubdomainSubdomainGet(@Path("subdomain") subdomain: kotlin.String): Response<TenantDto>

    /**
     * Update Tenant
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param tenantId 
     * @param updateTenantDto 
     * @return [Unit]
     */
    @PUT("api/v1/tenants/{tenant_id}")
    suspend fun updateTenantApiV1TenantsTenantIdPut(@Path("tenant_id") tenantId: kotlin.String, @Body updateTenantDto: UpdateTenantDto): Response<Unit>

    /**
     * Update Tenant Dns Record
     * When bringing your own domain you must map the DNS records for your custom domain to point to our main domain.                 You can do this by adding a CNAME record in your domain&#39;s DNS settings.                 Here is an example of how to set it up:                 Type: CNAME                 Name: app                 Value: fsrapp.com
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param tenantId 
     * @param updateTenantDto 
     * @return [UpdateTenantResponseDto]
     */
    @POST("api/v1/tenants/{tenant_id}/update_dns")
    suspend fun updateTenantDnsRecordApiV1TenantsTenantIdUpdateDnsPost(@Path("tenant_id") tenantId: kotlin.String, @Body updateTenantDto: UpdateTenantDto): Response<UpdateTenantResponseDto>

    /**
     * Update Tenant Feature
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param tenantId 
     * @param featureDto 
     * @return [UpdateTenantResponseDto]
     */
    @PATCH("api/v1/tenants/{tenant_id}/update_feature")
    suspend fun updateTenantFeatureApiV1TenantsTenantIdUpdateFeaturePatch(@Path("tenant_id") tenantId: kotlin.String, @Body featureDto: FeatureDto): Response<UpdateTenantResponseDto>

}
