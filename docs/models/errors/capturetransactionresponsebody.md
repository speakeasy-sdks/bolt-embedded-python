# CaptureTransactionResponseBody

Unprocessable Entity


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | Raw HTTP response; suitable for custom response parsing                               |
| `errors`                                                                              | List[[errors.Errors](../../models/errors/errors.md)]                                  | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `result`                                                                              | [Optional[errors.Result]](../../models/errors/result.md)                              | :heavy_minus_sign:                                                                    | N/A                                                                                   |