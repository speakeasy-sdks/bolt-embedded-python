# Payments
(*payments*)

## Overview

Create and manage transactions for non credit card payments such as Paypal in your Embedded Accounts experience.


### Available Operations

* [finalize_payment](#finalize_payment) - Finalize Payment
* [initialize_payment](#initialize_payment) - Initialize Payment
* [update_payment](#update_payment) - Update Payment

## finalize_payment

Finalize a Bolt Payment. NOTE: The authorization header is NOT required for payments associated with users who do not have a Bolt account.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.FinalizePaymentRequest(
    id='<id>',
)

res = s.payments.finalize_payment(req, operations.FinalizePaymentSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.FinalizePaymentRequest](../../models/operations/finalizepaymentrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.FinalizePaymentSecurity](../../models/operations/finalizepaymentsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.FinalizePaymentResponse](../../models/operations/finalizepaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## initialize_payment

Initialize a Bolt payment token that will be used to reference this payment to Bolt when it is updated or finalized. NOTE: The authorization header is NOT required for payments associated with users who do not have a Bolt account.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.InitializePaymentRequest()

res = s.payments.initialize_payment(req, operations.InitializePaymentSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
))

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.InitializePaymentRequest](../../models/operations/initializepaymentrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.InitializePaymentSecurity](../../models/operations/initializepaymentsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.InitializePaymentResponse](../../models/operations/initializepaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_payment

Update a Bolt payment using the token given after initializing a payment.  Updates will completely replace the original top-level resource (for example, if a cart is sent in with the request it will replace the existing cart).  Any included object should be sent as complete object. NOTE: The authorization header is NOT required for payments associated with users who do not have a Bolt account.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.UpdatePaymentRequest(
    id='<id>',
)

res = s.payments.update_payment(req, operations.UpdatePaymentSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
))

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdatePaymentRequest](../../models/operations/updatepaymentrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.UpdatePaymentSecurity](../../models/operations/updatepaymentsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.UpdatePaymentResponse](../../models/operations/updatepaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
