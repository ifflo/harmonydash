from django.db import models
from .user_profile import UserProfile


class Schedule(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_commute_day = models.BooleanField(default=False)
    # Other fields like type of shift, notes, etc.
