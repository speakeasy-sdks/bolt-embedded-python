"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address as shared_address
from ..shared import cart_create as shared_cart_create
from ..shared import credit_card as shared_credit_card
from ..shared import user_identifier as shared_user_identifier
from ..shared import user_identity as shared_user_identity
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class MerchantCreditCardAuthorizationProcessingInitiator(str, Enum):
    r"""Determines who initiated the transaction (e.g. shopper, merchant) and how they did it (e.g. recurring subscription, on-file card).

    * `initial_card_on_file` - The first transaction made for a card. The system then saves this card for future transactions.
    * `initial_recurring` - The first time any card is used to pay for a recurring charge. For example, a subscription.
    * `stored_cardholder_initiated` - The subsequent (second, third, etc.) transactions a shopper initiates with a stored card. This includes every situation during which a cardholder requests a charge, for example if the cardholder requests a merchant charge their card.
    * `stored_merchant_initiated` - The subsequent (second, third, etc.) transactions a merchant initiates with a stored card only when the cardholder does not request the charge. For example, when a customer service representative buys on behalf of a shopper or when a business adds funds to a public transit card.
    * `following_recurring` - The subsequent (second, third, etc.) transactions  a card is used to pay for a recurring charge. For example, a subscription.
    * `cardholder_initiated` - When a cardholder begins a transaction that isn’t stored in Bolt and won’t be stored in Bolt for future transactions.
    * `recurring` - Any time a card is used to pay for a recurring charge (for example, a subscription). Only use this value when you don’t know if it’s the first recurring charge.
    """
    INITIAL_CARD_ON_FILE = 'initial_card_on_file'
    INITIAL_RECURRING = 'initial_recurring'
    STORED_CARDHOLDER_INITIATED = 'stored_cardholder_initiated'
    STORED_MERCHANT_INITIATED = 'stored_merchant_initiated'
    FOLLOWING_RECURRING = 'following_recurring'
    CARDHOLDER_INITIATED = 'cardholder_initiated'
    RECURRING = 'recurring'

class MerchantCreditCardAuthorizationSource(str, Enum):
    DIRECT_PAYMENTS = 'direct_payments'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MerchantCreditCardAuthorization:
    r"""This request is used for authorizing a new, unsaved card."""
    cart: shared_cart_create.CartCreate = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cart') }})
    create_bolt_account: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('create_bolt_account') }})
    r"""If `true`, the guest shopper is provided a Bolt Account using their email address as its unique ID; if `false`, no information is saved at checkout."""
    credit_card: shared_credit_card.CreditCard = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_card') }})
    r"""The credit_card object is used to to pay for guest-checkout transactions or save payment method details to an account. Once saved, you can reference the credit card with the associated `credit_card_id` for future transactions. Add `billing_address` to this if storing a billing address for a returning shopper."""
    division_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('division_id') }})
    r"""The unique ID associated to the merchant's Bolt Account division; Merchants can have different divisions to suit multiple use cases (storefronts, pay-by-link, phone order processing). Use the Bolt Merchant Dashboard to switch between divisions and find the division ID under `Merchant Division Public ID`."""
    source: MerchantCreditCardAuthorizationSource = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    user_identifier: shared_user_identifier.UserIdentifier = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_identifier') }})
    r"""The object containing key lookup IDs associated with the shopper's account, such as the unique email address and phone number."""
    user_identity: shared_user_identity.UserIdentity = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_identity') }})
    auto_capture: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auto_capture'), 'exclude': lambda f: f is None }})
    merchant_event_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_event_id'), 'exclude': lambda f: f is None }})
    r"""The reference ID associated with a transaction event (auth, capture, refund, void). This is an arbitrary identifier created by the merchant. Bolt does not enforce any uniqueness constraints on this ID. It is up to the merchant to generate identifiers that properly fulfill its needs."""
    previous_transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous_transaction_id') }})
    r"""The unique ID associated with to the shopper's previous subscription-based transaction. Leave `null` for standard, non-subscription transactions."""
    processing_initiator: Optional[MerchantCreditCardAuthorizationProcessingInitiator] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processing_initiator'), 'exclude': lambda f: f is None }})
    r"""Determines who initiated the transaction (e.g. shopper, merchant) and how they did it (e.g. recurring subscription, on-file card).

    * `initial_card_on_file` - The first transaction made for a card. The system then saves this card for future transactions.
    * `initial_recurring` - The first time any card is used to pay for a recurring charge. For example, a subscription.
    * `stored_cardholder_initiated` - The subsequent (second, third, etc.) transactions a shopper initiates with a stored card. This includes every situation during which a cardholder requests a charge, for example if the cardholder requests a merchant charge their card.
    * `stored_merchant_initiated` - The subsequent (second, third, etc.) transactions a merchant initiates with a stored card only when the cardholder does not request the charge. For example, when a customer service representative buys on behalf of a shopper or when a business adds funds to a public transit card.
    * `following_recurring` - The subsequent (second, third, etc.) transactions  a card is used to pay for a recurring charge. For example, a subscription.
    * `cardholder_initiated` - When a cardholder begins a transaction that isn’t stored in Bolt and won’t be stored in Bolt for future transactions.
    * `recurring` - Any time a card is used to pay for a recurring charge (for example, a subscription). Only use this value when you don’t know if it’s the first recurring charge.
    """
    shipping_address: Optional[shared_address.Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_address'), 'exclude': lambda f: f is None }})
    r"""The Address object is used for billing, shipping, and physical store address use cases."""
    

