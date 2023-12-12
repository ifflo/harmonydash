# app/management/commands/sync_ynab.py

from django.core.management.base import BaseCommand
from app.utils.ynab_client import YNABClient
from django.conf import settings


class Command(BaseCommand):
    help = 'Sync data from YNAB API'

    def handle(self, *args, **kwargs):
        api_key = settings.YNAB_API_KEY  # Securely retrieve the API key
        ynab_client = YNABClient(api_key)
        ynab_client.sync_ynab_data()
        self.stdout.write(self.style.SUCCESS('Successfully synced data from YNAB API'))
