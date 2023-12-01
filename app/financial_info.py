from django.db import models
from .user_profile import UserProfile

class FinancialInfo(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bill_name = models.CharField(max_length=100)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    # Additional fields as required for your financial planning
