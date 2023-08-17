"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ConsumerBillingAddress:
    locality: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('locality') }})
    r"""A locale such as county, district, etc."""
    postal_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code') }})
    r"""The postal code."""
    region: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    r"""A state, province, or similar region type."""
    street_address1: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address1') }})
    r"""You can use up to 4 street address fields."""
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    r"""The company's name"""
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""The country's name."""
    country_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_code'), 'exclude': lambda f: f is None }})
    r"""The 2-digit country code."""
    email_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_address'), 'exclude': lambda f: f is None }})
    r"""An email address."""
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name'), 'exclude': lambda f: f is None }})
    r"""The person's first name."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique Bolt ID associated with a previously saved billing address. Not applicable to new, unsaved addresses."""
    last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name'), 'exclude': lambda f: f is None }})
    r"""The person's last name."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The first and last name together as a string."""
    phone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is None }})
    r"""A phone number following E164 standards, in its globalized format, i.e. prepended with a plus sign."""
    street_address2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address2'), 'exclude': lambda f: f is None }})
    r"""You can use up to 4 street address fields."""
    street_address3: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address3'), 'exclude': lambda f: f is None }})
    r"""You can use up to 4 street address fields."""
    street_address4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address4'), 'exclude': lambda f: f is None }})
    r"""You can use up to 4 street address fields."""
    
