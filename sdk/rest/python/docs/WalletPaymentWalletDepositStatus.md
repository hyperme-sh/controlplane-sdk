# WalletPaymentWalletDepositStatus

USD-priced sandbox observation; never an enterprise balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** |  | 
**billing_record_id** | **str** |  | 
**chain_id** | **int** |  | [optional] [default to 84532]
**currency** | **str** |  | [optional] [default to 'usd']
**deposit_address** | **str** |  | 
**lease_id** | **str** |  | 
**network** | **str** |  | [optional] [default to 'base']
**payer_mismatch** | **Dict[str, object]** |  | [optional] 
**provider_status** | **str** |  | 
**settled** | **bool** |  | 
**status** | **str** |  | 
**token_contract_address** | **str** |  | [optional] [default to '0x036cbd53842c5426634e7929541ec2318f3dcf7e']
**token_currency** | **str** |  | [optional] [default to 'usdc']

## Example

```python
from openapi_client.models.wallet_payment_wallet_deposit_status import WalletPaymentWalletDepositStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPaymentWalletDepositStatus from a JSON string
wallet_payment_wallet_deposit_status_instance = WalletPaymentWalletDepositStatus.from_json(json)
# print the JSON string representation of the object
print(WalletPaymentWalletDepositStatus.to_json())

# convert the object into a dict
wallet_payment_wallet_deposit_status_dict = wallet_payment_wallet_deposit_status_instance.to_dict()
# create an instance of WalletPaymentWalletDepositStatus from a dict
wallet_payment_wallet_deposit_status_from_dict = WalletPaymentWalletDepositStatus.from_dict(wallet_payment_wallet_deposit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


