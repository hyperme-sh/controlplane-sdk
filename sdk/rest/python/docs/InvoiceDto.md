# InvoiceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**account_country** | **str** |  | 
**account_name** | **str** |  | 
**amount_due** | **int** |  | [optional] [default to 0]
**amount_paid** | **int** |  | [optional] [default to 0]
**amount_remaining** | **int** |  | [optional] [default to 0]
**amount_overpaid** | **int** |  | [optional] [default to 0]
**attempt_count** | **int** |  | [optional] [default to 0]
**attempted** | **bool** |  | [optional] [default to False]
**auto_advance** | **bool** |  | [optional] [default to False]
**billing_reason** | **str** |  | 
**collection_method** | **str** |  | 
**created** | **int** |  | 
**currency** | **str** |  | 
**customer** | **str** |  | 
**customer_name** | **str** |  | 
**status** | **str** |  | 
**total** | **int** |  | 
**receipt_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_dto import InvoiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDto from a JSON string
invoice_dto_instance = InvoiceDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceDto.to_json())

# convert the object into a dict
invoice_dto_dict = invoice_dto_instance.to_dict()
# create an instance of InvoiceDto from a dict
invoice_dto_from_dict = InvoiceDto.from_dict(invoice_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


