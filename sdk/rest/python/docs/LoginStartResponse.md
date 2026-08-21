# LoginStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** |  | 
**state** | **str** | CSRF/state value; echo to /auth/callback. | 

## Example

```python
from openapi_client.models.login_start_response import LoginStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoginStartResponse from a JSON string
login_start_response_instance = LoginStartResponse.from_json(json)
# print the JSON string representation of the object
print(LoginStartResponse.to_json())

# convert the object into a dict
login_start_response_dict = login_start_response_instance.to_dict()
# create an instance of LoginStartResponse from a dict
login_start_response_from_dict = LoginStartResponse.from_dict(login_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


