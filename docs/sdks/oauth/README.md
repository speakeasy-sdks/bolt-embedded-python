# OAuth
(*o_auth*)

## Overview

Interact with Shopper data by completing the Bolt OAuth process.


### Available Operations

* [o_auth_token](#o_auth_token) - OAuth Token Endpoint

## o_auth_token

Endpoint for receiving access, ID, and refresh tokens from Bolt's OAuth server. 

To use this endpoint, first use the Authorization Code Request flow by using the `authorization_code` Grant Type (`grant_type`). Then, in the event that you would need a second or subsequent code, use the `refresh_token` value returned from a successful request as the `refresh_token` input value in your subsequent `refresh_token` Grant Type (`grant_type`) request.

 **Reminder - the Content-Type of this request must be application/x-www-form-urlencoded**


### Example Usage

```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI(
    security=shared.Security(
        o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.OAuthTokenRequest(
    request_body=shared.OAuthTokenInput(
    client_id='string',
    client_secret='string',
    code='string',
    grant_type=shared.GrantType.AUTHORIZATION_CODE,
    scope=shared.Scope.OPENID,
),
)

res = s.o_auth.o_auth_token(req)

if res.o_auth_token_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.OAuthTokenRequest](../../models/operations/oauthtokenrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.OAuthTokenResponse](../../models/operations/oauthtokenresponse.md)**
### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorsOauthServerResponse | 400,403,422                      | application/json                 |
| errors.SDKError                  | 400-600                          | */*                              |
