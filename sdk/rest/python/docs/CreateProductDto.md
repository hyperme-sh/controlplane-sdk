# CreateProductDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**tax_code** | **str** |  | [optional] 
**active** | **bool** |  | [optional] [default to True]

## Example

```python
from openapi_client.models.create_product_dto import CreateProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductDto from a JSON string
create_product_dto_instance = CreateProductDto.from_json(json)
# print the JSON string representation of the object
print(CreateProductDto.to_json())

# convert the object into a dict
create_product_dto_dict = create_product_dto_instance.to_dict()
# create an instance of CreateProductDto from a dict
create_product_dto_from_dict = CreateProductDto.from_dict(create_product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


