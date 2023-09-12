# testing

## Overview

A collection of endpoints that provide useful functionality to assist in testing your Bolt integration.


### Available Operations

* [create_testing_shopper_account](#create_testing_shopper_account) - Create Testing Shopper Account
* [get_test_credit_card_token](#get_test_credit_card_token) - Fetch a Test Credit Card Token

## create_testing_shopper_account

Create a Bolt shopper account for testing purposes. Available for sandbox use only and the created  account will be recycled after a certain time.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.CreateTestingShopperAccountRequest(
    request_body=operations.CreateTestingShopperAccountRequestBody(
        deactivate_in_days=674848,
        email='Doyle71@yahoo.com',
        email_state=operations.CreateTestingShopperAccountRequestBodyEmailState.VERIFIED,
        has_address=False,
        migrated=False,
        phone='545.812.1141 x3790',
        phone_state=shared.Onev11testing1shopper1createPostRequestBodyContentApplication1jsonSchemaPropertiesEmailState.VERIFIED,
    ),
    x_publishable_key='cumque',
)

res = s.testing.create_testing_shopper_account(req, operations.CreateTestingShopperAccountSecurity(
    x_api_key="",
))

if res.create_testing_shopper_account_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.CreateTestingShopperAccountRequest](../../models/operations/createtestingshopperaccountrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.CreateTestingShopperAccountSecurity](../../models/operations/createtestingshopperaccountsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.CreateTestingShopperAccountResponse](../../models/operations/createtestingshopperaccountresponse.md)**


## get_test_credit_card_token

This endpoint fetches a new credit card token for Bolt's universal test credit card number `4111 1111 1111 1004`. This is for testing and is available only in sandbox.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()


res = s.testing.get_test_credit_card_token(operations.GetTestCreditCardTokenSecurity(
    x_api_key="",
))

if res.get_test_credit_card_token_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `security`                                                                                             | [operations.GetTestCreditCardTokenSecurity](../../models/operations/gettestcreditcardtokensecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.GetTestCreditCardTokenResponse](../../models/operations/gettestcreditcardtokenresponse.md)**

