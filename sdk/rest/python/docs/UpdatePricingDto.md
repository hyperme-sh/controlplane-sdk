# UpdatePricingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**tax_behavior** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_pricing_dto import UpdatePricingDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePricingDto from a JSON string
update_pricing_dto_instance = UpdatePricingDto.from_json(json)
# print the JSON string representation of the object
print(UpdatePricingDto.to_json())

# convert the object into a dict
update_pricing_dto_dict = update_pricing_dto_instance.to_dict()
# create an instance of UpdatePricingDto from a dict
update_pricing_dto_from_dict = UpdatePricingDto.from_dict(update_pricing_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


