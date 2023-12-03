from django.db import models
from app.models.user_profile import UserProfile


class Task(models.Model):
    name = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    # Any other relevant fields
