# ProductDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**tax_code** | **str** |  | [optional] 
**active** | **bool** |  | 

## Example

```python
from openapi_client.models.product_dto import ProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDto from a JSON string
product_dto_instance = ProductDto.from_json(json)
# print the JSON string representation of the object
print(ProductDto.to_json())

# convert the object into a dict
product_dto_dict = product_dto_instance.to_dict()
# create an instance of ProductDto from a dict
product_dto_from_dict = ProductDto.from_dict(product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


