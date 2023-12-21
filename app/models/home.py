# app/models/home.py
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Home(models.Model):
    name = models.CharField(max_length=100)
    # Other fields as necessary (e.g., address, contact info)

    def save(self, *args, **kwargs):
        if Home.objects.exists() and not self.pk:
            # If trying to create a new Home instance when one already exists
            raise ValidationError('There can only be one Home instance.')
        return super(Home, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
