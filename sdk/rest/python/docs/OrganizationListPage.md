# OrganizationListPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OrganizationResponse]**](OrganizationResponse.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from openapi_client.models.organization_list_page import OrganizationListPage

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationListPage from a JSON string
organization_list_page_instance = OrganizationListPage.from_json(json)
# print the JSON string representation of the object
print(OrganizationListPage.to_json())

# convert the object into a dict
organization_list_page_dict = organization_list_page_instance.to_dict()
# create an instance of OrganizationListPage from a dict
organization_list_page_from_dict = OrganizationListPage.from_dict(organization_list_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


