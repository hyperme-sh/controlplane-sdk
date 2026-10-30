# NotificationBannerSettingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** |  | 
**message** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.notification_banner_setting_dto import NotificationBannerSettingDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationBannerSettingDto from a JSON string
notification_banner_setting_dto_instance = NotificationBannerSettingDto.from_json(json)
# print the JSON string representation of the object
print(NotificationBannerSettingDto.to_json())

# convert the object into a dict
notification_banner_setting_dto_dict = notification_banner_setting_dto_instance.to_dict()
# create an instance of NotificationBannerSettingDto from a dict
notification_banner_setting_dto_from_dict = NotificationBannerSettingDto.from_dict(notification_banner_setting_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


