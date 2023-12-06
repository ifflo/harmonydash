# app/utils/ynab_api.py
import requests
from django.conf import settings


def fetch_transactions():
    api_key = settings.YNAB_API_KEY
    headers = {'Authorization': f'Bearer {api_key}'}
    url = 'https://api.youneedabudget.com/v1/budgets/default/transactions'  # Example endpoint
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['transactions']
    else:
        # Handle error (e.g., log it, raise an exception, etc.)
        return None
