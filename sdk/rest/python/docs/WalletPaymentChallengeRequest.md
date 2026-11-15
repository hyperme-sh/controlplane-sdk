# WalletPaymentChallengeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**chain_id** | **int** |  | 

## Example

```python
from openapi_client.models.wallet_payment_challenge_request import WalletPaymentChallengeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPaymentChallengeRequest from a JSON string
wallet_payment_challenge_request_instance = WalletPaymentChallengeRequest.from_json(json)
# print the JSON string representation of the object
print(WalletPaymentChallengeRequest.to_json())

# convert the object into a dict
wallet_payment_challenge_request_dict = wallet_payment_challenge_request_instance.to_dict()
# create an instance of WalletPaymentChallengeRequest from a dict
wallet_payment_challenge_request_from_dict = WalletPaymentChallengeRequest.from_dict(wallet_payment_challenge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


