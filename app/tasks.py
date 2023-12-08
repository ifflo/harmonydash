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
    transactions = ynab_client.fetch_transactions()
    # Process and store transactions
