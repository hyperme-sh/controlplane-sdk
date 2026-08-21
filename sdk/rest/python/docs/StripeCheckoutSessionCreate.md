# StripeCheckoutSessionCreate

POST /payments/stripe/checkout-sessions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] [default to 'payment']
**price_id** | **str** |  | 
**success_url** | **str** |  | 
**cancel_url** | **str** |  | 

## Example

```python
from openapi_client.models.stripe_checkout_session_create import StripeCheckoutSessionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCheckoutSessionCreate from a JSON string
stripe_checkout_session_create_instance = StripeCheckoutSessionCreate.from_json(json)
# print the JSON string representation of the object
print(StripeCheckoutSessionCreate.to_json())

# convert the object into a dict
stripe_checkout_session_create_dict = stripe_checkout_session_create_instance.to_dict()
# create an instance of StripeCheckoutSessionCreate from a dict
stripe_checkout_session_create_from_dict = StripeCheckoutSessionCreate.from_dict(stripe_checkout_session_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


