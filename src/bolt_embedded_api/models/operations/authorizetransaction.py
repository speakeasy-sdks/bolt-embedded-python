"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import i_authorize_result_view as shared_i_authorize_result_view
from ...models.shared import merchant_credit_card_authorization as shared_merchant_credit_card_authorization
from ...models.shared import merchant_credit_card_authorization_recharge as shared_merchant_credit_card_authorization_recharge
from typing import Optional, Union


@dataclasses.dataclass
class AuthorizeTransactionSecurity:
    o_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    x_api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    



@dataclasses.dataclass
class AuthorizeTransactionRequest:
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Idempotency-Key', 'style': 'simple', 'explode': False }})
    r"""A key created by merchants that ensures `POST` and `PATCH` requests are only performed once. [Read more about Idempotent Requests here](/developers/references/idempotency/)."""
    request_body: Optional[Union[shared_merchant_credit_card_authorization.MerchantCreditCardAuthorization, shared_merchant_credit_card_authorization_recharge.MerchantCreditCardAuthorizationRecharge]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""**Authorize a Transaction**
    * • `merchant_credit_card_authorization`: For authorizing with a new, unsaved card. This can be for a guest checkout flow, one-time payment, or an existing Bolt shopper.
    * • `merchant_credit_card_authorization_recharge`: For authorizing a card using a shoppers saved payment methods.
    * • **Anytime the shopper is paying while logged-in attach their OAuth `access_token` to the request.**
    """
    x_publishable_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Publishable-Key', 'style': 'simple', 'explode': False }})
    r"""The publicly viewable identifier used to identify a merchant division. This key is found in the Developer > API section of the Bolt Merchant Dashboard [RECOMMENDED]."""
    



@dataclasses.dataclass
class AuthorizeTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    i_authorize_result_view: Optional[shared_i_authorize_result_view.IAuthorizeResultView] = dataclasses.field(default=None)
    r"""Authorization Successful"""
    

