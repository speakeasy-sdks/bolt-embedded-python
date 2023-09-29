# bolt-embedded-api

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/bolt-embedded-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AddAddressRequest(
    idempotency_key='Maserati Bespoke frictionless',
    x_publishable_key='deploy Central',
    address_account=shared.AddressAccount(
        company='Bolt',
        country='United States',
        country_code='US',
        default=False,
        door_code='123456',
        email='alan.watts@example.com',
        first_name='Alan',
        last_name='Watts',
        locality='Brooklyn',
        metadata=shared.Metadata(
            additional_properties='Loan Dollar',
        ),
        name='Alan Watts',
        phone='+12125550199',
        postal_code='10044',
        region='NY',
        region_code='NY',
        street_address1='888 main street',
        street_address2='apt 3021',
        street_address3='c/o Alicia Watts',
        street_address4='Bridge Street Apartment Building B',
    ),
)

res = s.account.add_address(req, operations.AddAddressSecurity(
    o_auth="",
    x_api_key="",
))

if res.add_address_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [account](docs/sdks/account/README.md)

* [add_address](docs/sdks/account/README.md#add_address) - Add Address
* [add_payment_method](docs/sdks/account/README.md#add_payment_method) - Add Payment Method
* [create_account](docs/sdks/account/README.md#create_account) - Create Bolt Account
* [delete_address](docs/sdks/account/README.md#delete_address) - Delete Address
* [delete_payment_method](docs/sdks/account/README.md#delete_payment_method) - Delete Payment Method
* [detect_account](docs/sdks/account/README.md#detect_account) - Detect Account
* [edit_address](docs/sdks/account/README.md#edit_address) - Edit Address
* [get_account](docs/sdks/account/README.md#get_account) - Get Account Details
* [replace_address](docs/sdks/account/README.md#replace_address) - Replace Address
* [update_account_profile](docs/sdks/account/README.md#update_account_profile) - Update Profile

### [o_auth](docs/sdks/oauth/README.md)

* [o_auth_token](docs/sdks/oauth/README.md#o_auth_token) - OAuth Token Endpoint

### [payments](docs/sdks/payments/README.md)

* [finalize_payment](docs/sdks/payments/README.md#finalize_payment) - Finalize Payment
* [initialize_payment](docs/sdks/payments/README.md#initialize_payment) - Initialize Payment
* [update_payment](docs/sdks/payments/README.md#update_payment) - Update Payment

### [testing](docs/sdks/testing/README.md)

* [create_testing_shopper_account](docs/sdks/testing/README.md#create_testing_shopper_account) - Create Testing Shopper Account
* [get_test_credit_card_token](docs/sdks/testing/README.md#get_test_credit_card_token) - Fetch a Test Credit Card Token

### [transactions](docs/sdks/transactions/README.md)

* [authorize_transaction](docs/sdks/transactions/README.md#authorize_transaction) - Authorize a Card
* [capture_transaction](docs/sdks/transactions/README.md#capture_transaction) - Capture a Transaction
* [get_transaction_details](docs/sdks/transactions/README.md#get_transaction_details) - Transaction Details
* [refund_transaction](docs/sdks/transactions/README.md#refund_transaction) - Refund a Transaction
* [update_transaction](docs/sdks/transactions/README.md#update_transaction) - Update a Transaction
* [void_transaction](docs/sdks/transactions/README.md#void_transaction) - Void a Transaction
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
