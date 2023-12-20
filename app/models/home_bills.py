from django.db import models
from app.models.home import Home


class HomeBills(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    bill_name = models.CharField(max_length=100)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    # Additional fields as required for your financial planning
