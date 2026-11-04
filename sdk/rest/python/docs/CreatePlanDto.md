# CreatePlanDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Must be a supported currency: https://docs.stripe.com/currencies | [optional] [default to 'eur']
**interval** | **str** |  | 
**product_id** | **str** | The product whose pricing the created plan will represent. This must be the ID of an existing product. | 
**amount** | **int** |  | 

## Example

```python
from openapi_client.models.create_plan_dto import CreatePlanDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlanDto from a JSON string
create_plan_dto_instance = CreatePlanDto.from_json(json)
# print the JSON string representation of the object
print(CreatePlanDto.to_json())

# convert the object into a dict
create_plan_dto_dict = create_plan_dto_instance.to_dict()
# create an instance of CreatePlanDto from a dict
create_plan_dto_from_dict = CreatePlanDto.from_dict(create_plan_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


