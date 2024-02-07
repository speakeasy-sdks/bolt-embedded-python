"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import credit_card_void as shared_credit_card_void
from ...models.shared import transaction_view as shared_transaction_view
from typing import Optional


@dataclasses.dataclass
class VoidTransactionSecurity:
    x_api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    



@dataclasses.dataclass
class VoidTransactionRequest:
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Idempotency-Key', 'style': 'simple', 'explode': False }})
    r"""A key created by merchants that ensures `POST` and `PATCH` requests are only performed once. [Read more about Idempotent Requests here](/developers/references/idempotency/)."""
    credit_card_void: Optional[shared_credit_card_void.CreditCardVoid] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Void a Transaction"""
    



@dataclasses.dataclass
class VoidTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    transaction_view: Optional[shared_transaction_view.TransactionView] = dataclasses.field(default=None)
    r"""Void Successful"""
    

