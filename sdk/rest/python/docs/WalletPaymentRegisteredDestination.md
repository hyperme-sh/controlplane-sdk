# WalletPaymentRegisteredDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**chain_id** | **int** |  | 
**host_org_id** | **str** |  | 
**tenant_id** | **str** |  | 
**verified_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.wallet_payment_registered_destination import WalletPaymentRegisteredDestination

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPaymentRegisteredDestination from a JSON string
wallet_payment_registered_destination_instance = WalletPaymentRegisteredDestination.from_json(json)
# print the JSON string representation of the object
print(WalletPaymentRegisteredDestination.to_json())

# convert the object into a dict
wallet_payment_registered_destination_dict = wallet_payment_registered_destination_instance.to_dict()
# create an instance of WalletPaymentRegisteredDestination from a dict
wallet_payment_registered_destination_from_dict = WalletPaymentRegisteredDestination.from_dict(wallet_payment_registered_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


