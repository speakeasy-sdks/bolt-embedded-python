"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ProfileMetadata:
    r"""A key-value pair object that allows users to store arbitrary information associated with an object.  For any individual account object, we allow up to 50 keys. Keys can be up to 40 characters long and values can be up to 500 characters long.  Metadata should not contain any sensitive customer information, like PII (Personally Identifiable Information). For more information about metadata, see our [documentation](https://help.bolt.com/developers/references/embedded-metadata/)."""
    additional_properties: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalProperties'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Profile:
    r"""The first name, last name, email address, and phone number of a shopper."""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""An email address."""
    first_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    r"""The given name of the person associated with this record."""
    last_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    r"""The surname of the person associated with this record."""
    phone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone') }})
    r"""A phone number following E164 standards, in its globalized format, i.e. prepended with a plus sign."""
    metadata: Optional[ProfileMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    r"""A key-value pair object that allows users to store arbitrary information associated with an object.  For any individual account object, we allow up to 50 keys. Keys can be up to 40 characters long and values can be up to 500 characters long.  Metadata should not contain any sensitive customer information, like PII (Personally Identifiable Information). For more information about metadata, see our [documentation](https://help.bolt.com/developers/references/embedded-metadata/)."""
    

