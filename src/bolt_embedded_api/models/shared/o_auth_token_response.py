"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OAuthTokenResponse:
    r"""OAuth token response."""
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""An access token you can use to make requests on behalf of a Bolt Account."""
    expires_in: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_in'), 'exclude': lambda f: f is None }})
    r"""Access token’s expiration in seconds."""
    id_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id_token'), 'exclude': lambda f: f is None }})
    r"""A JWT token issued when the request includes the scope open_id."""
    refresh_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token'), 'exclude': lambda f: f is None }})
    r"""A refresh token you can use to issue a brand new access token without obtaining a new authorization code."""
    refresh_token_scope: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token_scope'), 'exclude': lambda f: f is None }})
    r"""The scope granted to the refresh token. Currently this will always be bolt.account.view."""
    scope: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scope'), 'exclude': lambda f: f is None }})
    r"""The scope granted to access token, depending on the scope granted to the authorization code as well as the scope parameter. Options include `bolt.account.manage`, `bolt.account.view`, `openid`."""
    token_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_type'), 'exclude': lambda f: f is None }})
    r"""The token_type will always be bearer."""
    

