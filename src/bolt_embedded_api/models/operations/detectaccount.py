"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import v1_accounts_view as shared_v1_accounts_view
from typing import Optional


@dataclasses.dataclass
class DetectAccountRequest:
    x_publishable_key: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Publishable-Key', 'style': 'simple', 'explode': False }})
    r"""The publicly viewable identifier used to identify a merchant division. This key is found in the Developer > API section of the Bolt Merchant Dashboard."""
    email: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'email', 'style': 'form', 'explode': True }})
    r"""The shopper's email address is the primary mechanism for detecting an account. You **must** provide either a value for this parameter or for `sha256_email`."""
    phone: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'phone', 'style': 'form', 'explode': True }})
    r"""The shopper's phone number. Includes country code (e.g. +1); does not include dashes or spaces. Can be used to detect an account instead of `sha256_email` or `email`."""
    sha256_email: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sha256_email', 'style': 'form', 'explode': True }})
    r"""The sha256 hash of the shopper's normalized email address can be used to detect an account instead of `email`."""
    



@dataclasses.dataclass
class DetectAccountResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    v1_accounts_view: Optional[shared_v1_accounts_view.V1AccountsView] = dataclasses.field(default=None)
    r"""Has Bolt Account"""
    

