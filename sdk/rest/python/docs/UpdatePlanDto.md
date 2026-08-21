# UpdatePlanDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trial_period_days** | **int** |  | 
**active** | **bool** |  | [optional] [default to True]
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.update_plan_dto import UpdatePlanDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlanDto from a JSON string
update_plan_dto_instance = UpdatePlanDto.from_json(json)
# print the JSON string representation of the object
print(UpdatePlanDto.to_json())

# convert the object into a dict
update_plan_dto_dict = update_plan_dto_instance.to_dict()
# create an instance of UpdatePlanDto from a dict
update_plan_dto_from_dict = UpdatePlanDto.from_dict(update_plan_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


