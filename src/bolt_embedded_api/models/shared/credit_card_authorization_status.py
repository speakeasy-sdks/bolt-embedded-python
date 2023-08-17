"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class CreditCardAuthorizationStatus(str, Enum):
    r"""The status of the authorization request.
      * `1` - succeeded
      * `2` - declined
      * `3` - error
    """
    SUCCEEDED = 'succeeded'
    DECLINED = 'declined'
    ERROR = 'error'