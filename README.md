# bolt-embedded-api

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/bolt-embedded-python.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AddAddressRequest()

res = s.account.add_address(req, operations.AddAddressSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
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

### [transactions](docs/sdks/transactions/README.md)

* [authorize_transaction](docs/sdks/transactions/README.md#authorize_transaction) - Authorize a Card
* [capture_transaction](docs/sdks/transactions/README.md#capture_transaction) - Capture a Transaction
* [get_transaction_details](docs/sdks/transactions/README.md#get_transaction_details) - Transaction Details
* [refund_transaction](docs/sdks/transactions/README.md#refund_transaction) - Refund a Transaction
* [update_transaction](docs/sdks/transactions/README.md#update_transaction) - Update a Transaction
* [void_transaction](docs/sdks/transactions/README.md#void_transaction) - Void a Transaction

### [o_auth](docs/sdks/oauth/README.md)

* [o_auth_token](docs/sdks/oauth/README.md#o_auth_token) - OAuth Token Endpoint

### [payments](docs/sdks/payments/README.md)

* [finalize_payment](docs/sdks/payments/README.md#finalize_payment) - Finalize Payment
* [initialize_payment](docs/sdks/payments/README.md#initialize_payment) - Initialize Payment
* [update_payment](docs/sdks/payments/README.md#update_payment) - Update Payment

### [testing](docs/sdks/testing/README.md)

* [create_testing_shopper_account](docs/sdks/testing/README.md#create_testing_shopper_account) - Create Testing Shopper Account
* [get_test_credit_card_token](docs/sdks/testing/README.md#get_test_credit_card_token) - Fetch a Test Credit Card Token
<!-- End Available Resources and Operations [operations] -->







<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorsBoltAPIResponse | 403,404                      | application/json             |
| errors.SDKError              | 4x-5xx                       | */*                          |

### Example

```python
import bolt_embedded_api
from bolt_embedded_api.models import errors, operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.DeletePaymentMethodRequest(
    payment_method_id='<value>',
)

res = None
try:
    res = s.account.delete_payment_method(req, operations.DeletePaymentMethodSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))
except errors.ErrorsBoltAPIResponse as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.bolt.com` | None |
| 1 | `https://api-sandbox.bolt.com` | None |
| 2 | `https://api-staging.bolt.com` | None |

#### Example

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI(
    server_idx=2,
)

req = operations.AddAddressRequest()

res = s.account.add_address(req, operations.AddAddressSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.object is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI(
    server_url="https://api.bolt.com",
)

req = operations.AddAddressRequest()

res = s.account.add_address(req, operations.AddAddressSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.object is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import bolt_embedded_api
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = bolt_embedded_api.BoltEmbeddedAPI(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name         | Type         | Scheme       |
| ------------ | ------------ | ------------ |
| `o_auth`     | oauth2       | OAuth2 token |
| `x_api_key`  | apiKey       | API key      |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI(
    security=shared.Security(
        o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateAccountRequest()

res = s.account.create_account(req)

if res.account_details is not None:
    # handle response
    pass

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AddAddressRequest()

res = s.account.add_address(req, operations.AddAddressSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.object is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
