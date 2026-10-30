# PolicyRuleCreate

One Casbin policy row: ptype + values mapped to v0..v5.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ptype** | **str** |  | 
**rule** | **List[str]** |  | 

## Example

```python
from openapi_client.models.policy_rule_create import PolicyRuleCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleCreate from a JSON string
policy_rule_create_instance = PolicyRuleCreate.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleCreate.to_json())

# convert the object into a dict
policy_rule_create_dict = policy_rule_create_instance.to_dict()
# create an instance of PolicyRuleCreate from a dict
policy_rule_create_from_dict = PolicyRuleCreate.from_dict(policy_rule_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


