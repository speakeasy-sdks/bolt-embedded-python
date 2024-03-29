"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .address_view import AddressView
from .card_network import CardNetwork
from .metadata import Metadata
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SavedCreditCardViewType(str, Enum):
    r"""The payment method type. If empty, the property defaults to `card`."""
    CARD = 'card'
    PAYPAL = 'paypal'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavedCreditCardView:
    r"""Saved Credit Card Detail"""
    UNSET='__SPEAKEASY_UNSET__'
    billing_address: Optional[AddressView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    r"""The address object returned in the response."""
    default: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default'), 'exclude': lambda f: f is None }})
    r"""The default card payment method chosen by the shopper."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The APM account identifier; usually the email address."""
    exp_month: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exp_month'), 'exclude': lambda f: f is None }})
    r"""The expiration month of the credit card."""
    exp_year: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exp_year'), 'exclude': lambda f: f is None }})
    r"""The expiration year of the credit card."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The ID of the payment method associated with the Shopper's account."""
    last4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last4'), 'exclude': lambda f: f is None }})
    r"""The card's last 4 digits. **Nullable** for Transactions Details."""
    metadata: Optional[Metadata] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is SavedCreditCardView.UNSET }})
    r"""A key-value pair object that allows users to store arbitrary information associated with an object.  For any individual account object, we allow up to 50 keys. Keys can be up to 40 characters long and values can be up to 500 characters long.  Metadata should not contain any sensitive customer information, like PII (Personally Identifiable Information). For more information about metadata, see our [documentation](https://help.bolt.com/developers/references/embedded-metadata/)."""
    network: Optional[CardNetwork] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('network'), 'exclude': lambda f: f is None }})
    r"""The card's network code. **Nullable** for Transactions Details. Note: LEGACY diners_club_us_ca now tagged as mastercard"""
    type: Optional[SavedCreditCardViewType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The payment method type. If empty, the property defaults to `card`."""
    

