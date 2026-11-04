
# CreatePricingDto

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **unitAmount** | **kotlin.Int** | A positive integer in cents (or 0 for a free price) representing how much to charge. One of unit_amount, unit_amount_decimal, or custom_unit_amount is required, unless billing_scheme&#x3D;tiered. |  |
| **product** | **kotlin.String** | The ID of the product this price is associated with |  |
| **recurring** | [**RecurringDto**](RecurringDto.md) |  |  |
| **currency** | **kotlin.String** | Currency code, e.g., &#39;usd&#39; |  [optional] |
| **active** | **kotlin.Boolean** | Whether the price is active or not |  [optional] |



