# InferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | 
**model** | **str** |  | 
**max_tokens** | **int** |  | [optional] 
**billing_mode** | **str** |  | [optional] [default to 'none']
**budget_id** | **str** | Crypto agent budget (payment-service); required when billing_mode is crypto. | [optional] 

## Example

```python
from openapi_client.models.inference_request import InferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceRequest from a JSON string
inference_request_instance = InferenceRequest.from_json(json)
# print the JSON string representation of the object
print(InferenceRequest.to_json())

# convert the object into a dict
inference_request_dict = inference_request_instance.to_dict()
# create an instance of InferenceRequest from a dict
inference_request_from_dict = InferenceRequest.from_dict(inference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


