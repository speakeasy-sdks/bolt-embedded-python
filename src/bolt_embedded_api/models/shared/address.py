"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Address:
    r"""The Address object is used for billing, shipping, and physical store address use cases."""
    country_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_code') }})
    r"""The ISO 3166-1 alpha-2 country code associated with this address."""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""An email address."""
    first_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    r"""The given name of the person associated with this address."""
    last_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    r"""The surname of the person associated with this address."""
    locality: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('locality') }})
    r"""The city name details associated with this address."""
    postal_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code') }})
    r"""The the postal or zip code associated with this address."""
    region: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    r"""**Not Required for NON US addresses**. The region details such as state or province associated with this address."""
    street_address1: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address1') }})
    r"""The street number and street name of the address."""
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    r"""The company name associated with this address."""
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""The name of the country associated with this address."""
    default: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default'), 'exclude': lambda f: f is None }})
    r"""Whether the added address is now the default address."""
    door_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('door_code') }})
    r"""The building door code or community gate code."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The given and surname of the person associated with this address."""
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""A phone number following E164 standards, in its globalized format, i.e. prepended with a plus sign."""
    region_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region_code') }})
    r"""The ISO 3166-2 region code associated with this address.
      - * If specified, value must be valid for the `country`.
      - * If null, value is inferred from the `region`.
    """
    street_address2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address2'), 'exclude': lambda f: f is None }})
    r"""Any apartment, floor, or unit details."""
    street_address3: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address3') }})
    r"""Any additional street address details."""
    street_address4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address4') }})
    r"""Any additional street address details."""
    

