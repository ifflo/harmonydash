# app/admin.py
from django.contrib import admin
from .models import UserProfile, Schedule, FinancialSettings, Transaction

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Schedule)
admin.site.register(FinancialSettings)
admin.site.register(Transaction)
