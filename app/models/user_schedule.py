from django.db import models
from django.contrib.auth.models import User


class UserSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_commute_day = models.BooleanField(default=False)
    # Other fields like type of shift, notes, etc.
