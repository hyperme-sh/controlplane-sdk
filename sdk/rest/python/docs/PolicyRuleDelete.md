# PolicyRuleDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ptype** | **str** |  | 
**rule** | **List[str]** |  | 

## Example

```python
from openapi_client.models.policy_rule_delete import PolicyRuleDelete

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleDelete from a JSON string
policy_rule_delete_instance = PolicyRuleDelete.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleDelete.to_json())

# convert the object into a dict
policy_rule_delete_dict = policy_rule_delete_instance.to_dict()
# create an instance of PolicyRuleDelete from a dict
policy_rule_delete_from_dict = PolicyRuleDelete.from_dict(policy_rule_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


