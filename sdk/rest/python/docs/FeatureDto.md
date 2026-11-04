# FeatureDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Feature**](Feature.md) |  | 
**enabled** | **bool** |  | 

## Example

```python
from openapi_client.models.feature_dto import FeatureDto

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureDto from a JSON string
feature_dto_instance = FeatureDto.from_json(json)
# print the JSON string representation of the object
print(FeatureDto.to_json())

# convert the object into a dict
feature_dto_dict = feature_dto_instance.to_dict()
# create an instance of FeatureDto from a dict
feature_dto_from_dict = FeatureDto.from_dict(feature_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


