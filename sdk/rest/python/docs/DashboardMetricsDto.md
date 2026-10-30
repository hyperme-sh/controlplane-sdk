# DashboardMetricsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** |  | 
**joined_users** | **int** |  | 
**total_users** | **int** |  | 
**timeseries** | [**List[TimeSeriesDto]**](TimeSeriesDto.md) |  | 

## Example

```python
from openapi_client.models.dashboard_metrics_dto import DashboardMetricsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardMetricsDto from a JSON string
dashboard_metrics_dto_instance = DashboardMetricsDto.from_json(json)
# print the JSON string representation of the object
print(DashboardMetricsDto.to_json())

# convert the object into a dict
dashboard_metrics_dto_dict = dashboard_metrics_dto_instance.to_dict()
# create an instance of DashboardMetricsDto from a dict
dashboard_metrics_dto_from_dict = DashboardMetricsDto.from_dict(dashboard_metrics_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


