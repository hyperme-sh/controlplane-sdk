
# SubscriptionPlanDto

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **kotlin.String** |  |  |
| **planLevel** | **kotlin.collections.Map&lt;kotlin.String, kotlin.Int&gt;** | e.g., {&#39;basic&#39;: 0, &#39;pro&#39;: 1, &#39;enterprise&#39;: 2} |  |
| **isTrial** | **kotlin.Boolean** | Indicates if the subscription is a trial |  |
| **tenantId** | **kotlin.String** | The tenant who owns the subscription |  |
| **actor** | **kotlin.String** | who it is applied to, If end_user, then user_id must be set |  |
| **userId** | **kotlin.String** | The end user who has this subscription, if applicable |  |
| **planId** | **kotlin.String** | Corresponding Stripe Price ID |  |



