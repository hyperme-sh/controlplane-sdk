
# TenantDto

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **kotlin.String** |  |  |
| **id** | **kotlin.String** |  |  [optional] |
| **subdomain** | **kotlin.String** |  |  [optional] |
| **isActive** | **kotlin.Boolean** |  |  [optional] |
| **customDomain** | **kotlin.String** |  |  [optional] |
| **customDomainStatus** | [**inline**](#CustomDomainStatus) |  |  [optional] |
| **features** | [**kotlin.collections.List&lt;FeatureDto&gt;**](FeatureDto.md) |  |  [optional] |
| **subscriptionId** | **kotlin.String** |  |  [optional] |
| **createdAt** | **kotlin.String** |  |  [optional] |
| **updatedAt** | **kotlin.String** |  |  [optional] |


<a id="CustomDomainStatus"></a>
## Enum: custom_domain_status
| Name | Value |
| ---- | ----- |
| customDomainStatus | active, failed, activation-progress |



