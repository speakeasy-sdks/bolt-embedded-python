# SavedPaymentViewAction

Action after initializing payment


## Fields

| Field                                   | Type                                    | Required                                | Description                             | Example                                 |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `method`                                | *Optional[str]*                         | :heavy_minus_sign:                      | action method                           | POST                                    |
| `type`                                  | *Optional[str]*                         | :heavy_minus_sign:                      | action type                             | finalize                                |
| `url`                                   | *Optional[str]*                         | :heavy_minus_sign:                      | action URL                              | api.bolt.com/v1/payments/12345/finalize |