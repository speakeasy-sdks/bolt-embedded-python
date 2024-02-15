# Account
(*account*)

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
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AddAddressRequest()

res = s.account.add_address(req, operations.AddAddressSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.AddAddressRequest](../../models/operations/addaddressrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.AddAddressSecurity](../../models/operations/addaddresssecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.AddAddressResponse](../../models/operations/addaddressresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_payment_method

Add a payment method to a shopper's Bolt account Wallet. For security purposes, this request must come from your backend because authentication requires the use of your private key.

**Note**: Before using this API, the credit card details must be tokenized using Bolt's JavaScript library function, which is documented in [Install the Bolt Tokenizer](https://help.bolt.com/developers/references/bolt-tokenizer).


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AddPaymentMethodRequest()

res = s.account.add_payment_method(req, operations.AddPaymentMethodSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.saved_credit_card_view is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.AddPaymentMethodRequest](../../models/operations/addpaymentmethodrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.AddPaymentMethodSecurity](../../models/operations/addpaymentmethodsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.AddPaymentMethodResponse](../../models/operations/addpaymentmethodresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_account

Create a Bolt shopping account.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.CreateAccountRequest()

res = s.account.create_account(req, operations.CreateAccountSecurity(
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.account_details is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateAccountRequest](../../models/operations/createaccountrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.CreateAccountSecurity](../../models/operations/createaccountsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.CreateAccountResponse](../../models/operations/createaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_address

Deletes an existing address in a shopper's address book.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.DeleteAddressRequest(
    id='<id>',
)

res = s.account.delete_address(req, operations.DeleteAddressSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteAddressRequest](../../models/operations/deleteaddressrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.DeleteAddressSecurity](../../models/operations/deleteaddresssecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.DeleteAddressResponse](../../models/operations/deleteaddressresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_payment_method

Delete a saved payment method from a shopper's Bolt account Wallet.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.DeletePaymentMethodRequest(
    payment_method_id='<value>',
)

res = s.account.delete_payment_method(req, operations.DeletePaymentMethodSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.DeletePaymentMethodRequest](../../models/operations/deletepaymentmethodrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.DeletePaymentMethodSecurity](../../models/operations/deletepaymentmethodsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.DeletePaymentMethodResponse](../../models/operations/deletepaymentmethodresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorsBoltAPIResponse | 403,404                      | application/json             |
| errors.SDKError              | 4x-5xx                       | */*                          |

## detect_account

Check whether an account exists using one of `email`, `phone`, or `sha256_email` as the unique identifier.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI(
    security=shared.Security(
        o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.DetectAccountRequest(
    x_publishable_key='<value>',
)

res = s.account.detect_account(req)

if res.v1_accounts_view is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DetectAccountRequest](../../models/operations/detectaccountrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DetectAccountResponse](../../models/operations/detectaccountresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorsBoltAPIResponse | 422                          | application/json             |
| errors.SDKError              | 4x-5xx                       | */*                          |

## edit_address

Edit an existing address in a shopper's address book.
This endpoint fully replaces the information for an existing address while retaining the same address ID.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.EditAddressRequest(
    id='<id>',
)

res = s.account.edit_address(req, operations.EditAddressSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.EditAddressRequest](../../models/operations/editaddressrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.EditAddressSecurity](../../models/operations/editaddresssecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.EditAddressResponse](../../models/operations/editaddressresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_account

Fetch a shopper's account details to pre-fill checkout fields. This request must come from your backend for security purposes, as it requires the use of your private key to authenticate. For PCI compliance, only limited information is returned for each credit card available in the shopper’s wallet.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.GetAccountRequest()

res = s.account.get_account(req, operations.GetAccountSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.account_details is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetAccountRequest](../../models/operations/getaccountrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GetAccountSecurity](../../models/operations/getaccountsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetAccountResponse](../../models/operations/getaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## replace_address

Replace an existing address in a shopper's address book.
These changes delete the existing address and create a new one.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.ReplaceAddressRequest(
    id='<id>',
)

res = s.account.replace_address(req, operations.ReplaceAddressSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ReplaceAddressRequest](../../models/operations/replaceaddressrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.ReplaceAddressSecurity](../../models/operations/replaceaddresssecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.ReplaceAddressResponse](../../models/operations/replaceaddressresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_account_profile

Update the identifiers for a shopper's profile (first name or last name).

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.UpdateAccountProfileRequest()

res = s.account.update_account_profile(req, operations.UpdateAccountProfileSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.profile_view is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAccountProfileRequest](../../models/operations/updateaccountprofilerequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.UpdateAccountProfileSecurity](../../models/operations/updateaccountprofilesecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.UpdateAccountProfileResponse](../../models/operations/updateaccountprofileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
