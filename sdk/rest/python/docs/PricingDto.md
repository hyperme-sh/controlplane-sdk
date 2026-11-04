# PricingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**currency** | **str** |  | 
**unit_amount** | **int** |  | 
**product** | **str** |  | 
**active** | **bool** |  | 
**recurring** | [**RecurringDto**](RecurringDto.md) |  | 
**tax_behavior** | **str** |  | 
**type** | **str** |  | 
**unit_amount_decimal** | **str** |  | 

## Example

```python
from openapi_client.models.pricing_dto import PricingDto

# TODO update the JSON string below
json = "{}"
# create an instance of PricingDto from a JSON string
pricing_dto_instance = PricingDto.from_json(json)
# print the JSON string representation of the object
print(PricingDto.to_json())

# convert the object into a dict
pricing_dto_dict = pricing_dto_instance.to_dict()
# create an instance of PricingDto from a dict
pricing_dto_from_dict = PricingDto.from_dict(pricing_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


