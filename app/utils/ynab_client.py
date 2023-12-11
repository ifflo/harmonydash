# app/utils/ynab_client.py
import requests
from urllib.parse import urljoin
from app.models import FinancialSettings


class YNABClient:
    def __init__(self, api_key):
        self.base_url = 'https://api.ynab.com/v1/'
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def sync_ynab_data(self):
        """Synchronize data from the YNAB API."""
        try:
            # Step 1: Fetch data from YNAB
            budgets = self.get_budgets()['data']['budgets']

            # Step 2: Process and integrate budgets into your Django models
            for budget in budgets:
                # Example: Update or create budget in your Django model
                # Adjust the logic based on how your models are set up
                FinancialSettings.objects.update_or_create(
                    budget_id=budget['id'],
                    defaults={
                        'budget_name': budget['name'],
                        # ... other fields if necessary ...
                    }
                )
            print("YNAB data synchronized successfully.")
        except Exception as e:
            # Step 3: Error Handling
            print(f"Error during YNAB data synchronization: {e}")

    def _get(self, endpoint):
        """Generic GET request handler."""
        url = urljoin(self.base_url, endpoint)
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint, data):
        """Generic POST request handler."""
        url = urljoin(self.base_url, endpoint)
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def _put(self, endpoint, data):
        """Generic PUT request handler."""
        url = urljoin(self.base_url, endpoint)
        response = requests.put(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def get_budgets(self):
        """Fetch all budgets."""
        return self._get('budgets')['data']['budgets']

    def get_budget_details(self, budget_id):
        """Fetch details of a specific budget."""
        endpoint = f'budgets/{budget_id}'
        return self._get(endpoint)

    def get_transactions(self, budget_id):
        """Fetch transactions for a specific budget."""
        endpoint = f'budgets/{budget_id}/transactions'
        return self._get(endpoint)

    def create_transaction(self, budget_id, transaction_data):
        """Create a new transaction for a specific budget."""
        endpoint = f'budgets/{budget_id}/transactions'
        return self._post(endpoint, transaction_data)

    def update_transaction(self, budget_id, transaction_id, updated_data):
        """Update an existing transaction for a specific budget."""
        endpoint = f'budgets/{budget_id}/transactions/{transaction_id}'
        return self._put(endpoint, updated_data)

    def get_categories(self, budget_id):
        """Fetch categories for a specific budget."""
        endpoint = f'budgets/{budget_id}/categories'
        return self._get(endpoint)
