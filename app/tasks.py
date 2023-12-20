# app/tasks.py
from celery import shared_task
from .utils.financial_analysis import analyze_user_transactions
from django.contrib.auth.models import User
from .utils.ynab_client import YNABClient


@shared_task
def update_financial_data(user_id):
    user = User.objects.get(pk=user_id)
    analyze_user_transactions(user)
    # You can add logic here to handle the results, like sending notifications


@shared_task
def update_transactions():
    ynab_client = YNABClient()
    try:
        # Replace 'budget_id_example' with the actual budget ID
        transactions = ynab_client.get_transactions('budget_id_example')
        # Process and store transactions
        # Add your logic here to handle transactions
    except Exception as e:
        # Handle exceptions (e.g., log error)
        print(f"Error updating transactions: {e}")
