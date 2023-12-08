# app/utils/financial_analysis.py
from .ynab_client import YNABClient
from ..models import FinancialSettings


def analyze_user_transactions(user):
    ynab_client = YNABClient()
    transactions = ynab_client.fetch_transactions()
    financial_settings = FinancialSettings.objects.get(user=user)

    # Example analysis: Check if spending in any category exceeds the budget threshold
    category_totals = {}
    for transaction in transactions:
        category = transaction['category_name']
        amount = transaction['amount']
        category_totals[category] = category_totals.get(category, 0) + amount

    alerts = []
    for category, total in category_totals.items():
        if total > financial_settings.budget_threshold:
            alerts.append(f"Budget exceeded in {category}")

    return alerts
