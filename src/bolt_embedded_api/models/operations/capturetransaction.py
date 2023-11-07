"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import capture_transaction_with_reference as shared_capture_transaction_with_reference
from ...models.shared import transaction_view as shared_transaction_view
from typing import Optional


@dataclasses.dataclass
class CaptureTransactionSecurity:
    x_api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    



@dataclasses.dataclass
class CaptureTransactionRequest:
    capture_transaction_with_reference: Optional[shared_capture_transaction_with_reference.CaptureTransactionWithReference] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Capture a Transaction"""
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Idempotency-Key', 'style': 'simple', 'explode': False }})
    r"""A key created by merchants that ensures `POST` and `PATCH` requests are only performed once. [Read more about Idempotent Requests here](/developers/references/idempotency/)."""
    



@dataclasses.dataclass
class CaptureTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    transaction_view: Optional[shared_transaction_view.TransactionView] = dataclasses.field(default=None)
    r"""Capture Successful"""
    

