# app/models/home_settings.py
from django.db import models
from app.models.home import Home


class HomeSettings(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='home_settings')
    setting_name = models.CharField(max_length=100)
    setting_value = models.CharField(max_length=255)
    # Additional fields as required

    def __str__(self):
        return f"{self.setting_name} for {self.home.name}"
