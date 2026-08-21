# ThemeColors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **str** | --background | [optional] [default to 'oklch(1 0 0)']
**foreground** | **str** | --foreground | [optional] [default to 'oklch(0.145 0 0)']
**card** | **str** | --card | [optional] [default to 'oklch(1 0 0)']
**card_foreground** | **str** | --card-foreground | [optional] [default to 'oklch(0.145 0 0)']
**popover** | **str** | --popover | [optional] [default to 'oklch(1 0 0)']
**popover_foreground** | **str** | --popover-foreground | [optional] [default to 'oklch(0.145 0 0)']
**primary** | **str** | --primary | [optional] [default to 'oklch(0.205 0 0)']
**primary_foreground** | **str** | --primary-foreground | [optional] [default to 'oklch(0.985 0 0)']
**secondary** | **str** | --secondary | [optional] [default to 'oklch(0.97 0 0)']
**secondary_foreground** | **str** | --secondary-foreground | [optional] [default to 'oklch(0.205 0 0)']
**muted** | **str** | --muted | [optional] [default to 'oklch(0.97 0 0)']
**muted_foreground** | **str** | --muted-foreground | [optional] [default to 'oklch(0.556 0 0)']
**accent** | **str** | --accent | [optional] [default to 'oklch(0.97 0 0)']
**accent_foreground** | **str** | --accent-foreground | [optional] [default to 'oklch(0.205 0 0)']
**destructive** | **str** | --destructive | [optional] [default to 'oklch(0.577 0.245 27.325)']
**destructive_foreground** | **str** | --destructive-foreground | [optional] [default to 'oklch(0.985 0 0)']
**border** | **str** | --border | [optional] [default to 'oklch(0.922 0 0)']
**input** | **str** | --input | [optional] [default to 'oklch(0.922 0 0)']
**ring** | **str** | --ring | [optional] [default to 'oklch(0.708 0 0)']
**chart_1** | **str** | --chart-1 | [optional] [default to 'oklch(0.646 0.222 41.116)']
**chart_2** | **str** | --chart-2 | [optional] [default to 'oklch(0.6 0.118 184.704)']
**chart_3** | **str** | --chart-3 | [optional] [default to 'oklch(0.398 0.07 227.392)']
**chart_4** | **str** | --chart-4 | [optional] [default to 'oklch(0.828 0.189 84.429)']
**chart_5** | **str** | --chart-5 | [optional] [default to 'oklch(0.769 0.188 70.08)']
**sidebar** | **str** | --sidebar | [optional] [default to 'oklch(0.985 0 0)']
**sidebar_foreground** | **str** | --sidebar-foreground | [optional] [default to 'oklch(0.145 0 0)']
**sidebar_primary** | **str** | --sidebar-primary | [optional] [default to 'oklch(0.205 0 0)']
**sidebar_primary_foreground** | **str** | --sidebar-primary-foreground | [optional] [default to 'oklch(0.985 0 0)']
**sidebar_accent** | **str** | --sidebar-accent | [optional] [default to 'oklch(0.97 0 0)']
**sidebar_accent_foreground** | **str** | --sidebar-accent-foreground | [optional] [default to 'oklch(0.205 0 0)']
**sidebar_border** | **str** | --sidebar-border | [optional] [default to 'oklch(0.922 0 0)']
**sidebar_ring** | **str** | --sidebar-ring | [optional] [default to 'oklch(0.708 0 0)']

## Example

```python
from openapi_client.models.theme_colors import ThemeColors

# TODO update the JSON string below
json = "{}"
# create an instance of ThemeColors from a JSON string
theme_colors_instance = ThemeColors.from_json(json)
# print the JSON string representation of the object
print(ThemeColors.to_json())

# convert the object into a dict
theme_colors_dict = theme_colors_instance.to_dict()
# create an instance of ThemeColors from a dict
theme_colors_from_dict = ThemeColors.from_dict(theme_colors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


