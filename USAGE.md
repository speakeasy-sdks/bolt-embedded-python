<!-- Start SDK Example Usage [usage] -->
```python
import bolt_embedded_api
from bolt_embedded_api.models import operations

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AddAddressRequest()

res = s.account.add_address(req, operations.AddAddressSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->