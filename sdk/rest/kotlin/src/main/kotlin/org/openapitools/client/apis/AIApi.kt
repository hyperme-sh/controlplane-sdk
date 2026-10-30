package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.AIAskRequestDto
import org.openapitools.client.models.AIHistoriesDto
import org.openapitools.client.models.AIModelInfoDto
import org.openapitools.client.models.AISessionByUserIdDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.InferenceRequest
import org.openapitools.client.models.InferenceResponse
import org.openapitools.client.models.NewSessionResponseDto

interface AIApi {
    /**
     * Ask Ai
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param aiAskRequestDto 
     * @return [kotlin.Any]
     */
    @POST("api/v1/ai/ask")
    suspend fun askAiApiV1AiAskPost(@Body aiAskRequestDto: AIAskRequestDto): Response<kotlin.Any>

    /**
     * Complete
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param inferenceRequest 
     * @return [InferenceResponse]
     */
    @POST("api/v1/ai/complete")
    suspend fun completeApiV1AiCompletePost(@Body inferenceRequest: InferenceRequest): Response<InferenceResponse>

    /**
     * Create New Session
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [NewSessionResponseDto]
     */
    @GET("api/v1/ai/new_session")
    suspend fun createNewSessionApiV1AiNewSessionGet(): Response<NewSessionResponseDto>

    /**
     * Delete Session
     * 
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param sessionId 
     * @return [kotlin.Any]
     */
    @DELETE("api/v1/ai/sessions/{session_id}")
    suspend fun deleteSessionApiV1AiSessionsSessionIdDelete(@Path("session_id") sessionId: kotlin.String): Response<kotlin.Any>

    /**
     * Get History
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.List<AISessionByUserIdDto>]
     */
    @GET("api/v1/ai/history")
    suspend fun getHistoryApiV1AiHistoryGet(): Response<kotlin.collections.List<AISessionByUserIdDto>>

    /**
     * Get Models
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [kotlin.collections.List<AIModelInfoDto>]
     */
    @GET("api/v1/ai/models")
    suspend fun getModelsApiV1AiModelsGet(): Response<kotlin.collections.List<AIModelInfoDto>>

    /**
     * Get Single Session
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param sessionId 
     * @return [kotlin.collections.List<AIHistoriesDto>]
     */
    @GET("api/v1/ai/sessions/{session_id}")
    suspend fun getSingleSessionApiV1AiSessionsSessionIdGet(@Path("session_id") sessionId: kotlin.String): Response<kotlin.collections.List<AIHistoriesDto>>

    /**
     * Inference
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param inferenceRequest 
     * @return [InferenceResponse]
     */
    @POST("api/v1/ai/inference")
    suspend fun inferenceApiV1AiInferencePost(@Body inferenceRequest: InferenceRequest): Response<InferenceResponse>

    /**
     * Set Preferred Model
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param modelName 
     * @return [Unit]
     */
    @PUT("api/v1/ai/set_model_preference/{model_name}")
    suspend fun setPreferredModelApiV1AiSetModelPreferenceModelNamePut(@Path("model_name") modelName: kotlin.String): Response<Unit>

}
