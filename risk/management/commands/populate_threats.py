import json
from django.core.management.base import BaseCommand
from risk.models import ThreatEvent
from risk.serializers import ThreatEventSerializer

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            with open('threats-nist.json', 'r', encoding='utf-8') as f:
                threats_data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File threats-nist.json not found'))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('File threats-nist.json is not valid JSON'))
            return
        except UnicodeDecodeError as e:
            self.stdout.write(self.style.ERROR(f'Unicode decode error: {e}'))
            return

        serializer = ThreatEventSerializer(data=threats_data, many=True)
        if serializer.is_valid():
            serializer.save()
            self.stdout.write(self.style.SUCCESS('Successfully populated threats'))
        else:
            self.stdout.write(self.style.ERROR('Failed to populate threats'))
            self.stdout.write(str(serializer.errors))
