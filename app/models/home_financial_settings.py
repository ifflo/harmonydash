# app/models/home_financial_settings.py
from django.db import models
from app.models.home import Home


class HomeFinancialSettings(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='financial_settings')
    budget_id = models.CharField(max_length=100, blank=True, null=True, help_text="YNAB Budget ID")
    budget_name = models.CharField(max_length=255, blank=True, null=True, help_text="YNAB Budget Name")
    min_account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    budget_threshold = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    # Add other fields as necessary

    def __str__(self):
        return f"FinancialSettings for {self.home.name}"
