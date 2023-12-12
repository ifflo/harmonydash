# app/models/transactions.py
from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    ynab_id = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    memo = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    transaction_type = models.CharField(
        max_length=100,
        choices=TRANSACTION_TYPES,
        default='expense'  # Setting 'expense' as the default transaction type
    )

    def __str__(self):
        return f"Transaction on {self.date} for {self.user}"
