# CheckoutRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_id** | **str** |  | 
**tenant_id** | **str** |  | [optional] 
**mode** | **str** |  | [optional] [default to 'subscription']
**email** | **str** |  | 

## Example

```python
from openapi_client.models.checkout_request_dto import CheckoutRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutRequestDto from a JSON string
checkout_request_dto_instance = CheckoutRequestDto.from_json(json)
# print the JSON string representation of the object
print(CheckoutRequestDto.to_json())

# convert the object into a dict
checkout_request_dto_dict = checkout_request_dto_instance.to_dict()
# create an instance of CheckoutRequestDto from a dict
checkout_request_dto_from_dict = CheckoutRequestDto.from_dict(checkout_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


