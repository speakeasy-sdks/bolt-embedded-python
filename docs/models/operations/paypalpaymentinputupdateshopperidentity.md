# PaypalPaymentInputUpdateShopperIdentity

Identification information for the Shopper. This is only required when creating a new Bolt account.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `email`                                                      | *str*                                                        | :heavy_check_mark:                                           | Email address of the shopper                                 |                                                              |
| `first_name`                                                 | *str*                                                        | :heavy_check_mark:                                           | First name of the shopper                                    |                                                              |
| `last_name`                                                  | *str*                                                        | :heavy_check_mark:                                           | Last name of the shopper                                     |                                                              |
| `phone`                                                      | *str*                                                        | :heavy_check_mark:                                           | Phone number of the shopper                                  |                                                              |
| `create_bolt_account`                                        | *Optional[bool]*                                             | :heavy_minus_sign:                                           | determines whether to create a bolt account for this shopper | true                                                         |