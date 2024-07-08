from rest_framework import serializers
from .models import Threat, ThreatOrigin, ThreatType

class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = ['name', 'description', 'source', 'origin', 'type']

class ThreatOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreatOrigin
        fields = ['origin']

class ThreatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreatType
        fields = ['type']