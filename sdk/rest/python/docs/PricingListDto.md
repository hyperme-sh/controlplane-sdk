# PricingListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricings** | [**List[PricingDto]**](PricingDto.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from openapi_client.models.pricing_list_dto import PricingListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PricingListDto from a JSON string
pricing_list_dto_instance = PricingListDto.from_json(json)
# print the JSON string representation of the object
print(PricingListDto.to_json())

# convert the object into a dict
pricing_list_dto_dict = pricing_list_dto_instance.to_dict()
# create an instance of PricingListDto from a dict
pricing_list_dto_from_dict = PricingListDto.from_dict(pricing_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


