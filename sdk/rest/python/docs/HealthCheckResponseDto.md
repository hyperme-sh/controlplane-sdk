# HealthCheckResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from openapi_client.models.health_check_response_dto import HealthCheckResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckResponseDto from a JSON string
health_check_response_dto_instance = HealthCheckResponseDto.from_json(json)
# print the JSON string representation of the object
print(HealthCheckResponseDto.to_json())

# convert the object into a dict
health_check_response_dto_dict = health_check_response_dto_instance.to_dict()
# create an instance of HealthCheckResponseDto from a dict
health_check_response_dto_from_dict = HealthCheckResponseDto.from_dict(health_check_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


