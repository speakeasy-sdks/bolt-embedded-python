"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import email_priority as shared_email_priority
from ..shared import email_status as shared_email_status
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Emails:
    r"""An object of user email."""
    address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    r"""An email address."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""This is the ID for the email address associated with the shopper."""
    priority: Optional[shared_email_priority.EmailPriority] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('priority'), 'exclude': lambda f: f is None }})
    r"""This is the priority of the contact method. This field's contents are not displayed in the transaction details view."""
    status: Optional[shared_email_status.EmailStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""This is the status of the contact method."""
    

