# Account

## Overview

Create Embedded Accounts user flows for logged-in and guest experiences by interacting with and updating shopper data.


### Available Operations

* [add_address](#add_address) - Add Address
* [add_payment_method](#add_payment_method) - Add Payment Method
* [create_account](#create_account) - Create Bolt Account
* [delete_address](#delete_address) - Delete Address
* [delete_payment_method](#delete_payment_method) - Delete Payment Method
* [detect_account](#detect_account) - Detect Account
* [edit_address](#edit_address) - Edit Address
* [get_account](#get_account) - Get Account Details
* [replace_address](#replace_address) - Replace Address
* [update_account_profile](#update_account_profile) - Update Profile

## add_address

Add an address to a shopper's account address book.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AddAddressRequest(
    idempotency_key='quibusdam',
    x_publishable_key='unde',
    address_account=shared.AddressAccount(
        company='Bolt',
        country='United States',
        country_code='US',
        default=False,
        door_code='123456',
        email='alan.watts@example.com',
        first_name='Alan',
        last_name='Watts',
        locality='Brooklyn',
        metadata=shared.Metadata(
            additional_properties='nulla',
        ),
        name='Alan Watts',
        phone='+12125550199',
        postal_code='10044',
        region='NY',
        region_code='NY',
        street_address1='888 main street',
        street_address2='apt 3021',
        street_address3='c/o Alicia Watts',
        street_address4='Bridge Street Apartment Building B',
    ),
)

res = s.account.add_address(req, operations.AddAddressSecurity(
    o_auth="",
    x_api_key="",
))

if res.add_address_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.AddAddressRequest](../../models/operations/addaddressrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.AddAddressSecurity](../../models/operations/addaddresssecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.AddAddressResponse](../../models/operations/addaddressresponse.md)**


## add_payment_method

Add a payment method to a shopper's Bolt account Wallet. For security purposes, this request must come from your backend because authentication requires the use of your private key.

**Note**: Before using this API, the credit card details must be tokenized using Bolt's JavaScript library function, which is documented in [Install the Bolt Tokenizer](https://help.bolt.com/developers/references/bolt-tokenizer).


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AddPaymentMethodRequest(
    idempotency_key='corrupti',
    request_body=operations.AddPaymentMethodRequestBody(
        billing_address=shared.Address(
            company='Bolt',
            country='United States',
            country_code='US',
            default=True,
            door_code='123456',
            email='alan.watts@example.com',
            first_name='Alan',
            last_name='Watts',
            locality='Brooklyn',
            name='Alan Watts',
            phone='+12125550199',
            postal_code='10044',
            region='NY',
            region_code='NY',
            street_address1='888 main street',
            street_address2='apt 3021',
            street_address3='c/o Alicia Watts',
            street_address4='Bridge Street Apartment Building B',
        ),
        billing_address_id='null',
        bin='411111',
        cryptogram='illum',
        currency='USD',
        eci='vel',
        expiration='2025-11',
        last4='1234',
        metadata=shared.Metadata(
            additional_properties='error',
        ),
        network=operations.AddPaymentMethodRequestBodyNetwork.JCB,
        number='suscipit',
        postal_code='10044',
        priority=operations.AddPaymentMethodRequestBodyPriority.ONE,
        save=False,
        token='a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0',
        token_type=operations.AddPaymentMethodRequestBodyTokenType.BOLT,
    ),
    x_publishable_key='magnam',
)

res = s.account.add_payment_method(req, operations.AddPaymentMethodSecurity(
    o_auth="",
    x_api_key="",
))

if res.saved_credit_card_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.AddPaymentMethodRequest](../../models/operations/addpaymentmethodrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.AddPaymentMethodSecurity](../../models/operations/addpaymentmethodsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.AddPaymentMethodResponse](../../models/operations/addpaymentmethodresponse.md)**


## create_account

Create a Bolt shopping account.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.CreateAccountRequest(
    idempotency_key='debitis',
    x_publishable_key='ipsa',
    create_account_input=shared.CreateAccountInput(
        addresses=[
            shared.AddressAccount(
                company='Bolt',
                country='United States',
                country_code='US',
                default=False,
                door_code='123456',
                email='alan.watts@example.com',
                first_name='Alan',
                last_name='Watts',
                locality='Brooklyn',
                metadata=shared.Metadata(
                    additional_properties='delectus',
                ),
                name='Alan Watts',
                phone='+12125550199',
                postal_code='10044',
                region='NY',
                region_code='NY',
                street_address1='888 main street',
                street_address2='apt 3021',
                street_address3='c/o Alicia Watts',
                street_address4='Bridge Street Apartment Building B',
            ),
        ],
        payment_methods=[
            shared.PaymentMethodAccount(
                billing_address=shared.Address(
                    company='Bolt',
                    country='United States',
                    country_code='US',
                    default=True,
                    door_code='123456',
                    email='alan.watts@example.com',
                    first_name='Alan',
                    last_name='Watts',
                    locality='Brooklyn',
                    name='Alan Watts',
                    phone='+12125550199',
                    postal_code='10044',
                    region='NY',
                    region_code='NY',
                    street_address1='888 main street',
                    street_address2='apt 3021',
                    street_address3='c/o Alicia Watts',
                    street_address4='Bridge Street Apartment Building B',
                ),
                billing_address_id='null',
                bin='411111',
                cryptogram='tempora',
                default=False,
                eci='suscipit',
                expiration='2025-11',
                last4='1234',
                metadata=shared.Metadata(
                    additional_properties='molestiae',
                ),
                network=shared.PaymentMethodAccountNetwork.UNIONPAY,
                number='placeat',
                postal_code='10044',
                priority=shared.PaymentMethodAccountPriority.TWO,
                save=False,
                token='a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0',
                token_type=shared.PaymentMethodAccountTokenType.BOLT,
            ),
        ],
        profile=shared.Profile(
            email='alan.watts@example.com',
            first_name='Alan',
            last_name='Watts',
            metadata=shared.ProfileMetadata(
                additional_properties='iusto',
            ),
            phone='+12125550199',
        ),
    ),
)

res = s.account.create_account(req, operations.CreateAccountSecurity(
    x_api_key="",
))

if res.account_details is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateAccountRequest](../../models/operations/createaccountrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.CreateAccountSecurity](../../models/operations/createaccountsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.CreateAccountResponse](../../models/operations/createaccountresponse.md)**


## delete_address

Deletes an existing address in a shopper's address book.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.DeleteAddressRequest(
    x_publishable_key='excepturi',
    id='6ed151a0-5dfc-42dd-b7cc-78ca1ba928fc',
)

res = s.account.delete_address(req, operations.DeleteAddressSecurity(
    o_auth="",
    x_api_key="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteAddressRequest](../../models/operations/deleteaddressrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.DeleteAddressSecurity](../../models/operations/deleteaddresssecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.DeleteAddressResponse](../../models/operations/deleteaddressresponse.md)**


## delete_payment_method

Delete a saved payment method from a shopper's Bolt account Wallet.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.DeletePaymentMethodRequest(
    x_publishable_key='totam',
    payment_method_id='beatae',
)

res = s.account.delete_payment_method(req, operations.DeletePaymentMethodSecurity(
    o_auth="",
    x_api_key="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.DeletePaymentMethodRequest](../../models/operations/deletepaymentmethodrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.DeletePaymentMethodSecurity](../../models/operations/deletepaymentmethodsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.DeletePaymentMethodResponse](../../models/operations/deletepaymentmethodresponse.md)**


## detect_account

Check whether an account exists using one of `email`, `phone`, or `sha256_email` as the unique identifier.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI(
    security=shared.Security(
        o_auth="",
    ),
)

req = operations.DetectAccountRequest(
    x_publishable_key='commodi',
    email='Diego_Dibbert45@yahoo.com',
    phone='610.461.6263',
    sha256_email='hic',
)

res = s.account.detect_account(req)

if res.v1_accounts_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DetectAccountRequest](../../models/operations/detectaccountrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DetectAccountResponse](../../models/operations/detectaccountresponse.md)**


## edit_address

Edit an existing address in a shopper's address book.
This endpoint fully replaces the information for an existing address while retaining the same address ID.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.EditAddressRequest(
    x_publishable_key='saepe',
    address_account=shared.AddressAccount(
        company='Bolt',
        country='United States',
        country_code='US',
        default=False,
        door_code='123456',
        email='alan.watts@example.com',
        first_name='Alan',
        last_name='Watts',
        locality='Brooklyn',
        metadata=shared.Metadata(
            additional_properties='fuga',
        ),
        name='Alan Watts',
        phone='+12125550199',
        postal_code='10044',
        region='NY',
        region_code='NY',
        street_address1='888 main street',
        street_address2='apt 3021',
        street_address3='c/o Alicia Watts',
        street_address4='Bridge Street Apartment Building B',
    ),
    id='7596eb10-faaa-4235-ac59-55907aff1a3a',
)

res = s.account.edit_address(req, operations.EditAddressSecurity(
    o_auth="",
    x_api_key="",
))

if res.edit_address_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.EditAddressRequest](../../models/operations/editaddressrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.EditAddressSecurity](../../models/operations/editaddresssecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.EditAddressResponse](../../models/operations/editaddressresponse.md)**


## get_account

Fetch a shopper's account details to pre-fill checkout fields. This request must come from your backend for security purposes, as it requires the use of your private key to authenticate. For PCI compliance, only limited information is returned for each credit card available in the shopper’s wallet.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.GetAccountRequest(
    x_publishable_key='consequuntur',
)

res = s.account.get_account(req, operations.GetAccountSecurity(
    o_auth="",
    x_api_key="",
))

if res.account_details is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetAccountRequest](../../models/operations/getaccountrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GetAccountSecurity](../../models/operations/getaccountsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetAccountResponse](../../models/operations/getaccountresponse.md)**


## replace_address

Replace an existing address in a shopper's address book.
These changes delete the existing address and create a new one.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.ReplaceAddressRequest(
    idempotency_key='repellat',
    x_publishable_key='mollitia',
    address_account=shared.AddressAccount(
        company='Bolt',
        country='United States',
        country_code='US',
        default=False,
        door_code='123456',
        email='alan.watts@example.com',
        first_name='Alan',
        last_name='Watts',
        locality='Brooklyn',
        metadata=shared.Metadata(
            additional_properties='occaecati',
        ),
        name='Alan Watts',
        phone='+12125550199',
        postal_code='10044',
        region='NY',
        region_code='NY',
        street_address1='888 main street',
        street_address2='apt 3021',
        street_address3='c/o Alicia Watts',
        street_address4='Bridge Street Apartment Building B',
    ),
    id='46773925-1aa5-42c3-b5ad-019da1ffe78f',
)

res = s.account.replace_address(req, operations.ReplaceAddressSecurity(
    o_auth="",
    x_api_key="",
))

if res.replace_address_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ReplaceAddressRequest](../../models/operations/replaceaddressrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.ReplaceAddressSecurity](../../models/operations/replaceaddresssecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.ReplaceAddressResponse](../../models/operations/replaceaddressresponse.md)**


## update_account_profile

Update the identifiers for a shopper's profile (first name or last name).

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.UpdateAccountProfileRequest(
    request_body=operations.UpdateAccountProfileRequestBody(
        first_name='Alan',
        last_name='Watts',
        metadata=shared.Metadata(
            additional_properties='ipsa',
        ),
    ),
    x_publishable_key='omnis',
)

res = s.account.update_account_profile(req, operations.UpdateAccountProfileSecurity(
    o_auth="",
    x_api_key="",
))

if res.profile_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAccountProfileRequest](../../models/operations/updateaccountprofilerequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.UpdateAccountProfileSecurity](../../models/operations/updateaccountprofilesecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.UpdateAccountProfileResponse](../../models/operations/updateaccountprofileresponse.md)**

