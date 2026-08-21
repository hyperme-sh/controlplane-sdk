# SociaclShareCreatedResponse

Returned once from POST /acl/sociacl/shares; includes raw token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_id** | **str** |  | 
**token** | **str** |  | 
**public** | [**SociACLShareLinkPublic**](SociACLShareLinkPublic.md) |  | 

## Example

```python
from openapi_client.models.sociacl_share_created_response import SociaclShareCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SociaclShareCreatedResponse from a JSON string
sociacl_share_created_response_instance = SociaclShareCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(SociaclShareCreatedResponse.to_json())

# convert the object into a dict
sociacl_share_created_response_dict = sociacl_share_created_response_instance.to_dict()
# create an instance of SociaclShareCreatedResponse from a dict
sociacl_share_created_response_from_dict = SociaclShareCreatedResponse.from_dict(sociacl_share_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


