# app/admin.py
import logging

from django.contrib import admin
from .models import HomeBills, HomeFinancialSettings, UserSalary, UserSchedule, HomeTasks, UserProfile
from django import forms
from .utils.ynab_client import YNABClient
from django.conf import settings

# Register your models here.
admin.site.register(HomeBills)
admin.site.register(HomeFinancialSettings)
admin.site.register(UserSalary)
admin.site.register(UserSchedule)
admin.site.register(HomeTasks)
admin.site.register(UserProfile)


class HomeFinancialSettingsForm(forms.ModelForm):
    ynab_budget = forms.ChoiceField(choices=(), required=False, label="YNAB Budget")

    class Meta:
        model = HomeFinancialSettings
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        api_key = settings.YNAB_API_KEY
        ynab_client = YNABClient(api_key)
        try:
            budgets = ynab_client.get_budgets()
            budget_choices = [(budget['id'], budget['name']) for budget in budgets]
            self.fields['ynab_budget'].choices = budget_choices
        except Exception as e:
            # Handle exceptions (e.g., log error and set empty choices)
            self.fields['ynab_budget'].choices = []
            logging.exception(e)

    def save(self, commit=True):
        self.instance.budget_id = self.cleaned_data['ynab_budget']
        return super().save(commit)


class FinancialSettingsAdmin(admin.ModelAdmin):
    form = HomeFinancialSettingsForm
    list_display = ['id', 'name', 'budget_id', 'budget_name']

