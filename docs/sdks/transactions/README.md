# Transactions
(*transactions*)

## Overview

Authorize credit card transactions and perform operations on those transactions with Bolt's transaction API.


### Available Operations

* [authorize_transaction](#authorize_transaction) - Authorize a Card
* [capture_transaction](#capture_transaction) - Capture a Transaction
* [get_transaction_details](#get_transaction_details) - Transaction Details
* [refund_transaction](#refund_transaction) - Refund a Transaction
* [update_transaction](#update_transaction) - Update a Transaction
* [void_transaction](#void_transaction) - Void a Transaction

## authorize_transaction

This endpoint authorizes card payments and has three main use cases:
* • Authorize a payment using an unsaved payment method for a guest or logged-in shopper.
* • Authorize a payment using a saved payment method for a logged-in shopper.
*  • Re-charge a previous transaction using the `credit_card_id` of the transaction.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AuthorizeTransactionRequest(
    idempotency_key='Handmade',
    request_body=[],
    x_publishable_key='green Northeast online',
)

res = s.transactions.authorize_transaction(req, operations.AuthorizeTransactionSecurity(
    o_auth="",
    x_api_key="",
))

if res.i_authorize_result_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.AuthorizeTransactionRequest](../../models/operations/authorizetransactionrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.AuthorizeTransactionSecurity](../../models/operations/authorizetransactionsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.AuthorizeTransactionResponse](../../models/operations/authorizetransactionresponse.md)**


## capture_transaction

This captures funds for the designated transaction. A capture can be done for any partial amount or for the total authorized amount.

Although the response returns the standard `transaction_view` object, only `captures` and either `id` or `reference` are needed.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.CaptureTransactionRequest(
    idempotency_key='Metal',
    capture_transaction_with_reference=shared.CaptureTransactionWithReference(
        amount=754,
        currency='USD',
        merchant_event_id='dbe0cd5d-3261-41d9-ba61-49e5b9d07567',
        skip_hook_notification=False,
        transaction_reference='LBLJ-TWW7-R9VC',
    ),
)

res = s.transactions.capture_transaction(req, operations.CaptureTransactionSecurity(
    x_api_key="",
))

if res.transaction_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CaptureTransactionRequest](../../models/operations/capturetransactionrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.CaptureTransactionSecurity](../../models/operations/capturetransactionsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.CaptureTransactionResponse](../../models/operations/capturetransactionresponse.md)**


## get_transaction_details

This allows you to pull the full transaction details for a given transaction.

 **Note**: All objects and fields marked `required` in the Transaction Details response are also **nullable**. This includes any sub-components (objects or fields) also marked `required`.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.GetTransactionDetailsRequest(
    reference='repurpose Holmium Trans',
)

res = s.transactions.get_transaction_details(req, operations.GetTransactionDetailsSecurity(
    x_api_key="",
))

if res.get_transaction_details_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetTransactionDetailsRequest](../../models/operations/gettransactiondetailsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetTransactionDetailsSecurity](../../models/operations/gettransactiondetailssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetTransactionDetailsResponse](../../models/operations/gettransactiondetailsresponse.md)**


## refund_transaction

This refunds a captured transaction. Refunds can be done for any partial amount or for the total authorized amount. These refunds are processed synchronously and return information about the refunded transaction in the standard `transaction_view` object.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.RefundTransactionRequest(
    idempotency_key='strategy Gasoline',
    request_body=operations.RefundTransactionRequestBody(
        amount=754,
        currency='USD',
        merchant_event_id='dbe0cd5d-3261-41d9-ba61-49e5b9d07567',
        skip_hook_notification=False,
        transaction_reference='LBLJ-TWW7-R9VC',
    ),
)

res = s.transactions.refund_transaction(req, operations.RefundTransactionSecurity(
    x_api_key="",
))

if res.transaction_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RefundTransactionRequest](../../models/operations/refundtransactionrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RefundTransactionSecurity](../../models/operations/refundtransactionsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RefundTransactionResponse](../../models/operations/refundtransactionresponse.md)**


## update_transaction

This allows you to update certain transaction properties post-authorization.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.UpdateTransactionRequest(
    idempotency_key='Paterson',
    reference='set Administrator Networked',
    request_body=operations.UpdateTransactionRequestBody(
        display_id='order-123',
        metadata={
            "rerum": 'circuit',
        },
    ),
)

res = s.transactions.update_transaction(req, operations.UpdateTransactionSecurity(
    x_api_key="",
))

if res.update_transaction_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateTransactionRequest](../../models/operations/updatetransactionrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateTransactionSecurity](../../models/operations/updatetransactionsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateTransactionResponse](../../models/operations/updatetransactionresponse.md)**


## void_transaction

This voids the authorization for a given transaction. Voids must be completed before the authorization is captured.
In the request, either `transaction_id` or `transaction_reference` is required.
Although the response returns the standard `transaction_view` object, only `status` and either `id` or `reference` are needed.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.VoidTransactionRequest(
    idempotency_key='Bicycle',
    credit_card_void=shared.CreditCardVoid(
        merchant_event_id='dbe0cd5d-3261-41d9-ba61-49e5b9d07567',
        skip_hook_notification=False,
        transaction_reference='LBLJ-TWW7-R9VC',
    ),
)

res = s.transactions.void_transaction(req, operations.VoidTransactionSecurity(
    x_api_key="",
))

if res.transaction_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.VoidTransactionRequest](../../models/operations/voidtransactionrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.VoidTransactionSecurity](../../models/operations/voidtransactionsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.VoidTransactionResponse](../../models/operations/voidtransactionresponse.md)**

