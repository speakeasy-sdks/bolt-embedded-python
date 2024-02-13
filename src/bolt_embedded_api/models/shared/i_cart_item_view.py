"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .amount_view import AmountView
from .cart_item_customization import CartItemCustomization
from .gift_option_view import GiftOptionView
from .i_weight import IWeight
from .subscription import Subscription
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Properties:
    color: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('color'), 'exclude': lambda f: f is None }})
    display: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    


class ICartItemViewShipmentType(str, Enum):
    UNKNOWN = 'unknown'
    DOOR_DELIVERY = 'door_delivery'
    SHIP_TO_STORE = 'ship_to_store'
    IN_STORE_PICKUP = 'in_store_pickup'
    SHIP_TO_HOME_ONLY = 'ship_to_home_only'

class ICartItemViewType(str, Enum):
    UNKNOWN = 'unknown'
    DIGITAL = 'digital'
    PHYSICAL = 'physical'
    BUNDLED = 'bundled'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ICartItemView:
    UNSET='__SPEAKEASY_UNSET__'
    bolt_product_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bolt_product_id'), 'exclude': lambda f: f is None }})
    brand: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brand'), 'exclude': lambda f: f is None }})
    category: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category'), 'exclude': lambda f: f is ICartItemView.UNSET }})
    r"""Used to define a product category associated with the item."""
    collections: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collections'), 'exclude': lambda f: f is None }})
    color: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('color'), 'exclude': lambda f: f is None }})
    r"""Used to define the color of the item."""
    customizations: Optional[List[CartItemCustomization]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customizations'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    details_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details_url'), 'exclude': lambda f: f is None }})
    r"""Used to provide a link to the item's product page."""
    gift_option: Optional[GiftOptionView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gift_option'), 'exclude': lambda f: f is None }})
    r"""Defines which gift options are hidden."""
    hide: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hide'), 'exclude': lambda f: f is None }})
    image_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('image_url'), 'exclude': lambda f: f is None }})
    r"""Used to provide a link to the image associated with the item."""
    isbn: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isbn'), 'exclude': lambda f: f is ICartItemView.UNSET }})
    r"""Used to define the International Standard Book Number associated with the book."""
    item_group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item_group'), 'exclude': lambda f: f is None }})
    manufacturer: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('manufacturer'), 'exclude': lambda f: f is ICartItemView.UNSET }})
    r"""Used to define the organization that manufactured the item."""
    merchant_product_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_product_id'), 'exclude': lambda f: f is None }})
    merchant_variant_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_variant_id'), 'exclude': lambda f: f is None }})
    msrp: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('msrp'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    properties: Optional[List[Properties]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})
    quantity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    shipment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipment_id'), 'exclude': lambda f: f is None }})
    shipment_type: Optional[ICartItemViewShipmentType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipment_type'), 'exclude': lambda f: f is None }})
    shopify_line_item_reference: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shopify_line_item_reference'), 'exclude': lambda f: f is None }})
    shopify_product_reference: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shopify_product_reference'), 'exclude': lambda f: f is None }})
    shopify_product_variant_reference: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shopify_product_variant_reference'), 'exclude': lambda f: f is None }})
    size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    r"""Used to define the size of the item."""
    sku: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sku'), 'exclude': lambda f: f is ICartItemView.UNSET }})
    r"""Used to define an alpha-numeric Stock Keeping Unit associated with the item as it is mapped to your internal product catalogue."""
    subscription: Optional[Subscription] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscription'), 'exclude': lambda f: f is None }})
    r"""Describes a product added as a recurring subscription."""
    tags: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    r"""Used to define a comma-separated list of tags associated with the item."""
    tax_amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_amount'), 'exclude': lambda f: f is None }})
    taxable: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxable'), 'exclude': lambda f: f is None }})
    total_amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_amount'), 'exclude': lambda f: f is None }})
    type: Optional[ICartItemViewType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    unit_price: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_price'), 'exclude': lambda f: f is None }})
    uom: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uom'), 'exclude': lambda f: f is ICartItemView.UNSET }})
    r"""Used to define the unit of measure used to describe the product."""
    upc: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upc'), 'exclude': lambda f: f is ICartItemView.UNSET }})
    r"""Used to define the 12-digit Universal Product Code (a barcode) associated with the item worldwide."""
    weight: Optional[IWeight] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight'), 'exclude': lambda f: f is None }})
    

