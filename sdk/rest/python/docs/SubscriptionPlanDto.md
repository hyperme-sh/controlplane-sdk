# SubscriptionPlanDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**plan_level** | **Dict[str, int]** | e.g., {&#39;basic&#39;: 0, &#39;pro&#39;: 1, &#39;enterprise&#39;: 2} | 
**is_trial** | **bool** | Indicates if the subscription is a trial | 
**tenant_id** | **str** | The tenant who owns the subscription | 
**actor** | **str** | who it is applied to, If end_user, then user_id must be set | 
**user_id** | **str** | The end user who has this subscription, if applicable | 
**plan_id** | **str** | Corresponding Stripe Price ID | 

## Example

```python
from openapi_client.models.subscription_plan_dto import SubscriptionPlanDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPlanDto from a JSON string
subscription_plan_dto_instance = SubscriptionPlanDto.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPlanDto.to_json())

# convert the object into a dict
subscription_plan_dto_dict = subscription_plan_dto_instance.to_dict()
# create an instance of SubscriptionPlanDto from a dict
subscription_plan_dto_from_dict = SubscriptionPlanDto.from_dict(subscription_plan_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


