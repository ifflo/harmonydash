# app/utils/ynab_client.py
import requests
from urllib.parse import urljoin
from app.models import Transaction, Account


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
            # Sync budgets
            budgets = self.get_budgets()['data']['budgets']

            # Sync transactions
            for budget in budgets:
                transactions = self.get_transactions(budget['id'])['data']['transactions']
                for transaction_data in transactions:
                    # Assuming you have a method to determine the user from transaction data
                    user_instance = self.get_user_for_transaction(transaction_data)

                    transaction, created = Transaction.objects.update_or_create(
                        ynab_id=transaction_data['id'],
                        defaults={
                            'user': user_instance,  # Set the user for the transaction
                            'date': transaction_data['date'],
                            'amount': transaction_data['amount'],
                            'memo': transaction_data.get('memo'),
                            # include other necessary fields
                        }
                    )
                    if created:
                        print(f"Created new transaction: {transaction.ynab_id}")
                    else:
                        print(f"Updated existing transaction: {transaction.ynab_id}")

            # Sync accounts
            for budget in budgets:
                accounts = self.get_accounts(budget['id'])['data']['accounts']
                for account_data in accounts:
                    Account.objects.update_or_create(
                        ynab_id=account_data['id'],
                        defaults={
                            'name': account_data['name'],
                            'type': account_data['type'],
                            'balance': account_data['balance'],
                            # map other fields
                        }
                    )
            # Logic to update or create accounts in your Django model

            print("YNAB data synchronized successfully.")
        except Exception as e:
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

    def get_accounts(self, budget_id):
        """Fetch account information for a specific budget."""
        endpoint = f'budgets/{budget_id}/accounts'
        return self._get(endpoint)
