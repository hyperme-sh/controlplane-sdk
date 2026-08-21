# CheckoutResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_url** | **str** |  | 

## Example

```python
from openapi_client.models.checkout_response_dto import CheckoutResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutResponseDto from a JSON string
checkout_response_dto_instance = CheckoutResponseDto.from_json(json)
# print the JSON string representation of the object
print(CheckoutResponseDto.to_json())

# convert the object into a dict
checkout_response_dto_dict = checkout_response_dto_instance.to_dict()
# create an instance of CheckoutResponseDto from a dict
checkout_response_dto_from_dict = CheckoutResponseDto.from_dict(checkout_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


