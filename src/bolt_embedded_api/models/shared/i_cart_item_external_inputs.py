"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ICartItemExternalInputs:
    shopify_line_item_reference: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shopify_line_item_reference'), 'exclude': lambda f: f is None }})
    shopify_product_reference: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shopify_product_reference'), 'exclude': lambda f: f is None }})
    shopify_product_variant_reference: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shopify_product_variant_reference'), 'exclude': lambda f: f is None }})
    

