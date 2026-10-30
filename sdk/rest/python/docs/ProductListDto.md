# ProductListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[ProductDto]**](ProductDto.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from openapi_client.models.product_list_dto import ProductListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListDto from a JSON string
product_list_dto_instance = ProductListDto.from_json(json)
# print the JSON string representation of the object
print(ProductListDto.to_json())

# convert the object into a dict
product_list_dto_dict = product_list_dto_instance.to_dict()
# create an instance of ProductListDto from a dict
product_list_dto_from_dict = ProductListDto.from_dict(product_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


