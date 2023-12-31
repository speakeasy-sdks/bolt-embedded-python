"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .consumer_membership_status import ConsumerMembershipStatus
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConsumerUserMembership:
    r"""**Nullable** for Transactions Details."""
    status: ConsumerMembershipStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""True if user has an AllPass membership associated to their Bolt Account. **Nullable** for Transactions Details."""
    

