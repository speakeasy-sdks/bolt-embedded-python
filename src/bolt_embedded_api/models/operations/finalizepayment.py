"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class FinalizePaymentSecurity:
    o_auth: Optional[str] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    x_api_key: Optional[str] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FinalizePaymentRequestBodyShopperIdentity:
    r"""Identification information for the Shopper"""
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
class FinalizePaymentRequestBody:
    merchant_event_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_event_id'), 'exclude': lambda f: f is None }})
    r"""The reference ID associated with a transaction event (auth, capture, refund, void). This is an arbitrary identifier created by the merchant. Bolt does not enforce any uniqueness constraints on this ID. It is up to the merchant to generate identifiers that properly fulfill its needs."""
    shopper_identity: Optional[FinalizePaymentRequestBodyShopperIdentity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shopper_identity'), 'exclude': lambda f: f is None }})
    r"""Identification information for the Shopper"""
    



@dataclasses.dataclass
class FinalizePaymentRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The ID received in the initial v1/payments request."""
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Idempotency-Key', 'style': 'simple', 'explode': False }})
    r"""A key created by merchants that ensures `POST` and `PATCH` requests are only performed once. [Read more about Idempotent Requests here](/developers/references/idempotency/)."""
    request_body: Optional[FinalizePaymentRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FinalizePayment200ApplicationJSONPaypal:
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""An email address."""
    


class FinalizePayment200ApplicationJSONStatus(str, Enum):
    r"""The current payment status."""
    AWAITING_USER_CONFIRMATION = 'awaiting_user_confirmation'
    PAYMENT_READY = 'payment_ready'
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FinalizePayment200ApplicationJSONTransaction:
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    r"""The Bolt transaction reference (can be used to fetch transaction details, capture, void or refund transaction)"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FinalizePayment200ApplicationJSON:
    r"""Payment Token Retrieved"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The ID for the given Payment Attempt"""
    payment_method_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_method_id'), 'exclude': lambda f: f is None }})
    r"""ID of the payment method in Bolt's system, only if the payment method is saved."""
    paypal: Optional[FinalizePayment200ApplicationJSONPaypal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paypal'), 'exclude': lambda f: f is None }})
    status: Optional[FinalizePayment200ApplicationJSONStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The current payment status."""
    transaction: Optional[FinalizePayment200ApplicationJSONTransaction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class FinalizePaymentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    finalize_payment_200_application_json_object: Optional[FinalizePayment200ApplicationJSON] = dataclasses.field(default=None)
    r"""Payment Token Retrieved"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

