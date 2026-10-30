# TenantUsageSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_cost_usd** | **str** |  | 
**total_input_tokens** | **int** |  | 
**total_output_tokens** | **int** |  | 

## Example

```python
from openapi_client.models.tenant_usage_summary_response import TenantUsageSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUsageSummaryResponse from a JSON string
tenant_usage_summary_response_instance = TenantUsageSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(TenantUsageSummaryResponse.to_json())

# convert the object into a dict
tenant_usage_summary_response_dict = tenant_usage_summary_response_instance.to_dict()
# create an instance of TenantUsageSummaryResponse from a dict
tenant_usage_summary_response_from_dict = TenantUsageSummaryResponse.from_dict(tenant_usage_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


