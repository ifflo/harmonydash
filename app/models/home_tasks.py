from django.db import models
from app.models.home import Home
from django.contrib.auth.models import User


class HomeTasks(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    # Any other relevant fields
