# GroupListPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GroupResponse]**](GroupResponse.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from openapi_client.models.group_list_page import GroupListPage

# TODO update the JSON string below
json = "{}"
# create an instance of GroupListPage from a JSON string
group_list_page_instance = GroupListPage.from_json(json)
# print the JSON string representation of the object
print(GroupListPage.to_json())

# convert the object into a dict
group_list_page_dict = group_list_page_instance.to_dict()
# create an instance of GroupListPage from a dict
group_list_page_from_dict = GroupListPage.from_dict(group_list_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


