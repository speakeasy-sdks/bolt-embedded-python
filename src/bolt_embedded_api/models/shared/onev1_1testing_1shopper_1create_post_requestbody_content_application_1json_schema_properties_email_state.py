"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class Onev11testing1shopper1createPostRequestBodyContentApplication1jsonSchemaPropertiesEmailState(str, Enum):
    r"""The status of the shopper account identifier (email or phone). If the account does not have this identifier, the status is \\"missing\\"; If the identifier has been used to receive an OTP code, the status is \\"verified\\"; If the identifier has not been used to receive an OTP code, the status is \\"unverified\\"."""
    MISSING = 'missing'
    VERIFIED = 'verified'
    UNVERIFIED = 'unverified'
