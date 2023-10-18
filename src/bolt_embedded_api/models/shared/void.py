"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class VoidCause(str, Enum):
    r"""Specifies why this particular transaction is voided."""
    MERCHANT_ACTION = 'merchant_action'
    PAYPAL_SYNC = 'paypal_sync'
    AMAZON_PAY_SYNC = 'amazon_pay_sync'
    IRREVERSIBLE_REJECT = 'irreversible_reject'
    AUTH_EXPIRE = 'auth_expire'
    AUTH_VERIFICATION_EXPIRED = 'auth_verification_expired'
    PAYMENT_METHOD_UPDATER = 'payment_method_updater'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class VoidStatus(str, Enum):
    r"""The status of the void request."""
    SUCCEEDED = 'succeeded'
    DECLINED = 'declined'
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Void:
    cause: Optional[VoidCause] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cause'), 'exclude': lambda f: f is None }})
    r"""Specifies why this particular transaction is voided."""
    merchant_event_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_event_id'), 'exclude': lambda f: f is None }})
    r"""The reference ID associated with a transaction event (auth, capture, refund, void). This is an arbitrary identifier created by the merchant. Bolt does not enforce any uniqueness constraints on this ID. It is up to the merchant to generate identifiers that properly fulfill its needs."""
    status: Optional[VoidStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the void request."""
    void: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('void'), 'exclude': lambda f: f is None }})
    r"""The void ID returned from the payment processor."""
    

