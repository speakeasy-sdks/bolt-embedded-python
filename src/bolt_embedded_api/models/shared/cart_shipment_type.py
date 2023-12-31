"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class CartShipmentType(str, Enum):
    r"""The type corresponding to this shipment, if applicable."""
    DOOR_DELIVERY = 'door_delivery'
    IN_STORE_PICKUP = 'in_store_pickup'
    SHIP_TO_STORE = 'ship_to_store'
    SHIP_TO_HOME_ONLY = 'ship_to_home_only'
    UNKNOWN = 'unknown'
