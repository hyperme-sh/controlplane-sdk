# SociACLRequestContext

Requester-supplied context for evaluation (trust labels are advisory).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **str** |  | [optional] 
**political_view** | [**PoliticalViewCategory**](PoliticalViewCategory.md) |  | [optional] 
**verification_level** | **int** |  | [optional] 
**vouch_count** | **int** |  | [optional] 
**vouch_source** | **str** |  | [optional] 
**cross_network_handle** | **str** |  | [optional] 
**distance_km** | **float** |  | [optional] 
**distance_source** | [**SociACLDistanceSource**](SociACLDistanceSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.soci_acl_request_context import SociACLRequestContext

# TODO update the JSON string below
json = "{}"
# create an instance of SociACLRequestContext from a JSON string
soci_acl_request_context_instance = SociACLRequestContext.from_json(json)
# print the JSON string representation of the object
print(SociACLRequestContext.to_json())

# convert the object into a dict
soci_acl_request_context_dict = soci_acl_request_context_instance.to_dict()
# create an instance of SociACLRequestContext from a dict
soci_acl_request_context_from_dict = SociACLRequestContext.from_dict(soci_acl_request_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


