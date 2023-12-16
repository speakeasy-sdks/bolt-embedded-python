# PaypalPaymentViewSchemas


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `action`                                                         | [Optional[operations.Action]](../../models/operations/action.md) | :heavy_minus_sign:                                               | Action after initializing payment                                |
| `id`                                                             | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The ID for a Payment Attempt                                     |
| `status`                                                         | [Optional[operations.Status]](../../models/operations/status.md) | :heavy_minus_sign:                                               | The current payment status.                                      |