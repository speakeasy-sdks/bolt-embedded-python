"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .metadata import Metadata
from .profile_view import ProfileView
from .saved_credit_card_view import SavedCreditCardView
from .saved_paypal_account_view import SavedPaypalAccountView
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Addresses:
    r"""The address object returned in the response."""
    UNSET='__SPEAKEASY_UNSET__'
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    r"""The company name associated with this address."""
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""The name of the country associated with this address."""
    country_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_code'), 'exclude': lambda f: f is None }})
    r"""The ISO 3166-1 alpha-2 country code associated with this address."""
    default: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default'), 'exclude': lambda f: f is None }})
    r"""The default shipping address chosen by the shopper."""
    door_code: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('door_code'), 'exclude': lambda f: f is Addresses.UNSET }})
    r"""The building door code or community gate code."""
    email_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_address'), 'exclude': lambda f: f is None }})
    r"""An email address."""
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name'), 'exclude': lambda f: f is None }})
    r"""The given name of the person associated with this address."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique Bolt ID associated with this address."""
    last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name'), 'exclude': lambda f: f is None }})
    r"""The surname of the person associated with this address."""
    locality: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('locality'), 'exclude': lambda f: f is None }})
    r"""The city name details associated with this address."""
    metadata: Optional[Metadata] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is Addresses.UNSET }})
    r"""A key-value pair object that allows users to store arbitrary information associated with an object.  For any individual account object, we allow up to 50 keys. Keys can be up to 40 characters long and values can be up to 500 characters long.  Metadata should not contain any sensitive customer information, like PII (Personally Identifiable Information). For more information about metadata, see our [documentation](https://help.bolt.com/developers/references/embedded-metadata/)."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The given and surname of the person associated with this address."""
    phone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is None }})
    r"""A phone number following E164 standards, in its globalized format, i.e. prepended with a plus sign."""
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code'), 'exclude': lambda f: f is None }})
    r"""The postal or zip code associated with this address."""
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""The region details such as state or province associated with this address."""
    region_code: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region_code'), 'exclude': lambda f: f is Addresses.UNSET }})
    r"""The the ISO 3166-2 region code associated with this address."""
    street_address1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address1'), 'exclude': lambda f: f is None }})
    r"""The street number and street name of the address."""
    street_address2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address2'), 'exclude': lambda f: f is None }})
    r"""Any apartment, floor, or unit details."""
    street_address3: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address3'), 'exclude': lambda f: f is Addresses.UNSET }})
    r"""Any additional street address details."""
    street_address4: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address4'), 'exclude': lambda f: f is Addresses.UNSET }})
    r"""Any additional street address details."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountDetails:
    addresses: Optional[List[Addresses]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addresses'), 'exclude': lambda f: f is None }})
    r"""A list of all addresses associated to the shopper's account."""
    has_bolt_account: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_bolt_account'), 'exclude': lambda f: f is None }})
    r"""Used to determine whether a Bolt Account exists with this shopper's account details."""
    payment_methods: Optional[List[Union[SavedCreditCardView, SavedPaypalAccountView]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_methods'), 'exclude': lambda f: f is None }})
    r"""A list of all payment methods associated to the shopper's account."""
    profile: Optional[ProfileView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profile'), 'exclude': lambda f: f is None }})
    r"""The shopper's account profile."""
    

