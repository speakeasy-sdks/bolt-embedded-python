# Payments
(*payments*)

## Overview

Create and manage transactions for non credit card payments such as Paypal in your Embedded Accounts experience.


### Available Operations

* [finalize_payment](#finalize_payment) - Finalize Payment
* [initialize_payment](#initialize_payment) - Initialize Payment
* [update_payment](#update_payment) - Update Payment

## finalize_payment

Finalize a Bolt Payment. NOTE: The authorization header is NOT required for payments associated with users who do not have a Bolt account.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.FinalizePaymentRequest(
    request_body=operations.FinalizePaymentRequestBody(
        merchant_event_id='dbe0cd5d-3261-41d9-ba61-49e5b9d07567',
        shopper_identity=operations.ShopperIdentity(
            create_bolt_account=True,
            email='Shanon_Sipes@hotmail.com',
            first_name='Jalyn',
            last_name='Reichert',
            phone='567.701.8847 x69933',
        ),
    ),
    id='<ID>',
)

res = s.payments.finalize_payment(req, operations.FinalizePaymentSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
))

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.FinalizePaymentRequest](../../models/operations/finalizepaymentrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.FinalizePaymentSecurity](../../models/operations/finalizepaymentsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.FinalizePaymentResponse](../../models/operations/finalizepaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## initialize_payment

Initialize a Bolt payment token that will be used to reference this payment to Bolt when it is updated or finalized. NOTE: The authorization header is NOT required for payments associated with users who do not have a Bolt account.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.InitializePaymentRequest(
    request_body=operations.InitializePaymentRequestBody(
        cart=shared.CartCreate(
            add_ons=[
                shared.CartAddOn(
                    name='string',
                    price=3089.77,
                    product_id='string',
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
                    reference='DISC-1234',
                    type=shared.Type.PERCENTAGE,
                ),
            ],
            display_id='displayid_100',
            fees=[
                shared.Fees(
                    description='Item Fee',
                    name='Item Fee',
                    quantity=7673.67,
                    reference='ItemFee',
                    unit_price=7770.83,
                    unit_tax_amount=7895.06,
                ),
            ],
            fulfillments=[
                shared.Fulfillments(
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
                                        'key1': 'value1',
                                        'key2': 'value2',
                                    },
                                    price=shared.AmountView(
                                        amount=754,
                                        currency='USD',
                                        currency_symbol='$',
                                    ),
                                ),
                            ],
                            description='Large tote with Bolt logo.',
                            details_url='https://boltswagstore.com/products/123456',
                            external_inputs=shared.ICartItemExternalInputs(),
                            gift_option=shared.GiftOption(
                                cost=770,
                                merchant_product_id='881',
                                message='Happy Anniversary, Smoochy Poo!',
                                wrap=False,
                            ),
                            image_url='https://boltswagstore.com/products/123456/images/1.png',
                            isbn='9780091347314',
                            manufacturer='Bolt Textiles USA',
                            merchant_product_id='881',
                            merchant_variant_id='888',
                            name='Bolt Swag Bag',
                            options='Special Edition',
                            properties=[
                                shared.CartItemProperty(),
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
                            size='Large',
                            sku='BOLT-SKU_100',
                            tags='tote, blue, linen, eco-friendly',
                            tax_amount=0,
                            total_amount=1000,
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
                    digital_delivery=shared.DigitalDelivery(),
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
                        distance_unit=shared.DistanceUnit.MILE,
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
                        store_name='Bolt Collective',
                    ),
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
                    distance_unit=shared.DistanceUnit.MILE,
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
                                'key1': 'value1',
                                'key2': 'value2',
                            },
                            price=shared.AmountView(
                                amount=754,
                                currency='USD',
                                currency_symbol='$',
                            ),
                        ),
                    ],
                    description='Large tote with Bolt logo.',
                    details_url='https://boltswagstore.com/products/123456',
                    external_inputs=shared.ICartItemExternalInputs(),
                    gift_option=shared.GiftOption(
                        cost=770,
                        merchant_product_id='881',
                        message='Happy Anniversary, Smoochy Poo!',
                        wrap=False,
                    ),
                    image_url='https://boltswagstore.com/products/123456/images/1.png',
                    isbn='9780091347314',
                    manufacturer='Bolt Textiles USA',
                    merchant_product_id='881',
                    merchant_variant_id='888',
                    name='Bolt Swag Bag',
                    options='Special Edition',
                    properties=[
                        shared.CartItemProperty(),
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
                    size='Large',
                    sku='BOLT-SKU_100',
                    tags='tote, blue, linen, eco-friendly',
                    tax_amount=0,
                    total_amount=1000,
                    unit_price=1000,
                    uom='inches',
                    upc='825764603119',
                    weight=10,
                    weight_unit='pounds',
                ),
            ],
            loyalty_rewards=[
                shared.CartLoyaltyRewards(
                    description='$5 off (100 Points)',
                    details='{"id": 123456, "icon": "fa-dollar", "name": "$15.00 Off", "type": "Coupon", "amount": 100, "duration": "single_use", "cost_text": "150 Points",  "description": "Get $15 off your next purchase for 150 points", "discount_type": "fixed_amount", "unrendered_name": "$15.00 Off",  "discount_percentage": null, "discount_rate_cents": null, "discount_value_cents": null, "discount_amount_cents": 1500,  "unrendered_description": "Get $15 off your next purchase for 150 points", "applies_to_product_type": "ALL"}',
                ),
            ],
            metadata={
                'key1': 'value1',
                'key2': 'value2',
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
            total_amount=900,
        ),
        shopper_identity=operations.InitializePaymentShopperIdentity(
            create_bolt_account=True,
            email='Angelica40@gmail.com',
            first_name='Ottis',
            last_name='Bergnaum',
            phone='434-564-1598 x40879',
        ),
    ),
)

