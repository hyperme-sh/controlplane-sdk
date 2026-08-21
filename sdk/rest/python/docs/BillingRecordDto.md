# BillingRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**actor** | **str** |  | 
**user_id** | **str** |  | [optional] 
**payment_type** | **str** |  | 
**currency** | **str** |  | 
**amount** | **int** |  | [optional] 
**stripe_customer_id** | **str** |  | [optional] 
**stripe_subscription_id** | **str** |  | [optional] 
**stripe_session_id** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**price_id** | **str** |  | [optional] 
**status** | **str** |  | 
**current_period_end** | **int** |  | [optional] 
**canceled_at** | **int** |  | [optional] 
**cancellation_reason** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.billing_record_dto import BillingRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of BillingRecordDto from a JSON string
billing_record_dto_instance = BillingRecordDto.from_json(json)
# print the JSON string representation of the object
print(BillingRecordDto.to_json())

# convert the object into a dict
billing_record_dto_dict = billing_record_dto_instance.to_dict()
# create an instance of BillingRecordDto from a dict
billing_record_dto_from_dict = BillingRecordDto.from_dict(billing_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


