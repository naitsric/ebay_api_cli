import json

import requests
import xmltodict

from . import templates


class EbayAPI(object):
    def __init__(self):
        self.url = 'https://api.sandbox.ebay.com/ws/api.dll'
        self.headers = {
            'X-EBAY-API-CALL-NAME': None,
            'X-EBAY-API-APP-NAME': 'EchoBay62-5538-466c-b43b-662768d6841',
            'X-EBAY-API-CERT-NAME': '00dd08ab-2082-4e3c-9518-5f4298f296db',
            'X-EBAY-API-DEV-NAME': '16a26b1b-26cf-442d-906d-597b60c41c19',
            'X-EBAY-API-SITEID': '0',
            'X-EBAY-API-COMPATIBILITY-LEVEL': '861',
        }

    def get_categories(self):
        payload = templates.get_categories_payload
        headers = self.__set_header('GetCategories')
        r = requests.post(url=self.url, headers=headers, data=payload)
        return self.__to_dict(r.content)

    def get_bay_official_time(self):
        payload = templates.get_bay_official_time_payload
        headers = self.__set_header('GeteBayOfficialTime')
        r = requests.post(url=self.url, headers=headers, data=payload)
        return self.__to_dict(r.content)

    def __set_header(self, api_call_name):
        headers = self.headers
        headers['X-EBAY-API-CALL-NAME'] = api_call_name
        return headers

    @staticmethod
    def __to_dict(content):
        return json.loads(json.dumps(xmltodict.parse(content)))