"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errors_oauth_server_response as shared_errors_oauth_server_response
from ..shared import o_auth_token_response as shared_o_auth_token_response
from typing import Any, Optional



@dataclasses.dataclass
class OAuthTokenRequest:
    request_body: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    x_publishable_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Publishable-Key', 'style': 'simple', 'explode': False }})
    r"""The publicly viewable identifier used to identify a merchant division. This key is found in the Developer > API section of the Bolt Merchant Dashboard [RECOMMENDED]."""
    




@dataclasses.dataclass
class OAuthTokenResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    errors_oauth_server_response: Optional[shared_errors_oauth_server_response.ErrorsOauthServerResponse] = dataclasses.field(default=None)
    r"""Invalid request to OAuth Token."""
    o_auth_token_response: Optional[shared_o_auth_token_response.OAuthTokenResponse] = dataclasses.field(default=None)
    r"""OAuth token response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

