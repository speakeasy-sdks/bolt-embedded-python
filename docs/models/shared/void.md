# Void


## Fields

| Field                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cause`                                                                                                                                                                                                                                                                                     | [Optional[VoidCause]](../../models/shared/voidcause.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | Specifies why this particular transaction is voided.                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                             |
| `merchant_event_id`                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | The reference ID associated with a transaction event (auth, capture, refund, void). This is an arbitrary identifier created by the merchant. Bolt does not enforce any uniqueness constraints on this ID. It is up to the merchant to generate identifiers that properly fulfill its needs. | dbe0cd5d-3261-41d9-ba61-49e5b9d07567                                                                                                                                                                                                                                                        |
| `status`                                                                                                                                                                                                                                                                                    | [Optional[VoidStatus]](../../models/shared/voidstatus.md)                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | The status of the void request.                                                                                                                                                                                                                                                             | succeeded                                                                                                                                                                                                                                                                                   |
| `void`                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                          | The void ID returned from the payment processor.                                                                                                                                                                                                                                            | 123456                                                                                                                                                                                                                                                                                      |