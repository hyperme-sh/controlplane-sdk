# SociACLAttributes

Optional SociACL dimensions attached to a policy. Highly sensitive — minimize collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**political_view** | [**PoliticalViewCategory**](PoliticalViewCategory.md) |  | [optional] 
**sexual_orientation** | [**SexualOrientationCategory**](SexualOrientationCategory.md) |  | [optional] 
**verification_level** | **int** | 0&#x3D;none .. 4&#x3D;strong identity assurance | [optional] 
**notes** | **str** | Internal policy notes; avoid PII. | [optional] 

## Example

```python
from openapi_client.models.soci_acl_attributes import SociACLAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SociACLAttributes from a JSON string
soci_acl_attributes_instance = SociACLAttributes.from_json(json)
# print the JSON string representation of the object
print(SociACLAttributes.to_json())

# convert the object into a dict
soci_acl_attributes_dict = soci_acl_attributes_instance.to_dict()
# create an instance of SociACLAttributes from a dict
soci_acl_attributes_from_dict = SociACLAttributes.from_dict(soci_acl_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


