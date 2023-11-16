# Fulfillments

Defines the shipments associated with the cart items.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `cart_items`                                                                       | List[[shared.CartItem](../../models/shared/cartitem.md)]                           | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `cart_shipment`                                                                    | [Optional[shared.CartShipment]](../../models/shared/cartshipment.md)               | :heavy_minus_sign:                                                                 | A cart that is being prepared for shipment                                         |
| `digital_delivery`                                                                 | [Optional[shared.DigitalDelivery]](../../models/shared/digitaldelivery.md)         | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `in_store_cart_shipment`                                                           | [Optional[shared.InStoreCartShipment]](../../models/shared/instorecartshipment.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `type`                                                                             | [Optional[shared.CartCreateType]](../../models/shared/cartcreatetype.md)           | :heavy_minus_sign:                                                                 | N/A                                                                                |