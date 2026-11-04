# GroupCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**role_id** | **str** |  | 

## Example

```python
from openapi_client.models.group_create_body import GroupCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCreateBody from a JSON string
group_create_body_instance = GroupCreateBody.from_json(json)
# print the JSON string representation of the object
print(GroupCreateBody.to_json())

# convert the object into a dict
group_create_body_dict = group_create_body_instance.to_dict()
# create an instance of GroupCreateBody from a dict
group_create_body_from_dict = GroupCreateBody.from_dict(group_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


