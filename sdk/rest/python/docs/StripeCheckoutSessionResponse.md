# StripeCheckoutSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stripe_session_id** | **str** |  | 
**billing_record_id** | **str** |  | 
**checkout_url** | **str** | Stripe-hosted Checkout URL | [optional] 

## Example

```python
from openapi_client.models.stripe_checkout_session_response import StripeCheckoutSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCheckoutSessionResponse from a JSON string
stripe_checkout_session_response_instance = StripeCheckoutSessionResponse.from_json(json)
# print the JSON string representation of the object
print(StripeCheckoutSessionResponse.to_json())

# convert the object into a dict
stripe_checkout_session_response_dict = stripe_checkout_session_response_instance.to_dict()
# create an instance of StripeCheckoutSessionResponse from a dict
stripe_checkout_session_response_from_dict = StripeCheckoutSessionResponse.from_dict(stripe_checkout_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


