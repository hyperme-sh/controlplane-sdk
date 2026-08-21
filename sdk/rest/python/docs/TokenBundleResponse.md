# TokenBundleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**refresh_token** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**token_type** | **str** |  | [optional] [default to 'Bearer']

## Example

```python
from openapi_client.models.token_bundle_response import TokenBundleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenBundleResponse from a JSON string
token_bundle_response_instance = TokenBundleResponse.from_json(json)
# print the JSON string representation of the object
print(TokenBundleResponse.to_json())

# convert the object into a dict
token_bundle_response_dict = token_bundle_response_instance.to_dict()
# create an instance of TokenBundleResponse from a dict
token_bundle_response_from_dict = TokenBundleResponse.from_dict(token_bundle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


