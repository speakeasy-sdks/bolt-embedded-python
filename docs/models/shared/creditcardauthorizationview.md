# CreditCardAuthorizationView


## Fields

| Field                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `auth`                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                        |
| `avs_response`                                                                                                                                                                                                                                                                                         | [Optional[CreditCardAuthorizationViewAvsResponse]](../../models/shared/creditcardauthorizationviewavsresponse.md)                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                        |
| `cvv_response`                                                                                                                                                                                                                                                                                         | [Optional[CreditCardAuthorizationViewCvvResponse]](../../models/shared/creditcardauthorizationviewcvvresponse.md)                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                        |
| `merchant_event_id`                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | The reference ID associated with a transaction event (auth, capture, refund, void). This is an arbitrary identifier created by the merchant. Bolt does not enforce any uniqueness constraints on this ID. It is up to the merchant to generate identifiers that properly fulfill its needs.            | dbe0cd5d-3261-41d9-ba61-49e5b9d07567                                                                                                                                                                                                                                                                   |
| `metadata`                                                                                                                                                                                                                                                                                             | dict[str, *str*]                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                        |
| `processor`                                                                                                                                                                                                                                                                                            | [Optional[CreditCardAuthorizationViewProcessor]](../../models/shared/creditcardauthorizationviewprocessor.md)                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                        |
| `reason`                                                                                                                                                                                                                                                                                               | [Optional[CreditCardAuthorizationReason]](../../models/shared/creditcardauthorizationreason.md)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | The reason code explaining the authorization status.<br/>  * `1` - none<br/>  * `2` - invalid_amount<br/>  * `3` - invalid_cvv<br/>  * `4` - invalid_cc_number<br/>  * `5` - expired<br/>  * `6` - risk<br/>  * `7` - lost_stolen<br/>  * `8` - call_issuer<br/>  * `9` - invalid_merchant_for_card<br/>  * `10` - unsupported_payment_method<br/> |                                                                                                                                                                                                                                                                                                        |
| `status`                                                                                                                                                                                                                                                                                               | [Optional[CreditCardAuthorizationStatus]](../../models/shared/creditcardauthorizationstatus.md)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | The status of the authorization request.<br/>  * `1` - succeeded<br/>  * `2` - declined<br/>  * `3` - error<br/>                                                                                                                                                                                       | succeeded                                                                                                                                                                                                                                                                                              |