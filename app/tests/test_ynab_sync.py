from django.test import TestCase
from unittest.mock import patch
from app.models.transactions import Transaction
from app.utils.ynab_client import YNABClient


class YNABSyncTest(TestCase):

    @patch('app.utils.ynab_client.YNABClient.get_transactions')
    @patch('app.utils.ynab_client.YNABClient.get_budgets')
    def test_sync_transactions(self, mock_get_budgets, mock_get_transactions):
        # Mocking YNAB API response for budgets
        mock_get_budgets.return_value = {
            'data': {'budgets': [
                {'id': 'budget1', 'name': 'Test Budget 1'},
                # ... other mocked budgets ...
            ]}
        }

        # Mocking YNAB API response
        mock_get_transactions.return_value = {
            'data': {'transactions': [
                {'id': 'txn1', 'date': '2021-01-01', 'amount': 1000, 'memo': 'Test Transaction 1'},
                {'id': 'txn2', 'date': '2021-01-02', 'amount': 2000, 'memo': 'Test Transaction 2'}
                # ... more mocked transactions with unique 'id' ...
            ]}
        }

        # Initialize YNABClient and call sync_ynab_data
        ynab_client = YNABClient('test_api_key')
        ynab_client.sync_ynab_data()

        # Assertions to ensure transactions are synced correctly
        self.assertTrue(Transaction.objects.filter(ynab_id='txn1').exists())
        self.assertTrue(Transaction.objects.filter(ynab_id='txn2').exists())
        # ... more assertions ...
