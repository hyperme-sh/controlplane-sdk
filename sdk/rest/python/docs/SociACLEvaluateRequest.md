# SociACLEvaluateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**context** | [**SociACLRequestContext**](SociACLRequestContext.md) |  | 
**owner_attributes** | [**SociACLAttributes**](SociACLAttributes.md) | MVP/tests: owner SociACL dimensions; production should load from user-service. | [optional] 

## Example

```python
from openapi_client.models.soci_acl_evaluate_request import SociACLEvaluateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SociACLEvaluateRequest from a JSON string
soci_acl_evaluate_request_instance = SociACLEvaluateRequest.from_json(json)
# print the JSON string representation of the object
print(SociACLEvaluateRequest.to_json())

# convert the object into a dict
soci_acl_evaluate_request_dict = soci_acl_evaluate_request_instance.to_dict()
# create an instance of SociACLEvaluateRequest from a dict
soci_acl_evaluate_request_from_dict = SociACLEvaluateRequest.from_dict(soci_acl_evaluate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


