# OrganizationCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** |  | 

## Example

```python
from openapi_client.models.organization_create_body import OrganizationCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCreateBody from a JSON string
organization_create_body_instance = OrganizationCreateBody.from_json(json)
# print the JSON string representation of the object
print(OrganizationCreateBody.to_json())

# convert the object into a dict
organization_create_body_dict = organization_create_body_instance.to_dict()
# create an instance of OrganizationCreateBody from a dict
organization_create_body_from_dict = OrganizationCreateBody.from_dict(organization_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


