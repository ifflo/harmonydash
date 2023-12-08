# app/models/bonus.py

from django.db import models
from django.contrib.auth.models import User


class Bonus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField()
    reason = models.CharField(max_length=100)
    is_recurring = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Bonus on {self.date_received}"
