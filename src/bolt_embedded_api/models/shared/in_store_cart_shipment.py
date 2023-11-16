"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .address import Address
from .cart_shipment import CartShipment
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DistanceUnit(str, Enum):
    KM = 'km'
    MILE = 'mile'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InStoreCartShipment:
    cart_shipment: Optional[CartShipment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cart_shipment'), 'exclude': lambda f: f is None }})
    r"""A cart that is being prepared for shipment"""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Shipment option description."""
    distance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('distance'), 'exclude': lambda f: f is None }})
    distance_unit: Optional[DistanceUnit] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('distance_unit'), 'exclude': lambda f: f is None }})
    in_store_pickup_address: Optional[Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('in_store_pickup_address'), 'exclude': lambda f: f is None }})
    r"""The Address object is used for billing, shipping, and physical store address use cases."""
    pickup_window_close: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pickup_window_close'), 'exclude': lambda f: f is None }})
    pickup_window_open: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pickup_window_open'), 'exclude': lambda f: f is None }})
    store_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('store_name'), 'exclude': lambda f: f is None }})
    r"""The local store's name where the item can be picked up."""
    

