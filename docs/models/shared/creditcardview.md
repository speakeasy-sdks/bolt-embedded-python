# CreditCardView

Contains details about the credit card transaction.


## Fields

| Field                                                                                                                                                        | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  | Example                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `billing_address`                                                                                                                                            | [Optional[AddressView]](../../models/shared/addressview.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                           | The address object returned in the response.                                                                                                                 |                                                                                                                                                              |
| `bin`                                                                                                                                                        | *Optional[str]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | The Bank Identification Number for the credit card; this is typically the first 4-6 digits of the credit card number. **Nullable** for Transactions Details. | 402201                                                                                                                                                       |
| `display_network`                                                                                                                                            | [Optional[CardDisplayNetwork]](../../models/shared/carddisplaynetwork.md)                                                                                    | :heavy_minus_sign:                                                                                                                                           | The card's network. **Nullable** for Transactions Details.                                                                                                   | Visa                                                                                                                                                         |
| `expiration`                                                                                                                                                 | *Optional[int]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | The card's expiration. **Nullable** for Transactions Details.                                                                                                | 1654041600000                                                                                                                                                |
| `icon_asset_path`                                                                                                                                            | *Optional[str]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | The asset link for displayed icons. This link varies depending on payment method used.  **Nullable** for Transactions Details.                               | img/issuer-logos/visa.png                                                                                                                                    |
| `id`                                                                                                                                                         | *Optional[str]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | The card's ID. **Nullable** for Transactions Details.                                                                                                        | AB3rJKam5DhYE                                                                                                                                                |
| `last4`                                                                                                                                                      | *Optional[str]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | The card's last 4 digits. **Nullable** for Transactions Details.                                                                                             | 4021                                                                                                                                                         |
| `network`                                                                                                                                                    | [Optional[CardNetwork]](../../models/shared/cardnetwork.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                           | The card's network code. **Nullable** for Transactions Details. Note: LEGACY diners_club_us_ca now tagged as mastercard<br/>                                 | visa                                                                                                                                                         |
| `priority`                                                                                                                                                   | [Optional[Priority]](../../models/shared/priority.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                           | Describes the card's priority.<br/>                                                                                                                          | primary                                                                                                                                                      |
| `status`                                                                                                                                                     | [Optional[CardStatus]](../../models/shared/cardstatus.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                           | The card's status. **Nullable** for Transactions Details.                                                                                                    | active                                                                                                                                                       |
| `token`                                                                                                                                                      | *Optional[str]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | The Bolt token associated to the credit card. Required for new, unsaved cards.                                                                               | a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0                                                                                                                     |
| `token_type`                                                                                                                                                 | [Optional[CardTokenType]](../../models/shared/cardtokentype.md)                                                                                              | :heavy_minus_sign:                                                                                                                                           | Used to define which payment processor generated the token for this credit card.<br/>                                                                        | bolt                                                                                                                                                         |