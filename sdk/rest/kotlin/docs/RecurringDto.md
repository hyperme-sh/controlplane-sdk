
# RecurringDto

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **interval** | [**inline**](#Interval) | Billing interval, e.g., &#39;month&#39; |  [optional] |
| **intervalCount** | **kotlin.Int** | Number of intervals between each billing cycle |  [optional] |
| **usageType** | [**inline**](#UsageType) | Configures how the quantity per period should be determined. Can be either metered or licensed. licensed automatically bills the quantity set when adding it to a subscription. metered aggregates the total usage based on usage records. Defaults to licensed. |  [optional] |


<a id="Interval"></a>
## Enum: interval
| Name | Value |
| ---- | ----- |
| interval | day, week, month, year |


<a id="UsageType"></a>
## Enum: usage_type
| Name | Value |
| ---- | ----- |
| usageType | licensed, metered |



