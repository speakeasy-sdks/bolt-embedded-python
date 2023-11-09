"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from bolt_embedded_api import utils
from bolt_embedded_api.models import errors, operations
from typing import Optional

class Testing:
    r"""A collection of endpoints that provide useful functionality to assist in testing your Bolt integration."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def create_testing_shopper_account(self, request: operations.CreateTestingShopperAccountRequest, security: operations.CreateTestingShopperAccountSecurity) -> operations.CreateTestingShopperAccountResponse:
        r"""Create Testing Shopper Account
        Create a Bolt shopper account for testing purposes. Available for sandbox use only and the created  account will be recycled after a certain time.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/testing/shopper/create'
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateTestingShopperAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateTestingShopperAccountResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_test_credit_card_token(self, security: operations.GetTestCreditCardTokenSecurity) -> operations.GetTestCreditCardTokenResponse:
        r"""Fetch a Test Credit Card Token
        This endpoint fetches a new credit card token for Bolt's universal test credit card number `4111 1111 1111 1004`. This is for testing and is available only in sandbox.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/testing/card_token'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTestCreditCardTokenResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetTestCreditCardTokenResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    