# app/models/financial_settings.py
from django.db import models
from django.contrib.auth.models import User


class FinancialSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    min_account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    budget_threshold = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    # Add other fields as necessary

    def __str__(self):
        return f"FinancialSettings for {self.user.username}"
