# app/utils/ynab_client.py
import requests
from django.conf import settings


class YNABClient:
    BASE_URL = "https://api.ynab.com/v1"

    def __init__(self, api_key=None):
        self.api_key = api_key or settings.YNAB_API_KEY

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }

    def fetch_transactions(self):
        url = f"{self.BASE_URL}/budgets/default/transactions"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()['data']['transactions']
        else:
            response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code

    # Add more methods as needed for different types of data
