# app/admin.py
from django.contrib import admin
from .models import Bonus, FinancialInfo, FinancialSettings, Salary, Schedule, Task, Transaction, UserProfile

# Register your models here.

admin.site.register(Bonus)
admin.site.register(FinancialInfo)
admin.site.register(FinancialSettings)
admin.site.register(Salary)
admin.site.register(Schedule)
admin.site.register(Task)
admin.site.register(Transaction)
admin.site.register(UserProfile)
