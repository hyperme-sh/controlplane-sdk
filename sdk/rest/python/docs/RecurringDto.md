# RecurringDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** | Billing interval, e.g., &#39;month&#39; | [optional] [default to 'month']
**interval_count** | **int** | Number of intervals between each billing cycle | [optional] [default to 1]
**usage_type** | **str** | Configures how the quantity per period should be determined. Can be either metered or licensed. licensed automatically bills the quantity set when adding it to a subscription. metered aggregates the total usage based on usage records. Defaults to licensed. | [optional] [default to 'licensed']

## Example

```python
from openapi_client.models.recurring_dto import RecurringDto

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringDto from a JSON string
recurring_dto_instance = RecurringDto.from_json(json)
# print the JSON string representation of the object
print(RecurringDto.to_json())

# convert the object into a dict
recurring_dto_dict = recurring_dto_instance.to_dict()
# create an instance of RecurringDto from a dict
recurring_dto_from_dict = RecurringDto.from_dict(recurring_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


