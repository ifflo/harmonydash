# app/admin.py
from django.contrib import admin
from .models import Bonus, FinancialInfo, FinancialSettings, Salary, Schedule, Task, Transaction, UserProfile
from django import forms
from .utils.ynab_client import YNABClient
from django.conf import settings

# Register your models here.
admin.site.register(Bonus)
admin.site.register(FinancialInfo)
admin.site.register(FinancialSettings)
admin.site.register(Salary)
admin.site.register(Schedule)
admin.site.register(Task)
admin.site.register(Transaction)
admin.site.register(UserProfile)


class FinancialSettingsForm(forms.ModelForm):
    ynab_budget = forms.ChoiceField(choices=(), required=False, label="YNAB Budget")

    class Meta:
        model = FinancialSettings
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        api_key = settings.YNAB_API_KEY  # Securely retrieve the API key
        ynab_client = YNABClient(api_key)
        budgets = ynab_client.get_budgets()
        budget_choices = [(budget['id'], budget['name']) for budget in budgets]
        self.fields['ynab_budget'].choices = budget_choices

    def save(self, commit=True):
        self.instance.budget_id = self.cleaned_data['ynab_budget']
        return super().save(commit)


class FinancialSettingsAdmin(admin.ModelAdmin):
    form = FinancialSettingsForm
    list_display = ['id', 'name', 'budget_id', 'budget_name']

