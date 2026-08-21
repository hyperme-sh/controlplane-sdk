# BillingRecordListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_records** | [**List[BillingRecordDto]**](BillingRecordDto.md) |  | 
**skip** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**has_previous** | **bool** |  | 
**has_next** | **bool** |  | 

## Example

```python
from openapi_client.models.billing_record_list_dto import BillingRecordListDto

# TODO update the JSON string below
json = "{}"
# create an instance of BillingRecordListDto from a JSON string
billing_record_list_dto_instance = BillingRecordListDto.from_json(json)
# print the JSON string representation of the object
print(BillingRecordListDto.to_json())

# convert the object into a dict
billing_record_list_dto_dict = billing_record_list_dto_instance.to_dict()
# create an instance of BillingRecordListDto from a dict
billing_record_list_dto_from_dict = BillingRecordListDto.from_dict(billing_record_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


