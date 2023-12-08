# app/tests/test_ynab_api.py
from django.test import TestCase
import requests
import os


class YNABAPITest(TestCase):
    def test_ynab_api_connection(self):
        """ Test connection to the YNAB API """
        api_key = os.getenv('YNAB_API_KEY')
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get('https://api.ynab.com/v1/user', headers=headers)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Further checks can be added here, such as checking the structure of the response
