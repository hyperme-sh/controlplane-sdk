# RecurringDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **String** | Billing interval, e.g., &#39;month&#39; | [optional] [default to .month]
**intervalCount** | **Int** | Number of intervals between each billing cycle | [optional] [default to 1]
**usageType** | **String** | Configures how the quantity per period should be determined. Can be either metered or licensed. licensed automatically bills the quantity set when adding it to a subscription. metered aggregates the total usage based on usage records. Defaults to licensed. | [optional] [default to .licensed]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


