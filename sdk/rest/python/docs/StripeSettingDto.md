# StripeSettingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**default_currency** | **str** |  | 
**mode** | **str** |  | 
**trial_period_days** | **int** |  | 

## Example

```python
from openapi_client.models.stripe_setting_dto import StripeSettingDto

# TODO update the JSON string below
json = "{}"
# create an instance of StripeSettingDto from a JSON string
stripe_setting_dto_instance = StripeSettingDto.from_json(json)
# print the JSON string representation of the object
print(StripeSettingDto.to_json())

# convert the object into a dict
stripe_setting_dto_dict = stripe_setting_dto_instance.to_dict()
# create an instance of StripeSettingDto from a dict
stripe_setting_dto_from_dict = StripeSettingDto.from_dict(stripe_setting_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


