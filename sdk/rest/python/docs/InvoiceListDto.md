# InvoiceListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoices** | [**List[InvoiceDto]**](InvoiceDto.md) |  | 
**has_more** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.invoice_list_dto import InvoiceListDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceListDto from a JSON string
invoice_list_dto_instance = InvoiceListDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceListDto.to_json())

# convert the object into a dict
invoice_list_dto_dict = invoice_list_dto_instance.to_dict()
# create an instance of InvoiceListDto from a dict
invoice_list_dto_from_dict = InvoiceListDto.from_dict(invoice_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


