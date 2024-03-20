"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import transaction_view as shared_transaction_view
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RefundTransactionRequestBody:
    r"""Refund a Transaction"""
    amount: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount in cents. **Nullable** for Transactions Details."""
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""The 3-digit ISO code for the currency. **Nullable** for Transactions Details."""
    transaction_reference: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_reference') }})
    r"""The transaction's 12-digit Bolt reference ID. **Nullable** for Transactions Details."""
    merchant_event_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_event_id'), 'exclude': lambda f: f is None }})
    r"""The reference ID associated with a transaction event (auth, capture, refund, void). This is an arbitrary identifier created by the merchant. Bolt does not enforce any uniqueness constraints on this ID. It is up to the merchant to generate identifiers that properly fulfill its needs."""
    skip_hook_notification: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skip_hook_notification'), 'exclude': lambda f: f is None }})
    r"""Set to `true` to skip receiving a webhook notification from Bolt that is triggered by this update to the transaction."""
    



@dataclasses.dataclass
class RefundTransactionRequest:
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Idempotency-Key', 'style': 'simple', 'explode': False }})
    r"""A key created by merchants that ensures `POST` and `PATCH` requests are only performed once. [Read more about Idempotent Requests here](/developers/references/idempotency/)."""
    request_body: Optional[RefundTransactionRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Refund a Transaction"""
    



@dataclasses.dataclass
class RefundTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    transaction_view: Optional[shared_transaction_view.TransactionView] = dataclasses.field(default=None)
    r"""Refund Successful"""
    

