# SociACLPredicate

JSON-serializable rules stored on share links; evaluated server-side.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_verification_level** | **int** |  | [optional] 
**min_vouch_count** | **int** |  | [optional] 
**max_distance_km** | **float** |  | [optional] 
**required_political_tolerance** | [**PoliticalViewCategory**](PoliticalViewCategory.md) |  | [optional] 
**member_of_group_id** | **str** |  | [optional] 
**cross_network_handle_allowlist** | **List[str]** | If set, requester handle must match one entry (exact). | [optional] 
**cross_network_handle_blocklist** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.soci_acl_predicate import SociACLPredicate

# TODO update the JSON string below
json = "{}"
# create an instance of SociACLPredicate from a JSON string
soci_acl_predicate_instance = SociACLPredicate.from_json(json)
# print the JSON string representation of the object
print(SociACLPredicate.to_json())

# convert the object into a dict
soci_acl_predicate_dict = soci_acl_predicate_instance.to_dict()
# create an instance of SociACLPredicate from a dict
soci_acl_predicate_from_dict = SociACLPredicate.from_dict(soci_acl_predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


