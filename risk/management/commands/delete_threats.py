# File: myapp/management/commands/delete_threats.py

from django.core.management.base import BaseCommand
from risk.models import Threat

class Command(BaseCommand):
    help = 'Delete all Threat records'

    def handle(self, *args, **kwargs):
        try:
            count, _ = Threat.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} Threat records.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to delete Threat records: {str(e)}'))
