# InferenceRecordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**user_id** | **str** |  | 
**model** | **str** |  | 
**input_tokens** | **int** |  | 
**output_tokens** | **int** |  | 
**cost_usd** | **str** |  | 
**billing_mode** | **str** |  | 
**budget_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.inference_record_response import InferenceRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceRecordResponse from a JSON string
inference_record_response_instance = InferenceRecordResponse.from_json(json)
# print the JSON string representation of the object
print(InferenceRecordResponse.to_json())

# convert the object into a dict
inference_record_response_dict = inference_record_response_instance.to_dict()
# create an instance of InferenceRecordResponse from a dict
inference_record_response_from_dict = InferenceRecordResponse.from_dict(inference_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


