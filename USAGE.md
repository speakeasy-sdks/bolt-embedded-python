<!-- Start SDK Example Usage [usage] -->
```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AddAddressRequest(
    address_account=shared.AddressAccount(
        country_code='US',
        email='alan.watts@example.com',
        first_name='Alan',
        last_name='Watts',
        locality='Brooklyn',
        postal_code='10044',
        region='NY',
        street_address1='888 main street',
        company='Bolt',
        country='United States',
        door_code='123456',
        metadata=shared.Metadata(),
        name='Alan Watts',
        phone='+12125550199',
        region_code='NY',
        street_address2='apt 3021',
        street_address3='c/o Alicia Watts',
        street_address4='Bridge Street Apartment Building B',
    ),
)

res = s.account.add_address(req, operations.AddAddressSecurity(
    o_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    x_api_key="<YOUR_API_KEY_HERE>",
))

if res.object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->