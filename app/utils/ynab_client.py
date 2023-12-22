# app/utils/ynab_client.py
import requests
from urllib.parse import urljoin
import traceback
from app.models import HomeFinancialSettings
import ynab_api
import requests
from pprint import pprint
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.budget_summary_response import BudgetSummaryResponse
from ynab_api.api import accounts_api, budgets_api, months_api, categories_api, transactions_api, \
    scheduled_transactions_api, user_api, payees_api, payee_locations_api
from django.conf import settings


class YNABClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or settings.YNAB_API_KEY
        self.api_base_url = "https://api.ynab.com/v1"

    def sync_ynab_data(self):
        """Synchronize data from the YNAB API."""
        try:
            # Fetch budgets using the new method
            budgets = self.get_budgets()

            # Check if budgets data is valid
            if budgets is None or not isinstance(budgets, list):
                raise ValueError("Invalid budget data received from YNAB API")

            # Process and integrate budgets into Django models
            for budget in budgets:
                # Update or create budget in FinancialSettings model
                HomeFinancialSettings.objects.update_or_create(
                    budget_id=budget.id,  # Assuming 'id' is the correct field name
                    defaults={
                        'budget_name': budget.name,  # Assuming 'name' is the correct field name
                        # ... other fields if necessary ...
                    }
                )
            print("YNAB data synchronized successfully.")
        except Exception as e:
            print(f"Error during YNAB data synchronization: {e}")
            print(traceback.format_exc())

    def get_budgets(self):
        url = f"{self.api_base_url}/budgets"
        response = requests.get(url, headers=self.get_headers())
        return response.json()

    def get_transactions(self, budget_id):
        url = f"{self.api_base_url}/budgets/{budget_id}/transactions"
        response = requests.get(url, headers=self.get_headers())
        return response.json()

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}"
        }


