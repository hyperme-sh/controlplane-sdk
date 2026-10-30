# CreateNotificationBannerSettingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_notification_banner_setting_dto import CreateNotificationBannerSettingDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationBannerSettingDto from a JSON string
create_notification_banner_setting_dto_instance = CreateNotificationBannerSettingDto.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationBannerSettingDto.to_json())

# convert the object into a dict
create_notification_banner_setting_dto_dict = create_notification_banner_setting_dto_instance.to_dict()
# create an instance of CreateNotificationBannerSettingDto from a dict
create_notification_banner_setting_dto_from_dict = CreateNotificationBannerSettingDto.from_dict(create_notification_banner_setting_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


