"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import address_change_request_metadata_view as shared_address_change_request_metadata_view
from ..shared import amount_view as shared_amount_view
from ..shared import authorization_verification_status as shared_authorization_verification_status
from ..shared import capture as shared_capture
from ..shared import chargeback_details as shared_chargeback_details
from ..shared import consumer_self_view as shared_consumer_self_view
from ..shared import consumer_user_membership as shared_consumer_user_membership
from ..shared import credit as shared_credit
from ..shared import credit_card_authorization_view as shared_credit_card_authorization_view
from ..shared import credit_card_user as shared_credit_card_user
from ..shared import credit_card_view as shared_credit_card_view
from ..shared import custom_fields as shared_custom_fields
from ..shared import customer_list_status as shared_customer_list_status
from ..shared import errors_bolt_api_response as shared_errors_bolt_api_response
from ..shared import manual_disputes as shared_manual_disputes
from ..shared import merchant as shared_merchant
from ..shared import merchant_division as shared_merchant_division
from ..shared import order_decision as shared_order_decision
from ..shared import order_view as shared_order_view
from ..shared import review_ticket as shared_review_ticket
from ..shared import risk_insights_yml as shared_risk_insights_yml
from ..shared import risk_review_status as shared_risk_review_status
from ..shared import transaction_indemnification_decision as shared_transaction_indemnification_decision
from ..shared import transaction_indemnification_reason as shared_transaction_indemnification_reason
from ..shared import transaction_processor as shared_transaction_processor
from ..shared import transaction_status as shared_transaction_status
from ..shared import transaction_timeline_view as shared_transaction_timeline_view
from ..shared import transaction_type as shared_transaction_type
from ..shared import transaction_view as shared_transaction_view
from ..shared import void as shared_void
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional



@dataclasses.dataclass
class GetTransactionDetailsSecurity:
    x_api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    




@dataclasses.dataclass
class GetTransactionDetailsRequest:
    reference: str = dataclasses.field(metadata={'path_param': { 'field_name': 'REFERENCE', 'style': 'simple', 'explode': False }})
    r"""This is the Bolt transaction reference. (ex. N7Y3-NFKC-VFRF)"""
    


