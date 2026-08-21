package org.openapitools.client.apis

import org.openapitools.client.infrastructure.CollectionFormats.*
import retrofit2.http.*
import retrofit2.Response
import okhttp3.RequestBody
import com.fasterxml.jackson.annotation.JsonProperty

import org.openapitools.client.models.InvoiceListDto

interface StripeInvoicesApi {
    /**
     * List invoices
     * 
     * Responses:
     *  - 200: Successful Response
     *
     * @return [InvoiceListDto]
     */
    @GET("api/v1/invoices/")
    suspend fun listInvoicesApiV1InvoicesGet(): Response<InvoiceListDto>

}
