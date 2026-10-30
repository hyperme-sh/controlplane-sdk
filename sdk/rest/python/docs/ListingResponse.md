# ListingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**seller_id** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**listing_type** | **str** |  | 
**price_type** | **str** |  | 
**price_amount** | **int** |  | 
**metadata** | **Dict[str, object]** |  | 
**is_public** | **bool** |  | 

## Example

```python
from openapi_client.models.listing_response import ListingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListingResponse from a JSON string
listing_response_instance = ListingResponse.from_json(json)
# print the JSON string representation of the object
print(ListingResponse.to_json())

# convert the object into a dict
listing_response_dict = listing_response_instance.to_dict()
# create an instance of ListingResponse from a dict
listing_response_from_dict = ListingResponse.from_dict(listing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


