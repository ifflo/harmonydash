# app/models/account.py
from django.db import models


class Account(models.Model):
    ynab_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    # Add other relevant fields based on the YNAB account data structure
