# SubscriptionPlanDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | 
**planLevel** | **[String: Int]** | e.g., {&#39;basic&#39;: 0, &#39;pro&#39;: 1, &#39;enterprise&#39;: 2} | 
**isTrial** | **Bool** | Indicates if the subscription is a trial | 
**tenantId** | **String** | The tenant who owns the subscription | 
**actor** | **String** | who it is applied to, If end_user, then user_id must be set | 
**userId** | **String** | The end user who has this subscription, if applicable | 
**planId** | **String** | Corresponding Stripe Price ID | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


