
# CreatePlanDto

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **interval** | [**inline**](#Interval) |  |  |
| **productId** | **kotlin.String** | The product whose pricing the created plan will represent. This must be the ID of an existing product. |  |
| **amount** | **kotlin.Int** |  |  |
| **currency** | **kotlin.String** | Must be a supported currency: https://docs.stripe.com/currencies |  [optional] |


<a id="Interval"></a>
## Enum: interval
| Name | Value |
| ---- | ----- |
| interval | month, year |



