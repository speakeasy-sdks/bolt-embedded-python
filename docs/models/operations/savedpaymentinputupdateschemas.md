# SavedPaymentInputUpdateSchemas


## Fields

| Field                                                                                                                            | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `cart`                                                                                                                           | [Optional[shared.CartCreate]](../../models/shared/cartcreate.md)                                                                 | :heavy_minus_sign:                                                                                                               | The details of the cart being purchased with this payment.                                                                       |
| `payment_method`                                                                                                                 | [Optional[operations.SavedPaymentInputUpdatePaymentMethod]](../../models/operations/savedpaymentinputupdatepaymentmethod.md)     | :heavy_minus_sign:                                                                                                               | N/A                                                                                                                              |
| `shopper_identity`                                                                                                               | [Optional[operations.SavedPaymentInputUpdateShopperIdentity]](../../models/operations/savedpaymentinputupdateshopperidentity.md) | :heavy_minus_sign:                                                                                                               | Identification information for the Shopper. This is only required when creating a new Bolt account.                              |