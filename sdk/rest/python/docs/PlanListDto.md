# PlanListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plans** | [**List[PlanDto]**](PlanDto.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from openapi_client.models.plan_list_dto import PlanListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlanListDto from a JSON string
plan_list_dto_instance = PlanListDto.from_json(json)
# print the JSON string representation of the object
print(PlanListDto.to_json())

# convert the object into a dict
plan_list_dto_dict = plan_list_dto_instance.to_dict()
# create an instance of PlanListDto from a dict
plan_list_dto_from_dict = PlanListDto.from_dict(plan_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


