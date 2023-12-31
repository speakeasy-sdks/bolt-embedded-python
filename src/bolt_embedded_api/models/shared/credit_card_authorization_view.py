"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .credit_card_authorization_reason import CreditCardAuthorizationReason
from .credit_card_authorization_status import CreditCardAuthorizationStatus
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, Optional

class AvsResponse(str, Enum):
    ZERO = '00'
    ONE = '01'
    TWO = '02'
    TEN = '10'
    ELEVEN = '11'
    TWELVE = '12'
    THIRTEEN = '13'
    FOURTEEN = '14'
    TWENTY = '20'
    THIRTY = '30'
    THIRTY_ONE = '31'
    THIRTY_TWO = '32'
    THIRTY_THREE = '33'
    THIRTY_FOUR = '34'
    FORTY = '40'
    ADYEN_ = 'adyen_'
    ADYEN_A = 'adyen_A'
    ADYEN_N = 'adyen_N'
    ADYEN_U = 'adyen_U'
    ADYEN_S = 'adyen_S'
    ADYEN_R = 'adyen_R'
    ADYEN_W = 'adyen_W'
    ADYEN_T = 'adyen_T'
    ADYEN_Z = 'adyen_Z'
    ADYEN_D = 'adyen_D'
    ADYEN_F = 'adyen_F'
    ADYEN_M = 'adyen_M'
    ADYEN_X = 'adyen_X'
    ADYEN_Y = 'adyen_Y'
    ADYEN_B = 'adyen_B'
    ADYEN_P = 'adyen_P'
    ADYEN_C = 'adyen_C'
    ADYEN_G = 'adyen_G'
    ADYEN_I = 'adyen_I'
    ADYEN_K = 'adyen_K'

class CvvResponse(str, Enum):
    M = 'M'
    N = 'N'
    P = 'P'
    S = 'S'
    U = 'U'
    D = 'D'
    X = 'X'
    Y = 'Y'
    ONE = '1'
    TWO = '2'
    THREE = '3'
    PASS = 'pass'
    FAIL = 'fail'
    UNAVAILABLE = 'unavailable'
    UNCHECKED = 'unchecked'
    BRAINTREE_M = 'braintree_M'
    BRAINTREE_N = 'braintree_N'
    BRAINTREE_U = 'braintree_U'
    BRAINTREE_B = 'braintree_B'
    BRAINTREE_A = 'braintree_A'
    BRAINTREE_I = 'braintree_I'
    BRAINTREE_S = 'braintree_S'
    CVV2 = 'CVV2'

class Processor(str, Enum):
    VANTIV = 'vantiv'
    ADYEN_PAYFAC = 'adyen_payfac'
    ADYEN_GATEWAY = 'adyen_gateway'
    STRIPE = 'stripe'
    BRAINTREE = 'braintree'
    CYBERSOURCE = 'cybersource'
    NMI = 'nmi'
    AUTHORIZE_NET = 'authorize_net'
    RADIAL = 'radial'
    SHOPIFY_PAYMENTS = 'shopify_payments'
    ROCKETGATE = 'rocketgate'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditCardAuthorizationView:
    auth: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth'), 'exclude': lambda f: f is None }})
    avs_response: Optional[AvsResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avs_response'), 'exclude': lambda f: f is None }})
    cvv_response: Optional[CvvResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cvv_response'), 'exclude': lambda f: f is None }})
    merchant_event_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_event_id'), 'exclude': lambda f: f is None }})
    r"""The reference ID associated with a transaction event (auth, capture, refund, void). This is an arbitrary identifier created by the merchant. Bolt does not enforce any uniqueness constraints on this ID. It is up to the merchant to generate identifiers that properly fulfill its needs."""
    metadata: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    processor: Optional[Processor] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processor'), 'exclude': lambda f: f is None }})
    reason: Optional[CreditCardAuthorizationReason] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reason'), 'exclude': lambda f: f is None }})
    r"""The reason code explaining the authorization status.
      * `1` - none
      * `2` - invalid_amount
      * `3` - invalid_cvv
      * `4` - invalid_cc_number
      * `5` - expired
      * `6` - risk
      * `7` - lost_stolen
      * `8` - call_issuer
      * `9` - invalid_merchant_for_card
      * `10` - unsupported_payment_method
    """
    status: Optional[CreditCardAuthorizationStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the authorization request.
      * `1` - succeeded
      * `2` - declined
      * `3` - error
    """
    

