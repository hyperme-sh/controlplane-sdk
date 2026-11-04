# UserUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**sociacl_attributes** | [**SociACLAttributes**](SociACLAttributes.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_update_body import UserUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateBody from a JSON string
user_update_body_instance = UserUpdateBody.from_json(json)
# print the JSON string representation of the object
print(UserUpdateBody.to_json())

# convert the object into a dict
user_update_body_dict = user_update_body_instance.to_dict()
# create an instance of UserUpdateBody from a dict
user_update_body_from_dict = UserUpdateBody.from_dict(user_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


