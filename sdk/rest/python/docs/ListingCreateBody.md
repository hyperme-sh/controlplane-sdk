# ListingCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] [default to '']
**listing_type** | **str** |  | 
**price_type** | **str** |  | 
**price_amount** | **int** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**is_public** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.listing_create_body import ListingCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListingCreateBody from a JSON string
listing_create_body_instance = ListingCreateBody.from_json(json)
# print the JSON string representation of the object
print(ListingCreateBody.to_json())

# convert the object into a dict
listing_create_body_dict = listing_create_body_instance.to_dict()
# create an instance of ListingCreateBody from a dict
listing_create_body_from_dict = ListingCreateBody.from_dict(listing_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


