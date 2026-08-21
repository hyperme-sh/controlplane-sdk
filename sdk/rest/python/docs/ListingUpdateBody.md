# ListingUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**is_public** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.listing_update_body import ListingUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListingUpdateBody from a JSON string
listing_update_body_instance = ListingUpdateBody.from_json(json)
# print the JSON string representation of the object
print(ListingUpdateBody.to_json())

# convert the object into a dict
listing_update_body_dict = listing_update_body_instance.to_dict()
# create an instance of ListingUpdateBody from a dict
listing_update_body_from_dict = ListingUpdateBody.from_dict(listing_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


