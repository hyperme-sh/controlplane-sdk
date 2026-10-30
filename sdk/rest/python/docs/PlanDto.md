# PlanDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**active** | **bool** |  | 
**amount** | **int** |  | 
**amount_decimal** | **str** |  | 
**billing_scheme** | **str** |  | 
**currency** | **str** |  | [optional] [default to 'eur']
**interval** | **str** |  | 
**interval_count** | **int** |  | 
**product** | **str** |  | 
**trial_period_days** | **int** |  | [optional] 
**usage_type** | **str** |  | 

## Example

```python
from openapi_client.models.plan_dto import PlanDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlanDto from a JSON string
plan_dto_instance = PlanDto.from_json(json)
# print the JSON string representation of the object
print(PlanDto.to_json())

# convert the object into a dict
plan_dto_dict = plan_dto_instance.to_dict()
# create an instance of PlanDto from a dict
plan_dto_from_dict = PlanDto.from_dict(plan_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


