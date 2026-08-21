# UserCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**gender** | **str** |  | [optional] [default to 'unspecified']
**is_active** | **bool** |  | [optional] [default to True]

## Example

```python
from openapi_client.models.user_create_body import UserCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateBody from a JSON string
user_create_body_instance = UserCreateBody.from_json(json)
# print the JSON string representation of the object
print(UserCreateBody.to_json())

# convert the object into a dict
user_create_body_dict = user_create_body_instance.to_dict()
# create an instance of UserCreateBody from a dict
user_create_body_from_dict = UserCreateBody.from_dict(user_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


