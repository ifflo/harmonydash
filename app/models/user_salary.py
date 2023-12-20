# app/models/user_salary.py
from django.db import models
from .user_profile import UserProfile


class UserSalary(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    payment_frequency = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}'s Salary"
