"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import o_auth_token_input as shared_o_auth_token_input
from ...models.shared import o_auth_token_input_refresh as shared_o_auth_token_input_refresh
from ...models.shared import o_auth_token_response as shared_o_auth_token_response
from typing import Optional, Union


@dataclasses.dataclass
class OAuthTokenRequestBody:
    pass


@dataclasses.dataclass
class OAuthTokenRequest:
    request_body: Optional[Union[shared_o_auth_token_input.OAuthTokenInput, shared_o_auth_token_input_refresh.OAuthTokenInputRefresh]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    x_publishable_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Publishable-Key', 'style': 'simple', 'explode': False }})
    r"""The publicly viewable identifier used to identify a merchant division. This key is found in the Developer > API section of the Bolt Merchant Dashboard [RECOMMENDED]."""
    



@dataclasses.dataclass
class OAuthTokenResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    o_auth_token_response: Optional[shared_o_auth_token_response.OAuthTokenResponse] = dataclasses.field(default=None)
    r"""OAuth token response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

