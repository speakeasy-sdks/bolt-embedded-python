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
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AuthorizeTransactionRequest()

res = s.transactions.authorize_transaction(req, operations.AuthorizeTransactionSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.i_authorize_result_view is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.AuthorizeTransactionRequest](../../models/operations/authorizetransactionrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.AuthorizeTransactionSecurity](../../models/operations/authorizetransactionsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.AuthorizeTransactionResponse](../../models/operations/authorizetransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## capture_transaction

This captures funds for the designated transaction. A capture can be done for any partial amount or for the total authorized amount.

Although the response returns the standard `transaction_view` object, only `captures` and either `id` or `reference` are needed.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI(
    security=shared.Security(
        o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CaptureTransactionRequest()

res = s.transactions.capture_transaction(req)

if res.transaction_view is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CaptureTransactionRequest](../../models/operations/capturetransactionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CaptureTransactionResponse](../../models/operations/capturetransactionresponse.md)**
### Errors

| Error Object                          | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.ErrorsBoltAPIResponse          | 403,404                               | application/json                      |
| errors.CaptureTransactionResponseBody | 422                                   | application/json                      |
| errors.SDKError                       | 4x-5xx                                | */*                                   |

## get_transaction_details

This allows you to pull the full transaction details for a given transaction.

 **Note**: All objects and fields marked `required` in the Transaction Details response are also **nullable**. This includes any sub-components (objects or fields) also marked `required`.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI(
    security=shared.Security(
        o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.GetTransactionDetailsRequest(
    reference='<value>',
)

res = s.transactions.get_transaction_details(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetTransactionDetailsRequest](../../models/operations/gettransactiondetailsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetTransactionDetailsResponse](../../models/operations/gettransactiondetailsresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorsBoltAPIResponse | 403,422                      | application/json             |
| errors.SDKError              | 4x-5xx                       | */*                          |

## refund_transaction

This refunds a captured transaction. Refunds can be done for any partial amount or for the total authorized amount. These refunds are processed synchronously and return information about the refunded transaction in the standard `transaction_view` object.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI(
    security=shared.Security(
        o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.RefundTransactionRequest()

res = s.transactions.refund_transaction(req)

if res.transaction_view is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RefundTransactionRequest](../../models/operations/refundtransactionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.RefundTransactionResponse](../../models/operations/refundtransactionresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorsBoltAPIResponse | 422                          | application/json             |
| errors.SDKError              | 4x-5xx                       | */*                          |

## update_transaction

This allows you to update certain transaction properties post-authorization.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI(
    security=shared.Security(
        o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.UpdateTransactionRequest(
    reference='<value>',
)

res = s.transactions.update_transaction(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateTransactionRequest](../../models/operations/updatetransactionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateTransactionResponse](../../models/operations/updatetransactionresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorsBoltAPIResponse | 403,404                      | application/json             |
| errors.SDKError              | 4x-5xx                       | */*                          |

## void_transaction

This voids the authorization for a given transaction. Voids must be completed before the authorization is captured.
In the request, either `transaction_id` or `transaction_reference` is required.
Although the response returns the standard `transaction_view` object, only `status` and either `id` or `reference` are needed.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI(
    security=shared.Security(
        o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.VoidTransactionRequest()

res = s.transactions.void_transaction(req)

if res.transaction_view is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.VoidTransactionRequest](../../models/operations/voidtransactionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.VoidTransactionResponse](../../models/operations/voidtransactionresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorsBoltAPIResponse | 403,404                      | application/json             |
| errors.SDKError              | 4x-5xx                       | */*                          |
