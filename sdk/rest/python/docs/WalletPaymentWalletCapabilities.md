# WalletPaymentWalletCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_effect** | **str** |  | [optional] [default to 'confirmed_capacity_only']
**checkout_creation** | **bool** |  | 
**contract_version** | **str** |  | [optional] [default to 'wallet-payments/v1']
**deposit_creation** | **bool** |  | 
**deposit_observation** | **bool** |  | [optional] [default to True]
**enterprise_units_redeemable** | **bool** |  | [optional] [default to False]
**mode** | **str** |  | [optional] [default to 'sandbox']
**payout_address_proof** | **bool** |  | 
**production_payments** | **bool** |  | [optional] [default to False]
**refund_recovery** | **str** |  | [optional] [default to 'owner_managed']
**settlement_authority** | **str** |  | [optional] [default to 'verified_provider_confirmation']
**usdc_host_enrollment** | **bool** |  | 

## Example

```python
from openapi_client.models.wallet_payment_wallet_capabilities import WalletPaymentWalletCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPaymentWalletCapabilities from a JSON string
wallet_payment_wallet_capabilities_instance = WalletPaymentWalletCapabilities.from_json(json)
# print the JSON string representation of the object
print(WalletPaymentWalletCapabilities.to_json())

# convert the object into a dict
wallet_payment_wallet_capabilities_dict = wallet_payment_wallet_capabilities_instance.to_dict()
# create an instance of WalletPaymentWalletCapabilities from a dict
wallet_payment_wallet_capabilities_from_dict = WalletPaymentWalletCapabilities.from_dict(wallet_payment_wallet_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


