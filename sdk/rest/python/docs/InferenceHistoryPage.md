# InferenceHistoryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[InferenceRecordResponse]**](InferenceRecordResponse.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from openapi_client.models.inference_history_page import InferenceHistoryPage

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceHistoryPage from a JSON string
inference_history_page_instance = InferenceHistoryPage.from_json(json)
# print the JSON string representation of the object
print(InferenceHistoryPage.to_json())

# convert the object into a dict
inference_history_page_dict = inference_history_page_instance.to_dict()
# create an instance of InferenceHistoryPage from a dict
inference_history_page_from_dict = InferenceHistoryPage.from_dict(inference_history_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


