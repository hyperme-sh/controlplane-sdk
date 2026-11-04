package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.EnforceRequest
import org.openapitools.client.models.EnforceResponse
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.PolicyRowResponse
import org.openapitools.client.models.PolicyRuleCreate
import org.openapitools.client.models.PolicyRuleDelete

interface ACLApi {
    /**
     * Create Policy
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param policyRuleCreate 
     * @return [PolicyRowResponse]
     */
    @POST("api/v1/acl/policies")
    suspend fun createPolicyApiV1AclPoliciesPost(@Body policyRuleCreate: PolicyRuleCreate): Response<PolicyRowResponse>

    /**
     * Enforce Check
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param enforceRequest 
     * @return [EnforceResponse]
     */
    @POST("api/v1/acl/enforce")
    suspend fun enforceCheckApiV1AclEnforcePost(@Body enforceRequest: EnforceRequest): Response<EnforceResponse>

    /**
     * List Policies
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.List<PolicyRowResponse>]
     */
    @GET("api/v1/acl/policies")
    suspend fun listPoliciesApiV1AclPoliciesGet(): Response<kotlin.collections.List<PolicyRowResponse>>

    /**
     * Protected Ping
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.Any]
     */
    @GET("api/v1/acl/protected-ping")
    suspend fun protectedPingApiV1AclProtectedPingGet(): Response<kotlin.Any>

    /**
     * Remove Policy
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param policyRuleDelete 
     * @return [Unit]
     */
    @DELETE("api/v1/acl/policies")
    suspend fun removePolicyApiV1AclPoliciesDelete(@Body policyRuleDelete: PolicyRuleDelete): Response<Unit>

}
