# transactions

## Overview

Authorize credit card transactions and perform operations on those transactions with Bolt's transaction API.


### Available Operations

* [authorize_transaction](#authorize_transaction) - Authorize a Card
* [capture_transaction](#capture_transaction) - Capture a Transaction
* [get_transaction_details](#get_transaction_details) - Transaction Details
* [refund_transaction](#refund_transaction) - Refund a Transaction
* [update_transaction](#update_transaction) - Update a Transaction
* [void_transaction](#void_transaction) - Void a Transaction

## authorize_transaction

This endpoint authorizes card payments and has three main use cases:
* • Authorize a payment using an unsaved payment method for a guest or logged-in shopper.
* • Authorize a payment using a saved payment method for a logged-in shopper.
*  • Re-charge a previous transaction using the `credit_card_id` of the transaction.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AuthorizeTransactionRequest(
    idempotency_key='soluta',
    request_body=shared.MerchantCreditCardAuthorizationRecharge(
        auto_capture=False,
        cart=shared.CartCreate(
            add_ons=[
                shared.CartAddOn(
                    description='et',
                    image_url='saepe',
                    name='Carolyn Rohan',
                    price=5844.76,
                    product_id='aperiam',
                    product_page_url='delectus',
                ),
            ],
            billing_address=shared.Address(
                company='Bolt',
                country='United States',
                country_code='US',
                default=True,
                door_code='123456',
                email='alan.watts@example.com',
                first_name='Alan',
                last_name='Watts',
                locality='Brooklyn',
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
            cart_url='https://boltswagstore.com/orders/123456765432',
            currency='USD',
            discounts=[
                shared.CartDiscount(
                    amount=100,
                    code='SUMMER10DISCOUNT',
                    description='10% off our summer collection',
                    details_url='https://boltswagstore.com/SUMMERSALE',
                    discount_category=shared.CartDiscountDiscountCategory.MANAGED_GIFTCARD,
                    reference='DISC-1234',
                    type=shared.CartDiscountType.PERCENTAGE,
                ),
            ],
            display_id='displayid_100',
            fees=[
                shared.CartCreateFees(
                    description='Item Fee',
                    name='Item Fee',
                    quantity=2921.47,
                    reference='ItemFee',
                    unit_price=2869.15,
                    unit_tax_amount=2408.29,
                ),
            ],
            fulfillments=[
                shared.CartCreateFulfillments(
                    cart_items=[
                        shared.CartItem(
                            brand='Bolt',
                            category='bags',
                            collections=[
                                'summer',
                            ],
                            color='Bolt Blue',
                            customizations=[
                                shared.CartItemCustomization(
                                    attributes={
                                        "dolorum": 'architecto',
                                    },
                                    name='Margaret Luettgen MD',
                                    price=shared.AmountView(
                                        amount=754,
                                        currency='USD',
                                        currency_symbol='$',
                                    ),
                                ),
                            ],
                            description='Large tote with Bolt logo.',
                            details_url='https://boltswagstore.com/products/123456',
                            external_inputs=shared.ICartItemExternalInputs(
                                shopify_line_item_reference=8330.38,
                                shopify_product_reference=7851.53,
                                shopify_product_variant_reference=9843.3,
                            ),
                            gift_option=shared.CartItemGiftOption(
                                cost=770,
                                merchant_product_id='881',
                                message='Happy Anniversary, Smoochy Poo!',
                                wrap=False,
                            ),
                            image_url='https://boltswagstore.com/products/123456/images/1.png',
                            isbn='9780091347314',
                            item_group='ut',
                            manufacturer='Bolt Textiles USA',
                            merchant_product_id='881',
                            merchant_variant_id='888',
                            msrp=7034.95,
                            name='Bolt Swag Bag',
                            options='Special Edition',
                            properties=[
                                shared.CartItemProperty(
                                    color='cupiditate',
                                    display=False,
                                    name='Amy Langworth',
                                    name_id=9774.96,
                                    value='quisquam',
                                    value_id=8765.06,
                                ),
                            ],
                            quantity=1,
                            reference='item_100',
                            shipment=shared.CartShipment(
                                carrier='FedEx',
                                cost=770,
                                discounted_by_membership=False,
                                estimated_delivery_date='08-30-2022',
                                expedited=False,
                                package_depth=90,
                                package_dimension_unit='cm',
                                package_height=103,
                                package_type='A big package.',
                                package_weight_unit='kg',
                                package_width=222,
                                service='Option 1',
                                shipping_address=shared.Address(
                                    company='Bolt',
                                    country='United States',
                                    country_code='US',
                                    default=True,
                                    door_code='123456',
                                    email='alan.watts@example.com',
                                    first_name='Alan',
                                    last_name='Watts',
                                    locality='Brooklyn',
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
                                shipping_address_id='addres-1',
                                shipping_method='Unknown',
                                signature='a1B2s3dC4f5g5D6hj6E7k8F9l0',
                                tax_amount=230,
                                tax_code='tax-12345',
                                total_weight=55,
                                total_weight_unit='kg',
                                type=shared.CartShipmentType.DOOR_DELIVERY,
                            ),
                            shipment_type=shared.CartItemShipmentType.SHIP_TO_STORE,
                            size='Large',
                            sku='BOLT-SKU_100',
                            source='quis',
                            tags='tote, blue, linen, eco-friendly',
                            tax_amount=0,
                            tax_code='ipsum',
                            taxable=False,
                            total_amount=1000,
                            type=shared.CartItemType.BUNDLED,
                            unit_price=1000,
                            uom='inches',
                            upc='825764603119',
                            weight=10,
                            weight_unit='pounds',
                        ),
                    ],
                    cart_shipment=shared.CartShipment(
                        carrier='FedEx',
                        cost=770,
                        discounted_by_membership=False,
                        estimated_delivery_date='08-30-2022',
                        expedited=False,
                        package_depth=90,
                        package_dimension_unit='cm',
                        package_height=103,
                        package_type='A big package.',
                        package_weight_unit='kg',
                        package_width=222,
                        service='Option 1',
                        shipping_address=shared.Address(
                            company='Bolt',
                            country='United States',
                            country_code='US',
                            default=True,
                            door_code='123456',
                            email='alan.watts@example.com',
                            first_name='Alan',
                            last_name='Watts',
                            locality='Brooklyn',
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
                        shipping_address_id='addres-1',
                        shipping_method='Unknown',
                        signature='a1B2s3dC4f5g5D6hj6E7k8F9l0',
                        tax_amount=230,
                        tax_code='tax-12345',
                        total_weight=55,
                        total_weight_unit='kg',
                        type=shared.CartShipmentType.DOOR_DELIVERY,
                    ),
                    digital_delivery=shared.CartCreateFulfillmentsDigitalDelivery(
                        email='Dario.Thiel94@yahoo.com',
                        phone='846.784.2881 x6709',
                    ),
                    in_store_cart_shipment=shared.InStoreCartShipment(
                        cart_shipment=shared.CartShipment(
                            carrier='FedEx',
                            cost=770,
                            discounted_by_membership=False,
                            estimated_delivery_date='08-30-2022',
                            expedited=False,
                            package_depth=90,
                            package_dimension_unit='cm',
                            package_height=103,
                            package_type='A big package.',
                            package_weight_unit='kg',
                            package_width=222,
                            service='Option 1',
                            shipping_address=shared.Address(
                                company='Bolt',
                                country='United States',
                                country_code='US',
                                default=True,
                                door_code='123456',
                                email='alan.watts@example.com',
                                first_name='Alan',
                                last_name='Watts',
                                locality='Brooklyn',
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
                            shipping_address_id='addres-1',
                            shipping_method='Unknown',
                            signature='a1B2s3dC4f5g5D6hj6E7k8F9l0',
                            tax_amount=230,
                            tax_code='tax-12345',
                            total_weight=55,
                            total_weight_unit='kg',
                            type=shared.CartShipmentType.DOOR_DELIVERY,
                        ),
                        description='Pick up in-store at 123 Main St.',
                        distance=3,
                        distance_unit=shared.InStoreCartShipmentDistanceUnit.MILE,
                        in_store_pickup_address=shared.Address(
                            company='Bolt',
                            country='United States',
                            country_code='US',
                            default=True,
                            door_code='123456',
                            email='alan.watts@example.com',
                            first_name='Alan',
                            last_name='Watts',
                            locality='Brooklyn',
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
                        pickup_window_close=347233,
                        pickup_window_open=862310,
                        store_name='Bolt Collective',
                    ),
                    type=shared.CartCreateFulfillmentsType.PHYSICAL_DOOR_DELIVERY,
                ),
            ],
            in_store_cart_shipments=[
                shared.InStoreCartShipment(
                    cart_shipment=shared.CartShipment(
                        carrier='FedEx',
                        cost=770,
                        discounted_by_membership=False,
                        estimated_delivery_date='08-30-2022',
                        expedited=False,
                        package_depth=90,
                        package_dimension_unit='cm',
                        package_height=103,
                        package_type='A big package.',
                        package_weight_unit='kg',
                        package_width=222,
                        service='Option 1',
                        shipping_address=shared.Address(
                            company='Bolt',
                            country='United States',
                            country_code='US',
                            default=True,
                            door_code='123456',
                            email='alan.watts@example.com',
                            first_name='Alan',
                            last_name='Watts',
                            locality='Brooklyn',
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
                        shipping_address_id='addres-1',
                        shipping_method='Unknown',
                        signature='a1B2s3dC4f5g5D6hj6E7k8F9l0',
                        tax_amount=230,
                        tax_code='tax-12345',
                        total_weight=55,
                        total_weight_unit='kg',
                        type=shared.CartShipmentType.DOOR_DELIVERY,
                    ),
                    description='Pick up in-store at 123 Main St.',
                    distance=3,
                    distance_unit=shared.InStoreCartShipmentDistanceUnit.MILE,
                    in_store_pickup_address=shared.Address(
                        company='Bolt',
                        country='United States',
                        country_code='US',
                        default=True,
                        door_code='123456',
                        email='alan.watts@example.com',
                        first_name='Alan',
                        last_name='Watts',
                        locality='Brooklyn',
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
                    pickup_window_close=780427,
                    pickup_window_open=981830,
                    store_name='Bolt Collective',
                ),
            ],
            items=[
                shared.CartItem(
                    brand='Bolt',
                    category='bags',
                    collections=[
                        'summer',
                    ],
                    color='Bolt Blue',
                    customizations=[
                        shared.CartItemCustomization(
                            attributes={
                                "doloribus": 'iusto',
                            },
                            name='Kurt Abernathy',
                            price=shared.AmountView(
                                amount=754,
                                currency='USD',
                                currency_symbol='$',
                            ),
                        ),
                    ],
                    description='Large tote with Bolt logo.',
                    details_url='https://boltswagstore.com/products/123456',
                    external_inputs=shared.ICartItemExternalInputs(
                        shopify_line_item_reference=3685.84,
                        shopify_product_reference=4104.92,
                        shopify_product_variant_reference=1369,
                    ),
                    gift_option=shared.CartItemGiftOption(
                        cost=770,
                        merchant_product_id='881',
                        message='Happy Anniversary, Smoochy Poo!',
                        wrap=False,
                    ),
                    image_url='https://boltswagstore.com/products/123456/images/1.png',
                    isbn='9780091347314',
                    item_group='vel',
                    manufacturer='Bolt Textiles USA',
                    merchant_product_id='881',
                    merchant_variant_id='888',
                    msrp=8221.18,
                    name='Bolt Swag Bag',
                    options='Special Edition',
                    properties=[
                        shared.CartItemProperty(
                            color='magnam',
                            display=False,
                            name='Mrs. Vicki Langosh',
                            name_id=978.44,
                            value='ex',
                            value_id=8621.92,
                        ),
                    ],
                    quantity=1,
                    reference='item_100',
                    shipment=shared.CartShipment(
                        carrier='FedEx',
                        cost=770,
                        discounted_by_membership=False,
                        estimated_delivery_date='08-30-2022',
                        expedited=False,
                        package_depth=90,
                        package_dimension_unit='cm',
                        package_height=103,
                        package_type='A big package.',
                        package_weight_unit='kg',
                        package_width=222,
                        service='Option 1',
                        shipping_address=shared.Address(
                            company='Bolt',
                            country='United States',
                            country_code='US',
                            default=True,
                            door_code='123456',
                            email='alan.watts@example.com',
                            first_name='Alan',
                            last_name='Watts',
                            locality='Brooklyn',
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
                        shipping_address_id='addres-1',
                        shipping_method='Unknown',
                        signature='a1B2s3dC4f5g5D6hj6E7k8F9l0',
                        tax_amount=230,
                        tax_code='tax-12345',
                        total_weight=55,
                        total_weight_unit='kg',
                        type=shared.CartShipmentType.DOOR_DELIVERY,
                    ),
                    shipment_type=shared.CartItemShipmentType.SHIP_TO_STORE,
                    size='Large',
                    sku='BOLT-SKU_100',
                    source='voluptatibus',
                    tags='tote, blue, linen, eco-friendly',
                    tax_amount=0,
                    tax_code='nostrum',
                    taxable=False,
                    total_amount=1000,
                    type=shared.CartItemType.BUNDLED,
                    unit_price=1000,
                    uom='inches',
                    upc='825764603119',
                    weight=10,
                    weight_unit='pounds',
                ),
            ],
            loyalty_rewards=[
                shared.CartLoyaltyRewards(
                    amount=7888.73,
                    coupon_code='saepe',
                    description='$5 off (100 Points)',
                    details='{"id": 123456, "icon": "fa-dollar", "name": "$15.00 Off", "type": "Coupon", "amount": 100, "duration": "single_use", "cost_text": "150 Points",  "description": "Get $15 off your next purchase for 150 points", "discount_type": "fixed_amount", "unrendered_name": "$15.00 Off",  "discount_percentage": null, "discount_rate_cents": null, "discount_value_cents": null, "discount_amount_cents": 1500,  "unrendered_description": "Get $15 off your next purchase for 150 points", "applies_to_product_type": "ALL"}',
                    points=4113.72,
                    source='impedit',
                    type='corporis',
                ),
            ],
            metadata={
                "veniam": 'aliquid',
            },
            order_description='Order #1234567890',
            order_reference='order_100',
            shipments=[
                shared.CartShipment(
                    carrier='FedEx',
                    cost=770,
                    discounted_by_membership=False,
                    estimated_delivery_date='08-30-2022',
                    expedited=False,
                    package_depth=90,
                    package_dimension_unit='cm',
                    package_height=103,
                    package_type='A big package.',
                    package_weight_unit='kg',
                    package_width=222,
                    service='Option 1',
                    shipping_address=shared.Address(
                        company='Bolt',
                        country='United States',
                        country_code='US',
                        default=True,
                        door_code='123456',
                        email='alan.watts@example.com',
                        first_name='Alan',
                        last_name='Watts',
                        locality='Brooklyn',
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
                    shipping_address_id='addres-1',
                    shipping_method='Unknown',
                    signature='a1B2s3dC4f5g5D6hj6E7k8F9l0',
                    tax_amount=230,
                    tax_code='tax-12345',
                    total_weight=55,
                    total_weight_unit='kg',
                    type=shared.CartShipmentType.DOOR_DELIVERY,
                ),
            ],
            tax_amount=811.01,
            total_amount=900,
        ),
        credit_card_id='SAeEcU1hpMobc',
        division_id='4ab56ad7865ada4ad32',
        merchant_event_id='dbe0cd5d-3261-41d9-ba61-49e5b9d07567',
        previous_transaction_id='null',
        processing_initiator=shared.ProcessingInitiator.STORED_CARDHOLDER_INITIATED,
        shipping_address=shared.Address(
            company='Bolt',
            country='United States',
            country_code='US',
            default=True,
            door_code='123456',
            email='alan.watts@example.com',
            first_name='Alan',
            last_name='Watts',
            locality='Brooklyn',
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
        source=shared.MerchantCreditCardAuthorizationRechargeSource.DIRECT_PAYMENTS,
        user_identifier=shared.UserIdentifier(
            artifact='null',
            email='alan.watts@example.com',
            email_id='null',
            phone='+12125550199',
            phone_id='null',
        ),
        user_identity=shared.UserIdentity(
            first_name='Charlotte',
            last_name='Charles',
        ),
    ),
    x_publishable_key='magnam',
)

res = s.transactions.authorize_transaction(req, operations.AuthorizeTransactionSecurity(
    o_auth="",
    x_api_key="",
))

if res.i_authorize_result_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.AuthorizeTransactionRequest](../../models/operations/authorizetransactionrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.AuthorizeTransactionSecurity](../../models/operations/authorizetransactionsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.AuthorizeTransactionResponse](../../models/operations/authorizetransactionresponse.md)**


## capture_transaction

This captures funds for the designated transaction. A capture can be done for any partial amount or for the total authorized amount.

Although the response returns the standard `transaction_view` object, only `captures` and either `id` or `reference` are needed.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.CaptureTransactionRequest(
    idempotency_key='ea',
    capture_transaction_with_reference=shared.CaptureTransactionWithReference(
        amount=754,
        currency='USD',
        merchant_event_id='dbe0cd5d-3261-41d9-ba61-49e5b9d07567',
        skip_hook_notification=False,
        transaction_reference='LBLJ-TWW7-R9VC',
    ),
)

res = s.transactions.capture_transaction(req, operations.CaptureTransactionSecurity(
    x_api_key="",
))

if res.transaction_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CaptureTransactionRequest](../../models/operations/capturetransactionrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.CaptureTransactionSecurity](../../models/operations/capturetransactionsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.CaptureTransactionResponse](../../models/operations/capturetransactionresponse.md)**


## get_transaction_details

This allows you to pull the full transaction details for a given transaction.

 **Note**: All objects and fields marked `required` in the Transaction Details response are also **nullable**. This includes any sub-components (objects or fields) also marked `required`.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.GetTransactionDetailsRequest(
    reference='quo',
)

res = s.transactions.get_transaction_details(req, operations.GetTransactionDetailsSecurity(
    x_api_key="",
))

if res.get_transaction_details_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetTransactionDetailsRequest](../../models/operations/gettransactiondetailsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetTransactionDetailsSecurity](../../models/operations/gettransactiondetailssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetTransactionDetailsResponse](../../models/operations/gettransactiondetailsresponse.md)**


## refund_transaction

This refunds a captured transaction. Refunds can be done for any partial amount or for the total authorized amount. These refunds are processed synchronously and return information about the refunded transaction in the standard `transaction_view` object.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.RefundTransactionRequest(
    idempotency_key='consectetur',
    request_body=operations.RefundTransactionRequestBody(
        amount=754,
        currency='USD',
        merchant_event_id='dbe0cd5d-3261-41d9-ba61-49e5b9d07567',
        skip_hook_notification=False,
        transaction_reference='LBLJ-TWW7-R9VC',
    ),
)

res = s.transactions.refund_transaction(req, operations.RefundTransactionSecurity(
    x_api_key="",
))

if res.transaction_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RefundTransactionRequest](../../models/operations/refundtransactionrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RefundTransactionSecurity](../../models/operations/refundtransactionsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RefundTransactionResponse](../../models/operations/refundtransactionresponse.md)**


## update_transaction

This allows you to update certain transaction properties post-authorization.

### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.UpdateTransactionRequest(
    idempotency_key='recusandae',
    reference='aspernatur',
    request_body=operations.UpdateTransactionRequestBody(
        display_id='order-123',
        metadata={
            "minima": 'eaque',
        },
    ),
)

res = s.transactions.update_transaction(req, operations.UpdateTransactionSecurity(
    x_api_key="",
))

if res.update_transaction_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateTransactionRequest](../../models/operations/updatetransactionrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateTransactionSecurity](../../models/operations/updatetransactionsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateTransactionResponse](../../models/operations/updatetransactionresponse.md)**


## void_transaction

This voids the authorization for a given transaction. Voids must be completed before the authorization is captured.
In the request, either `transaction_id` or `transaction_reference` is required.
Although the response returns the standard `transaction_view` object, only `status` and either `id` or `reference` are needed.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.VoidTransactionRequest(
    idempotency_key='a',
    credit_card_void=shared.CreditCardVoid(
        merchant_event_id='dbe0cd5d-3261-41d9-ba61-49e5b9d07567',
        skip_hook_notification=False,
        transaction_reference='LBLJ-TWW7-R9VC',
    ),
)

res = s.transactions.void_transaction(req, operations.VoidTransactionSecurity(
    x_api_key="",
))

if res.transaction_view is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.VoidTransactionRequest](../../models/operations/voidtransactionrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.VoidTransactionSecurity](../../models/operations/voidtransactionsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.VoidTransactionResponse](../../models/operations/voidtransactionresponse.md)**

