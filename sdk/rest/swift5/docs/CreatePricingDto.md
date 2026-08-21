# CreatePricingDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **String** | Currency code, e.g., &#39;usd&#39; | [optional] [default to "eur"]
**unitAmount** | **Int** | A positive integer in cents (or 0 for a free price) representing how much to charge. One of unit_amount, unit_amount_decimal, or custom_unit_amount is required, unless billing_scheme&#x3D;tiered. | 
**product** | **String** | The ID of the product this price is associated with | 
**active** | **Bool** | Whether the price is active or not | [optional] [default to true]
**recurring** | [**RecurringDto**](RecurringDto.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


