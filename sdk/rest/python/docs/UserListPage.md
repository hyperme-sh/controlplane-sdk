# UserListPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UserResponse]**](UserResponse.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from openapi_client.models.user_list_page import UserListPage

# TODO update the JSON string below
json = "{}"
# create an instance of UserListPage from a JSON string
user_list_page_instance = UserListPage.from_json(json)
# print the JSON string representation of the object
print(UserListPage.to_json())

# convert the object into a dict
user_list_page_dict = user_list_page_instance.to_dict()
# create an instance of UserListPage from a dict
user_list_page_from_dict = UserListPage.from_dict(user_list_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


