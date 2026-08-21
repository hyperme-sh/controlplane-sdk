
# BillingRecordDto

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **scope** | [**inline**](#Scope) |  |  |
| **actor** | [**inline**](#Actor) |  |  |
| **paymentType** | **kotlin.String** |  |  |
| **currency** | **kotlin.String** |  |  |
| **status** | [**inline**](#Status) |  |  |
| **userId** | **kotlin.String** |  |  [optional] |
| **amount** | **kotlin.Int** |  |  [optional] |
| **stripeCustomerId** | **kotlin.String** |  |  [optional] |
| **stripeSubscriptionId** | **kotlin.String** |  |  [optional] |
| **stripeSessionId** | **kotlin.String** |  |  [optional] |
| **productId** | **kotlin.String** |  |  [optional] |
| **priceId** | **kotlin.String** |  |  [optional] |
| **currentPeriodEnd** | **kotlin.Int** |  |  [optional] |
| **canceledAt** | **kotlin.Int** |  |  [optional] |
| **cancellationReason** | **kotlin.String** |  |  [optional] |
| **metadata** | **kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;** |  |  [optional] |


<a id="Scope"></a>
## Enum: scope
| Name | Value |
| ---- | ----- |
| scope | host, tenant |


<a id="Actor"></a>
## Enum: actor
| Name | Value |
| ---- | ----- |
| actor | tenant, end_user |


<a id="Status"></a>
## Enum: status
| Name | Value |
| ---- | ----- |
| status | paid, pending, requires_payment_method, requires_action, active, succeeded, payment_failed, canceled, incomplete |



