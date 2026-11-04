# MeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**gender** | [**Gender**](Gender.md) |  | 
**role_id** | **str** |  | [optional] 
**is_active** | **bool** |  | 
**activated_at** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**tenant_id** | **str** |  | [optional] 
**sso_provider_id** | **str** |  | [optional] 
**keycloak_sub** | **str** |  | [optional] 
**role** | [**RoleDto**](RoleDto.md) |  | [optional] 
**subscription** | [**SubscriptionPlanDto**](SubscriptionPlanDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.me_response_dto import MeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MeResponseDto from a JSON string
me_response_dto_instance = MeResponseDto.from_json(json)
# print the JSON string representation of the object
print(MeResponseDto.to_json())

# convert the object into a dict
me_response_dto_dict = me_response_dto_instance.to_dict()
# create an instance of MeResponseDto from a dict
me_response_dto_from_dict = MeResponseDto.from_dict(me_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


