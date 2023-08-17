"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AddressView:
    r"""The address object returned in the response."""
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    r"""The company name associated with this address."""
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""The name of the country associated with this address."""
    country_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_code'), 'exclude': lambda f: f is None }})
    r"""The ISO 3166-1 alpha-2 country code associated with this address."""
    door_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('door_code'), 'exclude': lambda f: f is None }})
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
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The given and surname of the person associated with this address."""
    phone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is None }})
    r"""A phone number following E164 standards, in its globalized format, i.e. prepended with a plus sign."""
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code'), 'exclude': lambda f: f is None }})
    r"""The postal or zip code associated with this address."""
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""The region details such as state or province associated with this address."""
    region_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region_code'), 'exclude': lambda f: f is None }})
    r"""The the ISO 3166-2 region code associated with this address."""
    street_address1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address1'), 'exclude': lambda f: f is None }})
    r"""The street number and street name of the address."""
    street_address2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address2'), 'exclude': lambda f: f is None }})
    r"""Any apartment, floor, or unit details."""
    street_address3: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address3'), 'exclude': lambda f: f is None }})
    r"""Any additional street address details."""
    street_address4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address4'), 'exclude': lambda f: f is None }})
    r"""Any additional street address details."""
    
