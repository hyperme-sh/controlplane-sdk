# RegisteredPasskeyCredentialsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** |  | 
**public_key** | **str** |  | 
**sigin_count** | **int** |  | 
**transports** | [**List[AuthenticatorTransport]**](AuthenticatorTransport.md) |  | [optional] [default to []]
**created_at** | **datetime** |  | 
**last_used_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.registered_passkey_credentials_dto import RegisteredPasskeyCredentialsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredPasskeyCredentialsDto from a JSON string
registered_passkey_credentials_dto_instance = RegisteredPasskeyCredentialsDto.from_json(json)
# print the JSON string representation of the object
print(RegisteredPasskeyCredentialsDto.to_json())

# convert the object into a dict
registered_passkey_credentials_dto_dict = registered_passkey_credentials_dto_instance.to_dict()
# create an instance of RegisteredPasskeyCredentialsDto from a dict
registered_passkey_credentials_dto_from_dict = RegisteredPasskeyCredentialsDto.from_dict(registered_passkey_credentials_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


