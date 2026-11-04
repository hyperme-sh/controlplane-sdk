package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.RecoveryProofRequest
import org.openapitools.client.models.RecoverySessionCreate
import org.openapitools.client.models.RecoverySessionResponse
import org.openapitools.client.models.SociACLEvaluateRequest
import org.openapitools.client.models.SociACLShareLinkCreate
import org.openapitools.client.models.SociACLShareLinkPublic
import org.openapitools.client.models.SociaclShareCreatedResponse

interface SociACLApi {
    /**
     * Sociacl Create Share
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param sociACLShareLinkCreate 
     * @return [SociaclShareCreatedResponse]
     */
    @POST("api/v1/acl/sociacl/shares")
    suspend fun sociaclCreateShareApiV1AclSociaclSharesPost(@Body sociACLShareLinkCreate: SociACLShareLinkCreate): Response<SociaclShareCreatedResponse>

    /**
     * Sociacl Evaluate
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param sociACLEvaluateRequest 
     * @return [kotlin.Any]
     */
    @POST("api/v1/acl/sociacl/evaluate")
    suspend fun sociaclEvaluateApiV1AclSociaclEvaluatePost(@Body sociACLEvaluateRequest: SociACLEvaluateRequest): Response<kotlin.Any>

    /**
     * Sociacl Recovery Create
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param recoverySessionCreate 
     * @return [RecoverySessionResponse]
     */
    @POST("api/v1/acl/sociacl/recovery/sessions")
    suspend fun sociaclRecoveryCreateApiV1AclSociaclRecoverySessionsPost(@Body recoverySessionCreate: RecoverySessionCreate): Response<RecoverySessionResponse>

    /**
     * Sociacl Recovery Proof
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param sessionId 
     * @param recoveryProofRequest 
     * @return [kotlin.Any]
     */
    @POST("api/v1/acl/sociacl/recovery/sessions/{session_id}/proof")
    suspend fun sociaclRecoveryProofApiV1AclSociaclRecoverySessionsSessionIdProofPost(@Path("session_id") sessionId: java.util.UUID, @Body recoveryProofRequest: RecoveryProofRequest): Response<kotlin.Any>

    /**
     * Sociacl Resolve Share
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param token 
     * @return [SociACLShareLinkPublic]
     */
    @GET("api/v1/acl/sociacl/shares/by-token/{token}")
    suspend fun sociaclResolveShareApiV1AclSociaclSharesByTokenTokenGet(@Path("token") token: kotlin.String): Response<SociACLShareLinkPublic>

}
