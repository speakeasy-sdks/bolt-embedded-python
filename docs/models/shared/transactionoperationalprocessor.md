# TransactionOperationalProcessor


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `processor`                                                                     | [TransactionProcessor](../../models/shared/transactionprocessor.md)             | :heavy_check_mark:                                                              | The processor used. **Nullable** for Transactions Details.                      | adyen_gateway                                                                   |
| `status`                                                                        | [TransactionProcessorStatus](../../models/shared/transactionprocessorstatus.md) | :heavy_check_mark:                                                              | The processor's status. Only `primary` and `active` processor are displayed.    | primary                                                                         |