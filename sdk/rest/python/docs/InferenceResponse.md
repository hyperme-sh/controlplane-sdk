# InferenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**model** | **str** |  | 
**input_tokens** | **int** |  | 
**output_tokens** | **int** |  | 
**cost_usd** | **str** |  | 
**inference_id** | **str** |  | 

## Example

```python
from openapi_client.models.inference_response import InferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceResponse from a JSON string
inference_response_instance = InferenceResponse.from_json(json)
# print the JSON string representation of the object
print(InferenceResponse.to_json())

# convert the object into a dict
inference_response_dict = inference_response_instance.to_dict()
# create an instance of InferenceResponse from a dict
inference_response_from_dict = InferenceResponse.from_dict(inference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


