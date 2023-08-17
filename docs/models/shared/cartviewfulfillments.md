# CartViewFulfillments


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `cart_shipment`                                                         | [Optional[ICartShipmentView]](../../models/shared/icartshipmentview.md) | :heavy_minus_sign:                                                      | N/A                                                                     |
| `fulfillment_type`                                                      | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `id`                                                                    | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `in_store_cart_shipment`                                                | [Optional[InStoreShipment2]](../../models/shared/instoreshipment2.md)   | :heavy_minus_sign:                                                      | A cart that is being prepared for shipment                              |
| `items`                                                                 | list[[ICartItemView](../../models/shared/icartitemview.md)]             | :heavy_minus_sign:                                                      | N/A                                                                     |