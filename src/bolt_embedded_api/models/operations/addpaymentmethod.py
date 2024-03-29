"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import address as shared_address
from ...models.shared import metadata as shared_metadata
from ...models.shared import saved_credit_card_view as shared_saved_credit_card_view
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class AddPaymentMethodSecurity:
    o_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    x_api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    


class Network(str, Enum):
    UNKNOWN = 'unknown'
    VISA = 'visa'
    MASTERCARD = 'mastercard'
    AMEX = 'amex'
    DISCOVER = 'discover'
    DINERS_CLUB_US_CA = 'diners_club_us_ca'
    JCB = 'jcb'
    UNIONPAY = 'unionpay'
    ALLIANCEDATA = 'alliancedata'
    CITIPLCC = 'citiplcc'

class Priority(int, Enum):
    r"""Used to indicate the card's priority. '1' indicates primary, while '2' indicates a secondary card."""
    ONE = 1
    TWO = 2

class TokenType(str, Enum):
    r"""Used to define which payment processor generated the token for this credit card.  For those using Bolt's tokenizer, the value must be `bolt`."""
    VANTIV = 'vantiv'
    APPLEPAY = 'applepay'
    BOLT = 'bolt'
    STRIPE = 'stripe'
    PLCC = 'plcc'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddPaymentMethodRequestBody:
    r"""The `credit_card` object is used to to pay for guest checkout transactions or save payment method details to an account. Once saved, you can reference the credit card with the associated `credit_card_id` for future transactions."""
    UNSET='__SPEAKEASY_UNSET__'
    billing_address: shared_address.Address = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address') }})
    r"""The Address object is used for billing, shipping, and physical store address use cases."""
    expiration: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiration') }})
    r"""The expiration date of the credit card."""
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    r"""The Bolt token associated to the credit card."""
    billing_address_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_id'), 'exclude': lambda f: f is AddPaymentMethodRequestBody.UNSET }})
    r"""The unique Bolt ID associated with a saved shopper address. This can be obtained by accessing a shopper's account details. If you use this field, you do not need to use `billing_address`."""
    bin: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bin'), 'exclude': lambda f: f is None }})
    r"""The Bank Identification Number for the credit card. This is typically the first 4-6 digits of the credit card number."""
    cryptogram: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cryptogram'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""This can be left empty. A 3-digit ISO code for currency that will be used in the credit card authorization."""
    eci: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eci'), 'exclude': lambda f: f is None }})
    last4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last4'), 'exclude': lambda f: f is None }})
    r"""The last 4 digits of the credit card number."""
    metadata: Optional[shared_metadata.Metadata] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is AddPaymentMethodRequestBody.UNSET }})
    r"""A key-value pair object that allows users to store arbitrary information associated with an object.  For any individual account object, we allow up to 50 keys. Keys can be up to 40 characters long and values can be up to 500 characters long.  Metadata should not contain any sensitive customer information, like PII (Personally Identifiable Information). For more information about metadata, see our [documentation](https://help.bolt.com/developers/references/embedded-metadata/)."""
    network: Optional[Network] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('network'), 'exclude': lambda f: f is None }})
    number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number'), 'exclude': lambda f: f is None }})
    r"""Used to provide ApplePay DPAN or private label credit card PAN when applicable. Required when charging a private label credit card."""
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code'), 'exclude': lambda f: f is None }})
    r"""Used for the postal or zip code associated with the credit card."""
    priority: Optional[Priority] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('priority'), 'exclude': lambda f: f is None }})
    r"""Used to indicate the card's priority. '1' indicates primary, while '2' indicates a secondary card."""
    save: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('save'), 'exclude': lambda f: f is None }})
    r"""Determines whether or not the credit card will be saved to the shopper's account. Defaults to `true`."""
    token_type: Optional[TokenType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_type'), 'exclude': lambda f: f is None }})
    r"""Used to define which payment processor generated the token for this credit card.  For those using Bolt's tokenizer, the value must be `bolt`."""
    



@dataclasses.dataclass
class AddPaymentMethodRequest:
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Idempotency-Key', 'style': 'simple', 'explode': False }})
    r"""A key created by merchants that ensures `POST` and `PATCH` requests are only performed once. [Read more about Idempotent Requests here](/developers/references/idempotency/)."""
    request_body: Optional[AddPaymentMethodRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    x_publishable_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Publishable-Key', 'style': 'simple', 'explode': False }})
    r"""The publicly viewable identifier used to identify a merchant division. This key is found in the Developer > API section of the Bolt Merchant Dashboard [RECOMMENDED]."""
    



@dataclasses.dataclass
class AddPaymentMethodResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    saved_credit_card_view: Optional[shared_saved_credit_card_view.SavedCreditCardView] = dataclasses.field(default=None)
    r"""Payment Method Added"""
    

