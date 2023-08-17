"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CartAddOn:
    r"""A list of up to 3 add-ons that are displayed to the shopper."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the product being displayed as an add on."""
    price: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price') }})
    r"""The price of the product add on in cents (1/100)."""
    product_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productId') }})
    r"""The the ID of the product being displayed as an add on."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The description of the product being displayed as an add on."""
    image_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageUrl'), 'exclude': lambda f: f is None }})
    r"""The URL of the image displayed for the add on product."""
    product_page_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productPageUrl'), 'exclude': lambda f: f is None }})
    r"""The URL to the product page of the product being displayed as an add on."""
    