class GetTransactionDetails200ApplicationJSONSplitsType(str, Enum):
    r"""**Nullable** for Transactions Details."""
    NET = 'net'
    PROCESSING_FEE = 'processing_fee'
    BOLT_FEE = 'bolt_fee'
    ADJUSTMENT = 'adjustment'
    FLOAT = 'float'
    RESERVE = 'reserve'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetTransactionDetails200ApplicationJSONSplits:
    r"""A split of fees by type and amount."""
    amount: Optional[shared_amount_view.AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    type: Optional[GetTransactionDetails200ApplicationJSONSplitsType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""**Nullable** for Transactions Details."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetTransactionDetails200ApplicationJSONTransactionRejectionDetailsAuthRejectionDetails:
    reason_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reason_code'), 'exclude': lambda f: f is None }})
    reason_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reason_description'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetTransactionDetails200ApplicationJSONTransactionRejectionDetails:
    auth_rejection_details: Optional[GetTransactionDetails200ApplicationJSONTransactionRejectionDetailsAuthRejectionDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_rejection_details'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetTransactionDetails200ApplicationJSON:
    r"""Transaction Details Retrieved"""
    address_change_request_metadata: Optional[shared_address_change_request_metadata_view.AddressChangeRequestMetadataView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address_change_request_metadata'), 'exclude': lambda f: f is None }})
    adjust_transactions: Optional[list[shared_transaction_view.TransactionView]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('adjust_transactions'), 'exclude': lambda f: f is None }})
    r"""**Nullable** for Transactions Details."""
    amount: Optional[shared_amount_view.AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    auth_verification_status: Optional[shared_authorization_verification_status.AuthorizationVerificationStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_verification_status'), 'exclude': lambda f: f is None }})
    r"""Used to track the status of micro-authorizations. **Nullable** for Transactions Details."""
    authorization: Optional[shared_credit_card_authorization_view.CreditCardAuthorizationView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization'), 'exclude': lambda f: f is None }})
    authorization_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization_id'), 'exclude': lambda f: f is None }})
    r"""The authorization's id."""
    capture: Optional[shared_capture.Capture] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('capture'), 'exclude': lambda f: f is None }})
    r"""Deprecated. Use `captures`."""
    captures: Optional[list[shared_capture.Capture]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('captures'), 'exclude': lambda f: f is None }})
    r"""All captures associated with the transaction. **Nullable** for Transactions Details."""
    chargeback_details: Optional[shared_chargeback_details.ChargebackDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chargeback_details'), 'exclude': lambda f: f is None }})
    credit: Optional[shared_credit.Credit] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit'), 'exclude': lambda f: f is None }})
    custom_fields: Optional[shared_custom_fields.CustomFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_fields'), 'exclude': lambda f: f is None }})
    customer_list_status: Optional[shared_customer_list_status.CustomerListStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_list_status'), 'exclude': lambda f: f is None }})
    date_: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'exclude': lambda f: f is None }})
    r"""Transaction date. **Nullable** for Transactions Details."""
    from_consumer: Optional[shared_credit_card_user.CreditCardUser] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_consumer'), 'exclude': lambda f: f is None }})
    r"""The credit card user."""
    from_consumer_membership_users: Optional[shared_consumer_user_membership.ConsumerUserMembership] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_consumer_membership_users'), 'exclude': lambda f: f is None }})
    r"""**Nullable** for Transactions Details."""
    from_credit_card: Optional[shared_credit_card_view.CreditCardView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_credit_card'), 'exclude': lambda f: f is None }})
    r"""Contains details about the credit card transaction."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique ID associated with the transaction. **Nullable** for Transactions Details."""
    indemnification_decision: Optional[shared_transaction_indemnification_decision.TransactionIndemnificationDecision] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indemnification_decision'), 'exclude': lambda f: f is None }})
    r"""Describes whether the transaction is indemnified by Bolt for fraud."""
    indemnification_reason: Optional[shared_transaction_indemnification_reason.TransactionIndemnificationReason] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indemnification_reason'), 'exclude': lambda f: f is None }})
    r"""Describes the reason that the transaction is or is not indemnified by Bolt for fraud."""
    last_viewed_utc: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_viewed_utc'), 'exclude': lambda f: f is None }})
    r"""The last view time as UTC."""
    last4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last4'), 'exclude': lambda f: f is None }})
    r"""The card's last 4 digits. **Nullable** for Transactions Details."""
    manual_disputes: Optional[shared_manual_disputes.ManualDisputes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('manual_disputes'), 'exclude': lambda f: f is None }})
    merchant: Optional[shared_merchant.Merchant] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant'), 'exclude': lambda f: f is None }})
    merchant_division: Optional[shared_merchant_division.MerchantDivision] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_division'), 'exclude': lambda f: f is None }})
    merchant_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_order_number'), 'exclude': lambda f: f is None }})
    r"""The merchant's internal order number for this transaction."""
    order: Optional[shared_order_view.OrderView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order'), 'exclude': lambda f: f is None }})
    order_decision: Optional[shared_order_decision.OrderDecision] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_decision'), 'exclude': lambda f: f is None }})
    r"""Decision and score for an order."""
    platform_metadata: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('platform_metadata'), 'exclude': lambda f: f is None }})
    processor: Optional[shared_transaction_processor.TransactionProcessor] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processor'), 'exclude': lambda f: f is None }})
    r"""The processor used. **Nullable** for Transactions Details."""
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})
    r"""The transaction's 12-digit Bolt reference ID. **Nullable** for Transactions Details."""
    refund_transaction_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_transaction_ids'), 'exclude': lambda f: f is None }})
    r"""**Nullable** for Transactions Details."""
    refund_transactions: Optional[list[shared_transaction_view.TransactionView]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_transactions'), 'exclude': lambda f: f is None }})
    r"""**Nullable** for Transactions Details."""
    refunded_amount: Optional[shared_amount_view.AmountView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refunded_amount'), 'exclude': lambda f: f is None }})
    review_ticket: Optional[shared_review_ticket.ReviewTicket] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('review_ticket'), 'exclude': lambda f: f is None }})
    r"""Internal use only."""
    risk_insights: Optional[shared_risk_insights_yml.RiskInsightsYml] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_insights'), 'exclude': lambda f: f is None }})
    r"""Displays fraud decisioning insights based on key factors. This information can either be forwarded via a `risk_insights` transaction webhook type or be polled by sending a `GET` request to Bolt's [transactions endpoint](/api-bolt/#operation/transaction-details)."""
    risk_review_status: Optional[shared_risk_review_status.RiskReviewStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_review_status'), 'exclude': lambda f: f is None }})
    r"""Describes the current Risk Review status. A transaction could be unreviewed, reviewed, or pending manual review by the Bolt team."""
    risk_score: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_score'), 'exclude': lambda f: f is None }})
    source_transaction: Optional[shared_transaction_view.TransactionView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_transaction'), 'exclude': lambda f: f is None }})
    splits: Optional[list[GetTransactionDetails200ApplicationJSONSplits]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('splits'), 'exclude': lambda f: f is None }})
    r"""A list of splits. **Nullable** for Transactions Details."""
    status: Optional[shared_transaction_status.TransactionStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The transaction's status."""
    timeline: Optional[shared_transaction_timeline_view.TransactionTimelineView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeline'), 'exclude': lambda f: f is None }})
    to_consumer: Optional[shared_consumer_self_view.ConsumerSelfView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to_consumer'), 'exclude': lambda f: f is None }})
    to_credit_card: Optional[shared_credit_card_view.CreditCardView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to_credit_card'), 'exclude': lambda f: f is None }})
    r"""Contains details about the credit card transaction."""
    transaction_properties: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_properties'), 'exclude': lambda f: f is None }})
    transaction_rejection_details: Optional[GetTransactionDetails200ApplicationJSONTransactionRejectionDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_rejection_details'), 'exclude': lambda f: f is None }})
    type: Optional[shared_transaction_type.TransactionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type of transaction."""
    view_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('view_status'), 'exclude': lambda f: f is None }})
    void: Optional[shared_void.Void] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('void'), 'exclude': lambda f: f is None }})
    void_cause: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('void_cause'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetTransactionDetailsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    errors_bolt_api_response: Optional[shared_errors_bolt_api_response.ErrorsBoltAPIResponse] = dataclasses.field(default=None)
    r"""Generic Error Schema"""
    get_transaction_details_200_application_json_object: Optional[GetTransactionDetails200ApplicationJSON] = dataclasses.field(default=None)
    r"""Transaction Details Retrieved"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
