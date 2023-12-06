# app/utils/financial_processing.py
from .ynab_api import fetch_transactions


def analyze_financial_data():
    transactions = fetch_transactions()
    if transactions is None:
        return None

    # Example: Sum transactions by category
    category_totals = {}
    for transaction in transactions:
        category = transaction['category_name']
        amount = transaction['amount']
        category_totals[category] = category_totals.get(category, 0) + amount

    return category_totals
