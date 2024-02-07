"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .amount_view import AmountView
from .capture_status import CaptureStatus
from .consumer_self_view import ConsumerSelfView
from .credit_card_authorization_view import CreditCardAuthorizationView
from .credit_card_capture_view import CreditCardCaptureView
from .credit_card_credit_view import CreditCardCreditView
from .credit_card_view import CreditCardView
from .merchant_division_summary_view import MerchantDivisionSummaryView
from .order_decision_details_view import OrderDecisionDetailsView
from .review_ticket_view import ReviewTicketView
from .risk_model_external_result_view import RiskModelExternalResultView
from .transaction_indemnification_decision import TransactionIndemnificationDecision
from .transaction_indemnification_reason import TransactionIndemnificationReason
from .transaction_processor import TransactionProcessor
from .transaction_splits_view import TransactionSplitsView
from .transaction_status import TransactionStatus
from .transaction_type import TransactionType
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional

class TransactionViewType(str, Enum):
    r"""Fee type options. **Nullable** for Transactions Details."""
    NET = 'net'
    PROCESSING_FEE = 'processing_fee'
    RISK_FEE = 'risk_fee'
    APM_FEE = 'apm_fee'
    NETWORK_FEE = 'network_fee'
    PLATFORM_FEE = 'platform_fee'
    BOLT_ACCOUNT_FEE = 'bolt_account_fee'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionViewSplits:
    r"""A split of fees by type and amount."""
    amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    type: Optional[TransactionViewType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Fee type options. **Nullable** for Transactions Details."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionViewCapture:
    r"""Deprecated. Use `captures`."""
    amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique ID for the capture. **Nullable** for Transactions Details."""
    merchant_event_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_event_id'), 'exclude': lambda f: f is None }})
    r"""The reference ID associated with a transaction event (auth, capture, refund, void). This is an arbitrary identifier created by the merchant. Bolt does not enforce any uniqueness constraints on this ID. It is up to the merchant to generate identifiers that properly fulfill its needs."""
    metadata: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""Additional information about the capture. For example, the processor capture ID. **Nullable** for Transactions Details."""
    splits: Optional[List[TransactionViewSplits]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('splits'), 'exclude': lambda f: f is None }})
    r"""A split of fees by type and amount. **Nullable** for Transactions Details."""
    status: Optional[CaptureStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the capture. **Nullable** for Transactions Details."""
    


class TransactionViewRiskReviewStatus(str, Enum):
    r"""Describes the current Risk Review status. A transaction could be unreviewed, reviewed, or pending manual review by the Bolt team."""
    UNKNOWN = 'unknown'
    NEEDS_REVIEW = 'needs_review'
    REVIEWED = 'reviewed'

class ViewStatus(str, Enum):
    NOT_VIEWED = 'not_viewed'
    VIEWED = 'viewed'
    VIEWING = 'viewing'

class TransactionViewCause(str, Enum):
    r"""Specifies why this particular transaction is voided."""
    MERCHANT_ACTION = 'merchant_action'
    PAYPAL_SYNC = 'paypal_sync'
    AMAZON_PAY_SYNC = 'amazon_pay_sync'
    IRREVERSIBLE_REJECT = 'irreversible_reject'
    AUTH_EXPIRE = 'auth_expire'
    AUTH_VERIFICATION_EXPIRED = 'auth_verification_expired'
    PAYMENT_METHOD_UPDATER = 'payment_method_updater'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class TransactionViewStatus(str, Enum):
    r"""The status of the void request."""
    SUCCEEDED = 'succeeded'
    DECLINED = 'declined'
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionViewVoid:
    cause: Optional[TransactionViewCause] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cause'), 'exclude': lambda f: f is None }})
    r"""Specifies why this particular transaction is voided."""
    merchant_event_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_event_id'), 'exclude': lambda f: f is None }})
    r"""The reference ID associated with a transaction event (auth, capture, refund, void). This is an arbitrary identifier created by the merchant. Bolt does not enforce any uniqueness constraints on this ID. It is up to the merchant to generate identifiers that properly fulfill its needs."""
    status: Optional[TransactionViewStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the void request."""
    void: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('void'), 'exclude': lambda f: f is None }})
    r"""The void ID returned from the payment processor."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionView:
    amount: Optional[AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    authorization: Optional[CreditCardAuthorizationView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization'), 'exclude': lambda f: f is None }})
    capture: Optional[TransactionViewCapture] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('capture'), 'exclude': lambda f: f is None }})
    r"""Deprecated. Use `captures`."""
    captures: Optional[List[CreditCardCaptureView]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('captures'), 'exclude': lambda f: f is None }})
    credit: Optional[CreditCardCreditView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit'), 'exclude': lambda f: f is None }})
    date_: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'exclude': lambda f: f is None }})
    r"""Transaction date. **Nullable** for Transactions Details."""
    from_consumer: Optional[ConsumerSelfView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_consumer'), 'exclude': lambda f: f is None }})
    from_credit_card: Optional[CreditCardView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_credit_card'), 'exclude': lambda f: f is None }})
    r"""Contains details about the credit card transaction."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique ID associated with the transaction. **Nullable** for Transactions Details."""
    indemnification_decision: Optional[TransactionIndemnificationDecision] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indemnification_decision'), 'exclude': lambda f: f is None }})
    r"""Describes whether the transaction is indemnified by Bolt for fraud."""
    indemnification_reason: Optional[TransactionIndemnificationReason] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indemnification_reason'), 'exclude': lambda f: f is None }})
    r"""Describes the reason that the transaction is or is not indemnified by Bolt for fraud."""
    last4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last4'), 'exclude': lambda f: f is None }})
    r"""The card's last 4 digits. **Nullable** for Transactions Details."""
    last_viewed_utc: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_viewed_utc'), 'exclude': lambda f: f is None }})
    merchant_division: Optional[MerchantDivisionSummaryView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_division'), 'exclude': lambda f: f is None }})
    merchant_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_order_number'), 'exclude': lambda f: f is None }})
    order_decision: Optional[OrderDecisionDetailsView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_decision'), 'exclude': lambda f: f is None }})
    processor: Optional[TransactionProcessor] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processor'), 'exclude': lambda f: f is None }})
    r"""The processor used. **Nullable** for Transactions Details."""
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    r"""The transaction's 12-digit Bolt reference ID. **Nullable** for Transactions Details."""
    review_ticket: Optional[ReviewTicketView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('review_ticket'), 'exclude': lambda f: f is None }})
    risk_insights: Optional[RiskModelExternalResultView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_insights'), 'exclude': lambda f: f is None }})
    risk_review_status: Optional[TransactionViewRiskReviewStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_review_status'), 'exclude': lambda f: f is None }})
    r"""Describes the current Risk Review status. A transaction could be unreviewed, reviewed, or pending manual review by the Bolt team."""
    risk_score: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_score'), 'exclude': lambda f: f is None }})
    splits: Optional[List[TransactionSplitsView]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('splits'), 'exclude': lambda f: f is None }})
    status: Optional[TransactionStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The transaction's status."""
    to_consumer: Optional[ConsumerSelfView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to_consumer'), 'exclude': lambda f: f is None }})
    to_credit_card: Optional[CreditCardView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to_credit_card'), 'exclude': lambda f: f is None }})
    r"""Contains details about the credit card transaction."""
    transaction_properties: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_properties'), 'exclude': lambda f: f is None }})
    type: Optional[TransactionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type of transaction."""
    view_status: Optional[ViewStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('view_status'), 'exclude': lambda f: f is None }})
    void: Optional[TransactionViewVoid] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('void'), 'exclude': lambda f: f is None }})
    

