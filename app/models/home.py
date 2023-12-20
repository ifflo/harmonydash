# app/models/home.py
from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    name = models.CharField(max_length=100)
    # Other fields as necessary (e.g., address, contact info)

    def __str__(self):
        return self.name
