"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address as shared_address
from ..shared import cart_add_on as shared_cart_add_on
from ..shared import cart_discount as shared_cart_discount
from ..shared import cart_item as shared_cart_item
from ..shared import cart_loyalty_rewards as shared_cart_loyalty_rewards
from ..shared import cart_shipment as shared_cart_shipment
from ..shared import in_store_cart_shipment as shared_in_store_cart_shipment
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CartCreateFees:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the fee that will appear in the order ledger."""
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    reference: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference') }})
    r"""Unique reference used to identify the fee."""
    unit_price: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_price') }})
    unit_tax_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_tax_amount') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the fee that will appear in the tooltip if the mouse hovers over the fee."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CartCreateFulfillmentsDigitalDelivery:
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    


class CartCreateFulfillmentsType(str, Enum):
    PHYSICAL_DOOR_DELIVERY = 'physical_door_delivery'
    PHYSICAL_SHIP_TO_STORE = 'physical_ship_to_store'
    PHYSICAL_IN_STORE_PICKUP = 'physical_in_store_pickup'
    DIGITAL_DOWNLOAD = 'digital_download'
    DIGITAL_NO_DELIVERY = 'digital_no_delivery'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CartCreateFulfillments:
    r"""Defines the shipments associated with the cart items."""
    cart_items: Optional[list[shared_cart_item.CartItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cart_items'), 'exclude': lambda f: f is None }})
    cart_shipment: Optional[shared_cart_shipment.CartShipment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cart_shipment'), 'exclude': lambda f: f is None }})
    r"""A cart that is being prepared for shipment"""
    digital_delivery: Optional[CartCreateFulfillmentsDigitalDelivery] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('digital_delivery'), 'exclude': lambda f: f is None }})
    in_store_cart_shipment: Optional[shared_in_store_cart_shipment.InStoreCartShipment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('in_store_cart_shipment'), 'exclude': lambda f: f is None }})
    type: Optional[CartCreateFulfillmentsType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CartCreate:
    r"""The base_cart object contains the core details typically found in most cart objects, including items, discounts, amount totals, shipments, and in-store pickups."""
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    order_reference: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_reference') }})
    r"""This value is used by Bolt as an external reference to a given order. This reference must be unique per successful transaction."""
    total_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_amount') }})
    r"""The total amount, in cents, of the cart including its items and taxes (if applicable), e.g. $9.00 is 900. This total must match the sum of all other amounts."""
    add_ons: Optional[list[shared_cart_add_on.CartAddOn]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('add_ons'), 'exclude': lambda f: f is None }})
    billing_address: Optional[shared_address.Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    r"""The Address object is used for billing, shipping, and physical store address use cases."""
    cart_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cart_url'), 'exclude': lambda f: f is None }})
    r"""Used to provide a link to the cart ID."""
    discounts: Optional[list[shared_cart_discount.CartDiscount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discounts'), 'exclude': lambda f: f is None }})
    display_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_id'), 'exclude': lambda f: f is None }})
    r"""This field, although required, can be an empty string."""
    fees: Optional[list[CartCreateFees]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fees'), 'exclude': lambda f: f is None }})
    fulfillments: Optional[list[CartCreateFulfillments]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fulfillments'), 'exclude': lambda f: f is None }})
    in_store_cart_shipments: Optional[list[shared_in_store_cart_shipment.InStoreCartShipment]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('in_store_cart_shipments'), 'exclude': lambda f: f is None }})
    items: Optional[list[shared_cart_item.CartItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    r"""The list of items associated with the cart."""
    loyalty_rewards: Optional[list[shared_cart_loyalty_rewards.CartLoyaltyRewards]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loyalty_rewards'), 'exclude': lambda f: f is None }})
    metadata: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""Optional custom metadata."""
    order_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_description'), 'exclude': lambda f: f is None }})
    r"""Used optionally to pass additional information like order numbers or other IDs as needed."""
    shipments: Optional[list[shared_cart_shipment.CartShipment]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipments'), 'exclude': lambda f: f is None }})
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_amount'), 'exclude': lambda f: f is None }})
    r"""The total tax amount for all of the items associated with the cart."""
    

