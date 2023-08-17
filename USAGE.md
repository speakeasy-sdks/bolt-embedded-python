<!-- Start SDK Example Usage -->


```python
import bolt_embedded_api
from bolt_embedded_api.models import operations, shared

s = bolt_embedded_api.BoltEmbeddedAPI()

req = operations.AddAddressRequest(
    idempotency_key='corrupti',
    x_publishable_key='provident',
    address_account=shared.AddressAccount(
        company='Bolt',
        country='United States',
        country_code='US',
        default=False,
        door_code='123456',
        email='alan.watts@example.com',
        first_name='Alan',
        last_name='Watts',
        locality='Brooklyn',
        metadata=shared.Metadata(
            additional_properties='distinctio',
        ),
        name='Alan Watts',
        phone='+12125550199',
        postal_code='10044',
        region='NY',
        region_code='NY',
        street_address1='888 main street',
        street_address2='apt 3021',
        street_address3='c/o Alicia Watts',
        street_address4='Bridge Street Apartment Building B',
    ),
)

res = s.account.add_address(req, operations.AddAddressSecurity(
    o_auth="",
    x_api_key="",
))

if res.add_address_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->