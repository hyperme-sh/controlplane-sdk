# SociACLShareLinkCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_kind** | [**SociACLResourceKind**](SociACLResourceKind.md) |  | 
**owner_user_id** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**resource_descriptor** | **Dict[str, object]** |  | [optional] 
**predicate** | [**SociACLPredicate**](SociACLPredicate.md) |  | 
**mode** | [**SociACLShareMode**](SociACLShareMode.md) |  | 
**expires_at** | **str** | ISO8601; omit for no expiry | [optional] 
**max_uses** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.soci_acl_share_link_create import SociACLShareLinkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SociACLShareLinkCreate from a JSON string
soci_acl_share_link_create_instance = SociACLShareLinkCreate.from_json(json)
# print the JSON string representation of the object
print(SociACLShareLinkCreate.to_json())

# convert the object into a dict
soci_acl_share_link_create_dict = soci_acl_share_link_create_instance.to_dict()
# create an instance of SociACLShareLinkCreate from a dict
soci_acl_share_link_create_from_dict = SociACLShareLinkCreate.from_dict(soci_acl_share_link_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


