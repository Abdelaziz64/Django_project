from rest_framework import serializers
from risk.models import Threat

class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = ['name', 'description', 'source']

