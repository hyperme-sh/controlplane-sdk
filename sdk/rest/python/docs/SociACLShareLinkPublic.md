# SociACLShareLinkPublic

Non-sensitive resolve payload for anonymous callers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_id** | **str** |  | 
**mode** | [**SociACLShareMode**](SociACLShareMode.md) |  | 
**active** | **bool** |  | 
**resource_kind** | [**SociACLResourceKind**](SociACLResourceKind.md) |  | 
**expires_at** | **str** |  | [optional] 
**uses_remaining** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.soci_acl_share_link_public import SociACLShareLinkPublic

# TODO update the JSON string below
json = "{}"
# create an instance of SociACLShareLinkPublic from a JSON string
soci_acl_share_link_public_instance = SociACLShareLinkPublic.from_json(json)
# print the JSON string representation of the object
print(SociACLShareLinkPublic.to_json())

# convert the object into a dict
soci_acl_share_link_public_dict = soci_acl_share_link_public_instance.to_dict()
# create an instance of SociACLShareLinkPublic from a dict
soci_acl_share_link_public_from_dict = SociACLShareLinkPublic.from_dict(soci_acl_share_link_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


