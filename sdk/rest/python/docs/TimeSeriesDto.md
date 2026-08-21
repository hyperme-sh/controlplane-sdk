# TimeSeriesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_or_date** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from openapi_client.models.time_series_dto import TimeSeriesDto

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeriesDto from a JSON string
time_series_dto_instance = TimeSeriesDto.from_json(json)
# print the JSON string representation of the object
print(TimeSeriesDto.to_json())

# convert the object into a dict
time_series_dto_dict = time_series_dto_instance.to_dict()
# create an instance of TimeSeriesDto from a dict
time_series_dto_from_dict = TimeSeriesDto.from_dict(time_series_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


