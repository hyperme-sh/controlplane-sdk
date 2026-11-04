
# UsdcLeasePaymentCreate

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **amountCents** | **kotlin.Int** |  |  |
| **listingId** | [**java.util.UUID**](java.util.UUID.md) | Marketplace listing this payment buys. The server writes it to billing extra_metadata.listing_id, which marketplace purchase checks. A listing_id key in metadata is ignored. |  [optional] |
| **metadata** | **kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;** | Optional string map copied onto billing extra_metadata. Platform keys tenant_id and payment_rail win. lease_id and listing_id from a browser client are ignored. Do not send secrets. |  [optional] |



