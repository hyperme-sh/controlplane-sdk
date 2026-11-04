# RecoveryProofRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proof_type** | **str** |  | [optional] [default to 'split_key_stub']
**payload** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.recovery_proof_request import RecoveryProofRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveryProofRequest from a JSON string
recovery_proof_request_instance = RecoveryProofRequest.from_json(json)
# print the JSON string representation of the object
print(RecoveryProofRequest.to_json())

# convert the object into a dict
recovery_proof_request_dict = recovery_proof_request_instance.to_dict()
# create an instance of RecoveryProofRequest from a dict
recovery_proof_request_from_dict = RecoveryProofRequest.from_dict(recovery_proof_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


