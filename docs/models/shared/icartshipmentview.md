# ICartShipmentView


## Fields

| Field                                                                                                   | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `carrier`                                                                                               | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | The carrier used to deliver the shipment.                                                               | USPS                                                                                                    |
| `cost`                                                                                                  | [Optional[AmountView]](../../models/shared/amountview.md)                                               | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `default`                                                                                               | *Optional[bool]*                                                                                        | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `description`                                                                                           | list[[IDescriptionPart](../../models/shared/idescriptionpart.md)]                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `description_tooltips`                                                                                  | list[[IDescriptionTooltip](../../models/shared/idescriptiontooltip.md)]                                 | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `estimated_delivery_date`                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                    | :heavy_minus_sign:                                                                                      | N/A                                                                                                     | 2022-04-10T16:12:38.386Z                                                                                |
| `expedited`                                                                                             | *Optional[bool]*                                                                                        | :heavy_minus_sign:                                                                                      | Used to determine whether a shipment has been expedited or not.                                         |                                                                                                         |
| `gift_options`                                                                                          | [Optional[GiftOptionView]](../../models/shared/giftoptionview.md)                                       | :heavy_minus_sign:                                                                                      | Defines which gift options are hidden.                                                                  |                                                                                                         |
| `id`                                                                                                    | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `package_dimension`                                                                                     | [Optional[ICartShipmentViewPackageDimension]](../../models/shared/icartshipmentviewpackagedimension.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `package_type`                                                                                          | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `package_weight`                                                                                        | [Optional[IWeight]](../../models/shared/iweight.md)                                                     | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `reference`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `service`                                                                                               | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `shipping_address`                                                                                      | [Optional[AddressView]](../../models/shared/addressview.md)                                             | :heavy_minus_sign:                                                                                      | The address object returned in the response.                                                            |                                                                                                         |
| `shipping_method`                                                                                       | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `signature`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `tax_amount`                                                                                            | [Optional[AmountView]](../../models/shared/amountview.md)                                               | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `total_weight`                                                                                          | [Optional[IWeight]](../../models/shared/iweight.md)                                                     | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `type`                                                                                                  | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |                                                                                                         |