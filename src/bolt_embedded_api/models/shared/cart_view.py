"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .address_view import AddressView
from .amount_view import AmountView
from .i_cart_discount_view import ICartDiscountView
from .i_cart_item_view import ICartItemView
from .i_cart_shipment_view import ICartShipmentView
from .i_currency import ICurrency
from .in_store_shipment2 import InStoreShipment2
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CartViewFulfillments:
    cart_shipment: Optional[ICartShipmentView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cart_shipment'), 'exclude': lambda f: f is None }})
    fulfillment_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fulfillment_type'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    in_store_cart_shipment: Optional[InStoreShipment2] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('in_store_cart_shipment'), 'exclude': lambda f: f is None }})
    r"""A cart that is being prepared for shipment"""
    items: Optional[List[ICartItemView]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LoyaltyRewards:
    amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    coupon_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('coupon_code'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    details: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    points: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('points'), 'exclude': lambda f: f is None }})
    source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CartView:
    r"""This is the cart object returned in a successful response."""
    billing_address: Optional[AddressView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    r"""The address object returned in the response."""
    cart_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cart_url'), 'exclude': lambda f: f is None }})
    r"""Used to provide a link to the cart ID."""
    currency: Optional[ICurrency] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    discount_amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discount_amount'), 'exclude': lambda f: f is None }})
    discounts: Optional[List[ICartDiscountView]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discounts'), 'exclude': lambda f: f is None }})
    display_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_id'), 'exclude': lambda f: f is None }})
    fee_amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fee_amount'), 'exclude': lambda f: f is None }})
    fees: Optional[List[ICartItemView]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fees'), 'exclude': lambda f: f is None }})
    fulfillments: Optional[List[CartViewFulfillments]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fulfillments'), 'exclude': lambda f: f is None }})
    in_store_shipments: Optional[InStoreShipment2] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('in_store_shipments'), 'exclude': lambda f: f is None }})
    r"""A cart that is being prepared for shipment"""
    items: Optional[List[ICartItemView]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    loyalty_rewards: Optional[List[LoyaltyRewards]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loyalty_rewards'), 'exclude': lambda f: f is None }})
    loyalty_rewards_amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loyalty_rewards_amount'), 'exclude': lambda f: f is None }})
    merchant_order_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_order_url'), 'exclude': lambda f: f is None }})
    metadata: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    msrp: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('msrp'), 'exclude': lambda f: f is None }})
    order_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_description'), 'exclude': lambda f: f is None }})
    r"""Used optionally to pass additional information like order numbers or other IDs as needed."""
    order_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_reference'), 'exclude': lambda f: f is None }})
    r"""This value is used by Bolt as an external reference to a given order. This reference must be unique per successful transaction."""
    shipments: Optional[List[ICartShipmentView]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipments'), 'exclude': lambda f: f is None }})
    shipping_amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_amount'), 'exclude': lambda f: f is None }})
    subtotal_amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtotal_amount'), 'exclude': lambda f: f is None }})
    tax_amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_amount'), 'exclude': lambda f: f is None }})
    total_amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_amount'), 'exclude': lambda f: f is None }})
    transaction_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_reference'), 'exclude': lambda f: f is None }})
    r"""The 12 digit reference ID associated to a given transaction webhook for an order."""
    

