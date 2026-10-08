# UsdcLeasePaymentCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountCents** | **Int** |  | 
**listingId** | **UUID** | Marketplace listing this payment buys. The server writes it to billing extra_metadata.listing_id, which marketplace purchase checks. A listing_id key in metadata is ignored. | [optional] 
**metadata** | **[String: String]** | Optional string map copied onto billing extra_metadata. Platform keys tenant_id and payment_rail win. lease_id and listing_id from a browser client are ignored. Do not send secrets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