res = s.payments.initialize_payment(req, operations.InitializePaymentSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
))

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.InitializePaymentRequest](../../models/operations/initializepaymentrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.InitializePaymentSecurity](../../models/operations/initializepaymentsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.InitializePaymentResponse](../../models/operations/initializepaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_payment

Update a Bolt payment using the token given after initializing a payment.  Updates will completely replace the original top-level resource (for example, if a cart is sent in with the request it will replace the existing cart).  Any included object should be sent as complete object. NOTE: The authorization header is NOT required for payments associated with users who do not have a Bolt account.


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.UpdatePaymentRequest(
    request_body=operations.UpdatePaymentRequestBody(
        cart=shared.CartCreate(
            add_ons=[
                shared.CartAddOn(
                    name='string',
                    price=8194.81,
                    product_id='string',
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
                    reference='DISC-1234',
                    type=shared.Type.PERCENTAGE,
                ),
            ],
            display_id='displayid_100',
            fees=[
                shared.Fees(
                    description='Item Fee',
                    name='Item Fee',
                    quantity=1095.6,
                    reference='ItemFee',
                    unit_price=2053.88,
                    unit_tax_amount=4201.73,
                ),
            ],
            fulfillments=[
                shared.Fulfillments(
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
                                        'key1': 'value1',
                                        'key2': 'value2',
                                    },
                                    price=shared.AmountView(
                                        amount=754,
                                        currency='USD',
                                        currency_symbol='$',
                                    ),
                                ),
                            ],
                            description='Large tote with Bolt logo.',
                            details_url='https://boltswagstore.com/products/123456',
                            external_inputs=shared.ICartItemExternalInputs(),
                            gift_option=shared.GiftOption(
                                cost=770,
                                merchant_product_id='881',
                                message='Happy Anniversary, Smoochy Poo!',
                                wrap=False,
                            ),
                            image_url='https://boltswagstore.com/products/123456/images/1.png',
                            isbn='9780091347314',
                            manufacturer='Bolt Textiles USA',
                            merchant_product_id='881',
                            merchant_variant_id='888',
                            name='Bolt Swag Bag',
                            options='Special Edition',
                            properties=[
                                shared.CartItemProperty(),
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
                            size='Large',
                            sku='BOLT-SKU_100',
                            tags='tote, blue, linen, eco-friendly',
                            tax_amount=0,
                            total_amount=1000,
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
                    digital_delivery=shared.DigitalDelivery(),
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
                        distance_unit=shared.DistanceUnit.MILE,
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
                        store_name='Bolt Collective',
                    ),
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
                    distance_unit=shared.DistanceUnit.MILE,
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
                                'key1': 'value1',
                                'key2': 'value2',
                            },
                            price=shared.AmountView(
                                amount=754,
                                currency='USD',
                                currency_symbol='$',
                            ),
                        ),
                    ],
                    description='Large tote with Bolt logo.',
                    details_url='https://boltswagstore.com/products/123456',
                    external_inputs=shared.ICartItemExternalInputs(),
                    gift_option=shared.GiftOption(
                        cost=770,
                        merchant_product_id='881',
                        message='Happy Anniversary, Smoochy Poo!',
                        wrap=False,
                    ),
                    image_url='https://boltswagstore.com/products/123456/images/1.png',
                    isbn='9780091347314',
                    manufacturer='Bolt Textiles USA',
                    merchant_product_id='881',
                    merchant_variant_id='888',
                    name='Bolt Swag Bag',
                    options='Special Edition',
                    properties=[
                        shared.CartItemProperty(),
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
                    size='Large',
                    sku='BOLT-SKU_100',
                    tags='tote, blue, linen, eco-friendly',
                    tax_amount=0,
                    total_amount=1000,
                    unit_price=1000,
                    uom='inches',
                    upc='825764603119',
                    weight=10,
                    weight_unit='pounds',
                ),
            ],
            loyalty_rewards=[
                shared.CartLoyaltyRewards(
                    description='$5 off (100 Points)',
                    details='{"id": 123456, "icon": "fa-dollar", "name": "$15.00 Off", "type": "Coupon", "amount": 100, "duration": "single_use", "cost_text": "150 Points",  "description": "Get $15 off your next purchase for 150 points", "discount_type": "fixed_amount", "unrendered_name": "$15.00 Off",  "discount_percentage": null, "discount_rate_cents": null, "discount_value_cents": null, "discount_amount_cents": 1500,  "unrendered_description": "Get $15 off your next purchase for 150 points", "applies_to_product_type": "ALL"}',
                ),
            ],
            metadata={
                'key1': 'value1',
                'key2': 'value2',
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
            total_amount=900,
        ),
        shopper_identity=operations.UpdatePaymentShopperIdentity(
            create_bolt_account=True,
            email='Jannie.Kshlerin@yahoo.com',
            first_name='Adeline',
            last_name='Wyman',
            phone='358.969.1849 x6760',
        ),
    ),
    id='<ID>',
)

res = s.payments.update_payment(req, operations.UpdatePaymentSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
))

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdatePaymentRequest](../../models/operations/updatepaymentrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.UpdatePaymentSecurity](../../models/operations/updatepaymentsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.UpdatePaymentResponse](../../models/operations/updatepaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
