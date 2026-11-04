# IdentityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] [default to 'SaaS Org']

## Example

```python
from openapi_client.models.identity_dto import IdentityDto

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDto from a JSON string
identity_dto_instance = IdentityDto.from_json(json)
# print the JSON string representation of the object
print(IdentityDto.to_json())

# convert the object into a dict
identity_dto_dict = identity_dto_instance.to_dict()
# create an instance of IdentityDto from a dict
identity_dto_from_dict = IdentityDto.from_dict(identity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


