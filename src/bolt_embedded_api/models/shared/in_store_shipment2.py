"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address_view as shared_address_view
from ..shared import in_store_shipment as shared_in_store_shipment
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class InStoreShipment2DistanceUnit(str, Enum):
    MILE = 'mile'
    KM = 'km'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InStoreShipment2:
    r"""A cart that is being prepared for shipment"""
    address: Optional[shared_address_view.AddressView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    r"""The address object returned in the response."""
    distance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('distance'), 'exclude': lambda f: f is None }})
    distance_unit: Optional[InStoreShipment2DistanceUnit] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('distance_unit'), 'exclude': lambda f: f is None }})
    shipment: Optional[shared_in_store_shipment.InStoreShipment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipment'), 'exclude': lambda f: f is None }})
    r"""A cart that is being prepared for shipment"""
    store_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('store_name'), 'exclude': lambda f: f is None }})
    
