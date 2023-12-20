# app/utils/financial_analysis.py
from .ynab_client import YNABClient
from app.models import HomeFinancialSettings
from django.db.models import Sum
from django.db.models.functions import TruncMonth


def analyze_transactions(home):
    ynab_client = YNABClient()
    transactions = ynab_client.get_transactions('budget_id')
    financial_settings = HomeFinancialSettings.objects.get(home=home)

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
