# app/utils/financial_analysis.py
from .ynab_client import YNABClient
from app.models import FinancialSettings
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from app.models import Transaction


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


def calculate_monthly_expenses(user_id):
    monthly_expenses = Transaction.objects.filter(
        user_id=user_id,
        transaction_type='expense'
    ).annotate(
        month=TruncMonth('date')
    ).values(
        'month'
    ).annotate(
        total=Sum('amount')
    ).order_by('month')

    return list(monthly_expenses)


def calculate_monthly_income(user_id):
    monthly_income = Transaction.objects.filter(
        user_id=user_id,
        transaction_type='income'
    ).annotate(
        month=TruncMonth('date')
    ).values(
        'month'
    ).annotate(
        total=Sum('amount')
    ).order_by('month')

    return list(monthly_income)


def calculate_spending_by_category(user_id):
    category_spending = Transaction.objects.filter(
        user_id=user_id,
        transaction_type='expense'
    ).values(
        'category'
    ).annotate(
        total=Sum('amount')
    ).order_by('-total')

    return list(category_spending)
