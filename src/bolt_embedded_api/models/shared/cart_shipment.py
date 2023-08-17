"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address as shared_address
from ..shared import cart_shipment_type as shared_cart_shipment_type
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CartShipment:
    r"""A cart that is being prepared for shipment"""
    carrier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier'), 'exclude': lambda f: f is None }})
    r"""The name of the carrier selected."""
    cost: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cost'), 'exclude': lambda f: f is None }})
    r"""The cost in cents."""
    discounted_by_membership: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discounted_by_membership'), 'exclude': lambda f: f is None }})
    r"""Defines if shopper has a membership discount."""
    estimated_delivery_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('estimated_delivery_date'), 'exclude': lambda f: f is None }})
    r"""The estimated delivery date."""
    expedited: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expedited'), 'exclude': lambda f: f is None }})
    r"""True if shipment is expedited."""
    package_depth: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('package_depth'), 'exclude': lambda f: f is None }})
    r"""The depth."""
    package_dimension_unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('package_dimension_unit'), 'exclude': lambda f: f is None }})
    r"""The unit of measurement for an item's dimensions."""
    package_height: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('package_height'), 'exclude': lambda f: f is None }})
    r"""The height."""
    package_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('package_type'), 'exclude': lambda f: f is None }})
    r"""The type of package."""
    package_weight_unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('package_weight_unit'), 'exclude': lambda f: f is None }})
    r"""The unit of measurement for an item's weight."""
    package_width: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('package_width'), 'exclude': lambda f: f is None }})
    r"""The width."""
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})
    r"""The service name."""
    shipping_address: Optional[shared_address.Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_address'), 'exclude': lambda f: f is None }})
    r"""The Address object is used for billing, shipping, and physical store address use cases."""
    shipping_address_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_address_id'), 'exclude': lambda f: f is None }})
    r"""ID for billing address"""
    shipping_method: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_method'), 'exclude': lambda f: f is None }})
    r"""The name of the shipping method."""
    signature: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signature'), 'exclude': lambda f: f is None }})
    r"""The signature."""
    tax_amount: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_amount'), 'exclude': lambda f: f is None }})
    r"""Tax amount in cents."""
    tax_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_code'), 'exclude': lambda f: f is None }})
    r"""The relevant tax code."""
    total_weight: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_weight'), 'exclude': lambda f: f is None }})
    r"""The total weight."""
    total_weight_unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_weight_unit'), 'exclude': lambda f: f is None }})
    r"""The unit of measurement for an item's weight."""
    type: Optional[shared_cart_shipment_type.CartShipmentType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type corresponding to this shipment, if applicable."""
    
