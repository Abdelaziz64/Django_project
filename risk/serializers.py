from rest_framework import serializers
from .models import Threat,Family, Category,ThreatEvent,ThreatEventCategory

class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = ['category_name','description', 'name']

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['family']

class ThreatCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name','description','family','id']

class ThreatEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreatEvent
        fields = ['event_category_name','event_name','description',]

class ThreatEventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreatEventCategory
        fields = ['category_name','event_category_name']
