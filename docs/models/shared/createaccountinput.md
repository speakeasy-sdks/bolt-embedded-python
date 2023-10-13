# CreateAccountInput

The details needed to create a Bolt account.


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `addresses`                                                               | list[[AddressAccount](../../models/shared/addressaccount.md)]             | :heavy_minus_sign:                                                        | A list of physical shipping addresses associated with this account.       |
| `payment_methods`                                                         | list[[PaymentMethodAccount](../../models/shared/paymentmethodaccount.md)] | :heavy_minus_sign:                                                        | A list of payment methods associated with this account.                   |
| `profile`                                                                 | [Profile](../../models/shared/profile.md)                                 | :heavy_check_mark:                                                        | The first name, last name, email address, and phone number of a shopper.  |