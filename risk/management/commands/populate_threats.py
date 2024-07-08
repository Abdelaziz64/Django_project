import json
from django.core.management.base import BaseCommand
from risk.models import Threat
from risk.serializers import ThreatSerializer

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('threats.json') as f:
            threats_data = json.load(f)
        
        serializer = ThreatSerializer(data=threats_data, many=True)
        if serializer.is_valid():
            serializer.save()
            self.stdout.write(self.style.SUCCESS('Successfully populated threats'))
        else:
            self.stdout.write(self.style.ERROR('Failed to populate threats'))
            self.stdout.write(str(serializer.errors))
