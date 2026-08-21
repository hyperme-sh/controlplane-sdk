# CreatePricingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency code, e.g., &#39;usd&#39; | [optional] [default to 'eur']
**unit_amount** | **int** | A positive integer in cents (or 0 for a free price) representing how much to charge. One of unit_amount, unit_amount_decimal, or custom_unit_amount is required, unless billing_scheme&#x3D;tiered. | 
**product** | **str** | The ID of the product this price is associated with | 
**active** | **bool** | Whether the price is active or not | [optional] [default to True]
**recurring** | [**RecurringDto**](RecurringDto.md) |  | 

## Example

```python
from openapi_client.models.create_pricing_dto import CreatePricingDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePricingDto from a JSON string
create_pricing_dto_instance = CreatePricingDto.from_json(json)
# print the JSON string representation of the object
print(CreatePricingDto.to_json())

# convert the object into a dict
create_pricing_dto_dict = create_pricing_dto_instance.to_dict()
# create an instance of CreatePricingDto from a dict
create_pricing_dto_from_dict = CreatePricingDto.from_dict(create_pricing_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


