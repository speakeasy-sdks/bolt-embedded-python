"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RiskModelExternalResultView:
    available: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('available'), 'exclude': lambda f: f is None }})
    decision_factors: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('decision_factors'), 'exclude': lambda f: f is None }})
    r"""Used to list a total of up to 5 decision factors used by the risk model to determine the risk analysis result."""
    fraud_probability: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fraud_probability'), 'exclude': lambda f: f is None }})
    payment_instrument_factors: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_instrument_factors'), 'exclude': lambda f: f is None }})
    

