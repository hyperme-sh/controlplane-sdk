# WalletPaymentPayoutChallenge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**chain_id** | **int** |  | 
**message** | **str** |  | 
**nonce** | **str** |  | 

## Example

```python
from openapi_client.models.wallet_payment_payout_challenge import WalletPaymentPayoutChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPaymentPayoutChallenge from a JSON string
wallet_payment_payout_challenge_instance = WalletPaymentPayoutChallenge.from_json(json)
# print the JSON string representation of the object
print(WalletPaymentPayoutChallenge.to_json())

# convert the object into a dict
wallet_payment_payout_challenge_dict = wallet_payment_payout_challenge_instance.to_dict()
# create an instance of WalletPaymentPayoutChallenge from a dict
wallet_payment_payout_challenge_from_dict = WalletPaymentPayoutChallenge.from_dict(wallet_payment_payout_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