'''
    def get_budget_months(self, budget_id):
        """Retrieve all months for a given budget."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = months_api.MonthsApi(api_client)
            try:
                api_response = api_instance.get_budget_months(budget_id)
                return api_response.data.months
            except ynab_api.ApiException as e:
                print("Exception when calling MonthsApi->get_budget_months: %s\n" % e)
                return None

    def get_budget_month(self, budget_id, month):
        """Retrieve a specific month's budget details."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = months_api.MonthsApi(api_client)
            try:
                api_response = api_instance.get_budget_month(budget_id, month)
                return api_response.data.month
            except ynab_api.ApiException as e:
                print("Exception when calling MonthsApi->get_budget_month: %s\n" % e)
                return None

    def get_budget_settings_by_id(self, budget_id):
        """Retrieve the settings for a specific budget."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = budgets_api.BudgetsApi(api_client)
            try:
                api_response = api_instance.get_budget_settings_by_id(budget_id)
                return api_response.data.settings
            except ynab_api.ApiException as e:
                print("Exception when calling BudgetsApi->get_budget_settings_by_id: %s\n" % e)
                return None

    def get_categories(self, budget_id):
        """Retrieve all categories for a given budget."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = categories_api.CategoriesApi(api_client)
            try:
                api_response = api_instance.get_categories(budget_id)
                return api_response.data.category_groups
            except ynab_api.ApiException as e:
                print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
                return None

    def update_month_category(self, budget_id, month, category_id, category_data):
        """Update a category for a specific month."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = categories_api.CategoriesApi(api_client)
            try:
                api_response = api_instance.update_month_category(budget_id, month, category_id, category_data)
                return api_response.data.category
            except ynab_api.ApiException as e:
                print("Exception when calling CategoriesApi->update_month_category: %s\n" % e)
                return None

    def get_accounts(self, budget_id):
        """Retrieve accounts for a given budget."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = accounts_api.AccountsApi(api_client)
            try:
                api_response = api_instance.get_accounts(budget_id)
                return api_response.data.accounts
            except ynab_api.ApiException as e:
                print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
                return None

    def create_transaction(self, budget_id, transaction_data):
        """Create a new transaction."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = transactions_api.TransactionsApi(api_client)
            data = transactions_api.SaveTransactionsWrapper(transaction=transaction_data)
            try:
                api_response = api_instance.create_transaction(budget_id, data)
                return api_response.data.transaction
            except ynab_api.ApiException as e:
                print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
                return None

    def get_category_by_id(self, budget_id, category_id):
        """Retrieve a single category by its ID."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = categories_api.CategoriesApi(api_client)
            try:
                api_response = api_instance.get_category_by_id(budget_id, category_id)
                return api_response.data.category
            except ynab_api.ApiException as e:
                print("Exception when calling CategoriesApi->get_category_by_id: %s\n" % e)
                return None

    def get_transactions_by_category(self, budget_id, category_id):
        """Retrieve transactions for a specific category."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = transactions_api.TransactionsApi(api_client)
            try:
                api_response = api_instance.get_transactions_by_category(budget_id, category_id)
                return api_response.data.transactions
            except ynab_api.ApiException as e:
                print("Exception when calling TransactionsApi->get_transactions_by_category: %s\n" % e)
                return None

    def get_scheduled_transaction_by_id(self, budget_id, scheduled_transaction_id):
        """Retrieve a single scheduled transaction by its ID."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = scheduled_transactions_api.ScheduledTransactionsApi(api_client)
            try:
                api_response = api_instance.get_scheduled_transaction_by_id(budget_id, scheduled_transaction_id)
                return api_response.data.scheduled_transaction
            except ynab_api.ApiException as e:
                print("Exception when calling ScheduledTransactionsApi->get_scheduled_transaction_by_id: %s\n" % e)
                return None

    def get_scheduled_transactions(self, budget_id):
        """Retrieve all scheduled transactions for a given budget."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = scheduled_transactions_api.ScheduledTransactionsApi(api_client)
            try:
                api_response = api_instance.get_scheduled_transactions(budget_id)
                return api_response.data.scheduled_transactions
            except ynab_api.ApiException as e:
                print("Exception when calling ScheduledTransactionsApi->get_scheduled_transactions: %s\n" % e)
                return None

    def update_transaction(self, budget_id, transaction_id, transaction_data):
        """Update an existing transaction."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = transactions_api.TransactionsApi(api_client)
            try:
                api_response = api_instance.update_transaction(budget_id, transaction_id, transaction_data)
                return api_response.data.transaction
            except ynab_api.ApiException as e:
                print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
                return None

    def get_transactions_by_account(self, budget_id, account_id):
        """Retrieve transactions for a specific account."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = transactions_api.TransactionsApi(api_client)
            try:
                api_response = api_instance.get_transactions_by_account(budget_id, account_id)
                return api_response.data.transactions
            except ynab_api.ApiException as e:
                print("Exception when calling TransactionsApi->get_transactions_by_account: %s\n" % e)
                return None

    def get_user(self):
        """Retrieve user information."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = user_api.UserApi(api_client)
            try:
                api_response = api_instance.get_user()
                return api_response.data.user
            except ynab_api.ApiException as e:
                print("Exception when calling UserApi->get_user: %s\n" % e)
                return None

    def get_transactions_by_payee(self, budget_id, payee_id):
        """Retrieve transactions for a specific payee."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = transactions_api.TransactionsApi(api_client)
            try:
                api_response = api_instance.get_transactions_by_payee(budget_id, payee_id)
                return api_response.data.transactions
            except ynab_api.ApiException as e:
                print("Exception when calling TransactionsApi->get_transactions_by_payee: %s\n" % e)
                return None

    def get_payee_by_id(self, budget_id, payee_id):
        """Retrieve a single payee by its ID."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = payees_api.PayeesApi(api_client)
            try:
                api_response = api_instance.get_payee_by_id(budget_id, payee_id)
                return api_response.data.payee
            except ynab_api.ApiException as e:
                print("Exception when calling PayeesApi->get_payee_by_id: %s\n" % e)
                return None

    def import_transactions(self, budget_id):
        """Import transactions."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = transactions_api.TransactionsApi(api_client)
            try:
                api_response = api_instance.import_transactions(budget_id)
                return api_response.data.transaction_ids
            except ynab_api.ApiException as e:
                print("Exception when calling TransactionsApi->import_transactions: %s\n" % e)
                return None

    def update_transactions(self, budget_id, transactions_data):
        """Update multiple transactions."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = transactions_api.TransactionsApi(api_client)
            try:
                api_response = api_instance.update_transactions(budget_id, transactions_data)
                return api_response.data.transactions
            except ynab_api.ApiException as e:
                print("Exception when calling TransactionsApi->update_transactions: %s\n" % e)
                return None

    def get_payees(self, budget_id):
        """Retrieve a list of all payees for a budget."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = payees_api.PayeesApi(api_client)
            try:
                api_response = api_instance.get_payees(budget_id)
                return api_response.data.payees
            except ynab_api.ApiException as e:
                print("Exception when calling PayeesApi->get_payees: %s\n" % e)
                return None

    def get_payee_locations(self, budget_id):
        """Retrieve a list of all payee locations for a budget."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = payee_locations_api.PayeeLocationsApi(api_client)
            try:
                api_response = api_instance.get_payee_locations(budget_id)
                return api_response.data.payee_locations
            except ynab_api.ApiException as e:
                print("Exception when calling PayeeLocationsApi->get_payee_locations: %s\n" % e)
                return None

    def get_payee_locations_by_payee(self, budget_id, payee_id):
        """Retrieve a list of all locations for a specific payee."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = payee_locations_api.PayeeLocationsApi(api_client)
            try:
                api_response = api_instance.get_payee_locations_by_payee(budget_id, payee_id)
                return api_response.data.payee_locations
            except ynab_api.ApiException as e:
                print("Exception when calling PayeeLocationsApi->get_payee_locations_by_payee: %s\n" % e)
                return None

    def get_payee_location_by_id(self, budget_id, payee_location_id):
        """Retrieve details of a specific payee location."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = payee_locations_api.PayeeLocationsApi(api_client)
            try:
                api_response = api_instance.get_payee_location_by_id(budget_id, payee_location_id)
                return api_response.data.payee_location
            except ynab_api.ApiException as e:
                print("Exception when calling PayeeLocationsApi->get_payee_location_by_id: %s\n" % e)
                return None

    def get_transaction_by_id(self, budget_id, transaction_id):
        """Retrieve details of a specific transaction."""
        with ynab_api.ApiClient(self.configuration) as api_client:
            api_instance = transactions_api.TransactionsApi(api_client)
            try:
                api_response = api_instance.get_transaction_by_id(budget_id, transaction_id)
                return api_response.data.transaction
            except ynab_api.ApiException as e:
                print("Exception when calling TransactionsApi->get_transaction_by_id: %s\n" % e)
                return None'''