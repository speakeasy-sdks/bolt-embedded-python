# FinalizePaymentRequestBodyShopperIdentity

Identification information for the Shopper


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `create_bolt_account`                                        | *Optional[bool]*                                             | :heavy_minus_sign:                                           | determines whether to create a bolt account for this shopper | true                                                         |
| `email`                                                      | *Optional[str]*                                              | :heavy_check_mark:                                           | Email address of the shopper                                 |                                                              |
| `first_name`                                                 | *Optional[str]*                                              | :heavy_check_mark:                                           | First name of the shopper                                    |                                                              |
| `last_name`                                                  | *Optional[str]*                                              | :heavy_check_mark:                                           | Last name of the shopper                                     |                                                              |
| `phone`                                                      | *Optional[str]*                                              | :heavy_check_mark:                                           | Phone number of the shopper                                  |                                                              |