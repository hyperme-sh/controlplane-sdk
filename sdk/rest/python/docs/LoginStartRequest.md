# LoginStartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_provider_hint** | **str** | Keycloak broker alias (e.g. google, github, microsoft) passed as kc_idp_hint. | [optional] 

## Example

```python
from openapi_client.models.login_start_request import LoginStartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoginStartRequest from a JSON string
login_start_request_instance = LoginStartRequest.from_json(json)
# print the JSON string representation of the object
print(LoginStartRequest.to_json())

# convert the object into a dict
login_start_request_dict = login_start_request_instance.to_dict()
# create an instance of LoginStartRequest from a dict
login_start_request_from_dict = LoginStartRequest.from_dict(login_start_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


