# CreateStripeSettingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_currency** | **str** |  | [optional] [default to 'eur']
**stripe_webhook_secret** | **str** |  | 
**mode** | **str** |  | [optional] [default to 'recurring']
**trial_period_days** | **int** |  | [optional] [default to 14]
**stripe_secret_key** | **str** |  | 
**tenant_id** | **str** |  | 

## Example

```python
from openapi_client.models.create_stripe_setting_dto import CreateStripeSettingDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeSettingDto from a JSON string
create_stripe_setting_dto_instance = CreateStripeSettingDto.from_json(json)
# print the JSON string representation of the object
print(CreateStripeSettingDto.to_json())

# convert the object into a dict
create_stripe_setting_dto_dict = create_stripe_setting_dto_instance.to_dict()
# create an instance of CreateStripeSettingDto from a dict
create_stripe_setting_dto_from_dict = CreateStripeSettingDto.from_dict(create_stripe_setting_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


