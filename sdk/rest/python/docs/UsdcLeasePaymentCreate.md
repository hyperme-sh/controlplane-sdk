# UsdcLeasePaymentCreate

POST /payments/usdc/lease-payments  Opens a pending USDC payment for one lease. The price clears 1:1 from USD cents into USDC atoms. No card is involved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** |  | 
**listing_id** | **str** | Marketplace listing this payment buys. The server writes it to billing extra_metadata.listing_id, which marketplace purchase checks. A listing_id key in metadata is ignored. | [optional] 
**metadata** | **Dict[str, str]** | Optional string map copied onto billing extra_metadata. Platform keys tenant_id and payment_rail win. lease_id and listing_id from a browser client are ignored. Do not send secrets. | [optional] 

## Example

```python
from openapi_client.models.usdc_lease_payment_create import UsdcLeasePaymentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UsdcLeasePaymentCreate from a JSON string
usdc_lease_payment_create_instance = UsdcLeasePaymentCreate.from_json(json)
# print the JSON string representation of the object
print(UsdcLeasePaymentCreate.to_json())

# convert the object into a dict
usdc_lease_payment_create_dict = usdc_lease_payment_create_instance.to_dict()
# create an instance of UsdcLeasePaymentCreate from a dict
usdc_lease_payment_create_from_dict = UsdcLeasePaymentCreate.from_dict(usdc_lease_payment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


