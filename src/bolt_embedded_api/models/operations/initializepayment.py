"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cart_create as shared_cart_create
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional



@dataclasses.dataclass
class InitializePaymentSecurity:
    o_auth: Optional[str] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    x_api_key: Optional[str] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InitializePaymentRequestBodyShopperIdentity:
    r"""Identification information for the Shopper. This is only required when creating a new Bolt account."""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""Email address of the shopper"""
    first_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    r"""First name of the shopper"""
    last_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    r"""Last name of the shopper"""
    phone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone') }})
    r"""Phone number of the shopper"""
    create_bolt_account: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('create_bolt_account'), 'exclude': lambda f: f is None }})
    r"""determines whether to create a bolt account for this shopper"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InitializePaymentRequestBody:
    cart: shared_cart_create.CartCreate = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cart') }})
    r"""The details of the cart being purchased with this payment."""
    shopper_identity: Optional[InitializePaymentRequestBodyShopperIdentity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shopper_identity'), 'exclude': lambda f: f is None }})
    r"""Identification information for the Shopper. This is only required when creating a new Bolt account."""
    




@dataclasses.dataclass
class InitializePaymentRequest:
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Idempotency-Key', 'style': 'simple', 'explode': False }})
    r"""A key created by merchants that ensures `POST` and `PATCH` requests are only performed once. [Read more about Idempotent Requests here](/developers/references/idempotency/)."""
    request_body: Optional[InitializePaymentRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    x_publishable_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Publishable-Key', 'style': 'simple', 'explode': False }})
    r"""The publicly viewable identifier used to identify a merchant division. This key is found in the Developer > API section of the Bolt Merchant Dashboard [RECOMMENDED]."""
    


class InitializePayment200ApplicationJSONStatus(str, Enum):
    r"""The current payment status."""
    AWAITING_USER_CONFIRMATION = 'awaiting_user_confirmation'
    PAYMENT_READY = 'payment_ready'
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InitializePayment200ApplicationJSON:
    r"""Payment token retrieved."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The ID for a Payment Attempt"""
    status: Optional[InitializePayment200ApplicationJSONStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The current payment status."""
    




@dataclasses.dataclass
class InitializePaymentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    initialize_payment_200_application_json_object: Optional[InitializePayment200ApplicationJSON] = dataclasses.field(default=None)
    r"""Payment token retrieved."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
