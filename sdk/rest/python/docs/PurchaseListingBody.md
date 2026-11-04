# PurchaseListingBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_listing_body import PurchaseListingBody

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseListingBody from a JSON string
purchase_listing_body_instance = PurchaseListingBody.from_json(json)
# print the JSON string representation of the object
print(PurchaseListingBody.to_json())

# convert the object into a dict
purchase_listing_body_dict = purchase_listing_body_instance.to_dict()
# create an instance of PurchaseListingBody from a dict
purchase_listing_body_from_dict = PurchaseListingBody.from_dict(purchase_listing_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


