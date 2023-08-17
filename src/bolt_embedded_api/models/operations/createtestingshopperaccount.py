"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import onev1_1testing_1shopper_1create_post_requestbody_content_application_1json_schema_properties_email_state as shared_onev1_1testing_1shopper_1create_post_requestbody_content_application_1json_schema_properties_email_state
from bolt_embedded_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional



@dataclasses.dataclass
class CreateTestingShopperAccountSecurity:
    x_api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    


class CreateTestingShopperAccountRequestBodyEmailState(str, Enum):
    r"""The status of the shopper account identifier (email or phone). If the account does not have this identifier, the status is \\"missing\\"; If the identifier has been used to receive an OTP code, the status is \\"verified\\"; If the identifier has not been used to receive an OTP code, the status is \\"unverified\\"."""
    MISSING = 'missing'
    VERIFIED = 'verified'
    UNVERIFIED = 'unverified'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateTestingShopperAccountRequestBody:
    deactivate_in_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deactivate_in_days'), 'exclude': lambda f: f is None }})
    r"""Number of days after which the test account is deactivated. Default: 30 days. Maximum: 180 days."""
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""Deprecated. Please leave this field absent and let the API automatically generate a random email."""
    email_state: Optional[CreateTestingShopperAccountRequestBodyEmailState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_state'), 'exclude': lambda f: f is None }})
    r"""The status of the shopper account identifier (email or phone). If the account does not have this identifier, the status is \\"missing\\"; If the identifier has been used to receive an OTP code, the status is \\"verified\\"; If the identifier has not been used to receive an OTP code, the status is \\"unverified\\"."""
    has_address: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_address'), 'exclude': lambda f: f is None }})
    r"""Add a random U.S. address to the created account if set to `true`"""
    migrated: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('migrated'), 'exclude': lambda f: f is None }})
    r"""Set this account as migrated by the merchant in the request"""
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""Deprecated. Please leave this field absent and let the API automatically generate a random phone number."""
    phone_state: Optional[shared_onev1_1testing_1shopper_1create_post_requestbody_content_application_1json_schema_properties_email_state.Onev11testing1shopper1createPostRequestBodyContentApplication1jsonSchemaPropertiesEmailState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_state'), 'exclude': lambda f: f is None }})
    r"""The status of the shopper account identifier (email or phone). If the account does not have this identifier, the status is \\"missing\\"; If the identifier has been used to receive an OTP code, the status is \\"verified\\"; If the identifier has not been used to receive an OTP code, the status is \\"unverified\\"."""
    




@dataclasses.dataclass
class CreateTestingShopperAccountRequest:
    request_body: Optional[CreateTestingShopperAccountRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    x_publishable_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Publishable-Key', 'style': 'simple', 'explode': False }})
    r"""The publicly viewable identifier used to identify a merchant division. This key is found in the Developer > API section of the Bolt Merchant Dashboard [RECOMMENDED]."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateTestingShopperAccount200ApplicationJSON:
    r"""Testing Account Created"""
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""An email address."""
    email_state: Optional[shared_onev1_1testing_1shopper_1create_post_requestbody_content_application_1json_schema_properties_email_state.Onev11testing1shopper1createPostRequestBodyContentApplication1jsonSchemaPropertiesEmailState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_state'), 'exclude': lambda f: f is None }})
    r"""The status of the shopper account identifier (email or phone). If the account does not have this identifier, the status is \\"missing\\"; If the identifier has been used to receive an OTP code, the status is \\"verified\\"; If the identifier has not been used to receive an OTP code, the status is \\"unverified\\"."""
    migrated_merchant_owner_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('migrated_merchant_owner_id'), 'exclude': lambda f: f is None }})
    r"""The merchant's public id if the account is migrated"""
    oauth_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauth_code'), 'exclude': lambda f: f is None }})
    r"""OAuth code that is associated with this account and can be used to exchange for an access token"""
    otp_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('otp_code'), 'exclude': lambda f: f is None }})
    r"""Fixed OTP code that can be used to login to the created account"""
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""A phone number following E164 standards, in its globalized format, i.e. prepended with a plus sign."""
    phone_state: Optional[shared_onev1_1testing_1shopper_1create_post_requestbody_content_application_1json_schema_properties_email_state.Onev11testing1shopper1createPostRequestBodyContentApplication1jsonSchemaPropertiesEmailState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_state'), 'exclude': lambda f: f is None }})
    r"""The status of the shopper account identifier (email or phone). If the account does not have this identifier, the status is \\"missing\\"; If the identifier has been used to receive an OTP code, the status is \\"verified\\"; If the identifier has not been used to receive an OTP code, the status is \\"unverified\\"."""
    will_deactivate_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('will_deactivate_at'), 'exclude': lambda f: f is None }})
    r"""The created testing account will be deactivated after this date"""
    




@dataclasses.dataclass
class CreateTestingShopperAccountResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_testing_shopper_account_200_application_json_object: Optional[CreateTestingShopperAccount200ApplicationJSON] = dataclasses.field(default=None)
    r"""Testing Account Created"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
