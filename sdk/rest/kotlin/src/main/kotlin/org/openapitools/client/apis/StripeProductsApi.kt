package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.CreateProductDto
import org.openapitools.client.models.HTTPValidationError
import org.openapitools.client.models.ProductDto
import org.openapitools.client.models.ProductListDto

interface StripeProductsApi {
    /**
     * Create a Product
     * 
     * Responses:
     *  - 201: Successful Response
     *  - 422: Validation Error
     *
     * @param createProductDto 
     * @return [kotlin.Any]
     */
    @POST("api/v1/products/")
    suspend fun createProductApiV1ProductsPost(@Body createProductDto: CreateProductDto): Response<kotlin.Any>

    /**
     * Delete a Product
     * 
     * Responses:
     *  - 202: Successful Response
     *  - 422: Validation Error
     *
     * @param productId 
     * @return [kotlin.Any]
     */
    @DELETE("api/v1/products/{product_id}")
    suspend fun deleteProductApiV1ProductsProductIdDelete(@Path("product_id") productId: kotlin.String): Response<kotlin.Any>

    /**
     * Get Product by ID
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param productId 
     * @return [ProductDto]
     */
    @GET("api/v1/products/{product_id}")
    suspend fun getProductByIdApiV1ProductsProductIdGet(@Path("product_id") productId: kotlin.String): Response<ProductDto>

    /**
     * List Products
     * 
     * Responses:
     *  - 200: Successful Response
     *  - 422: Validation Error
     *
     * @param active Filter active products, defaults to True (optional, default to true)
     * @return [ProductListDto]
     */
    @GET("api/v1/products/")
    suspend fun listProductsApiV1ProductsGet(@Query("active") active: kotlin.Boolean? = true): Response<ProductListDto>

    /**
     * Update a Product
     * 
     * Responses:
     *  - 204: Successful Response
     *  - 422: Validation Error
     *
     * @param productId 
     * @param createProductDto 
     * @return [Unit]
     */
    @PATCH("api/v1/products/{product_id}")
    suspend fun updateProductApiV1ProductsProductIdPatch(@Path("product_id") productId: kotlin.String, @Body createProductDto: CreateProductDto): Response<Unit>

}
