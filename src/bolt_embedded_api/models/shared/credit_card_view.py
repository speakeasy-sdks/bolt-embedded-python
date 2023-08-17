"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address_view as shared_address_view
from ..shared import card_display_network as shared_card_display_network
from ..shared import card_network as shared_card_network
from ..shared import card_status as shared_card_status
from ..shared import card_token_type as shared_card_token_type
from ..shared import priority as shared_priority
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreditCardView:
    r"""Contains details about the credit card transaction."""
    billing_address: Optional[shared_address_view.AddressView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    r"""The address object returned in the response."""
    bin: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bin'), 'exclude': lambda f: f is None }})
    r"""The Bank Identification Number for the credit card; this is typically the first 4-6 digits of the credit card number. **Nullable** for Transactions Details."""
    display_network: Optional[shared_card_display_network.CardDisplayNetwork] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_network'), 'exclude': lambda f: f is None }})
    r"""The card's network. **Nullable** for Transactions Details."""
    expiration: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiration'), 'exclude': lambda f: f is None }})
    r"""The card's expiration. **Nullable** for Transactions Details."""
    icon_asset_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon_asset_path'), 'exclude': lambda f: f is None }})
    r"""The asset link for displayed icons. This link varies depending on payment method used.  **Nullable** for Transactions Details."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The card's ID. **Nullable** for Transactions Details."""
    last4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last4'), 'exclude': lambda f: f is None }})
    r"""The card's last 4 digits. **Nullable** for Transactions Details."""
    network: Optional[shared_card_network.CardNetwork] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('network'), 'exclude': lambda f: f is None }})
    r"""The card's network code. **Nullable** for Transactions Details. Note: LEGACY diners_club_us_ca now tagged as mastercard"""
    priority: Optional[shared_priority.Priority] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('priority'), 'exclude': lambda f: f is None }})
    r"""Describes the card's priority."""
    status: Optional[shared_card_status.CardStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The card's status. **Nullable** for Transactions Details."""
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    r"""The Bolt token associated to the credit card. Required for new, unsaved cards."""
    token_type: Optional[shared_card_token_type.CardTokenType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_type'), 'exclude': lambda f: f is None }})
    r"""Used to define which payment processor generated the token for this credit card."""
    

