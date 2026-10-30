# ThemeConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radius** | **str** | --radius | [optional] [default to '0.625rem']
**light** | [**ThemeColors**](ThemeColors.md) |  | [optional] 
**dark** | [**ThemeColors**](ThemeColors.md) |  | [optional] 

## Example

```python
from openapi_client.models.theme_config import ThemeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ThemeConfig from a JSON string
theme_config_instance = ThemeConfig.from_json(json)
# print the JSON string representation of the object
print(ThemeConfig.to_json())

# convert the object into a dict
theme_config_dict = theme_config_instance.to_dict()
# create an instance of ThemeConfig from a dict
theme_config_from_dict = ThemeConfig.from_dict(theme_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


