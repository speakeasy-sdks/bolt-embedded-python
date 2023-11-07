"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import account_details as shared_account_details
from typing import Optional


@dataclasses.dataclass
class GetAccountSecurity:
    o_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    x_api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    



@dataclasses.dataclass
class GetAccountRequest:
    x_publishable_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Publishable-Key', 'style': 'simple', 'explode': False }})
    r"""The publicly viewable identifier used to identify a merchant division. This key is found in the Developer > API section of the Bolt Merchant Dashboard [RECOMMENDED]."""
    



@dataclasses.dataclass
class GetAccountResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    account_details: Optional[shared_account_details.AccountDetails] = dataclasses.field(default=None)
    r"""Account Details Fetched"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

