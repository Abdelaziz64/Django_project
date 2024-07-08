# views.py
from django.views.generic import ListView
from rest_framework import viewsets
from .models import Threat, ThreatOrigin, ThreatType
from .serializers import ThreatSerializer, ThreatOriginSerializer, ThreatTypeSerializer

class ThreatListView(ListView):
    model = Threat
    template_name = "home.html"

class ThreatViewSet(viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer

class ThreatOriginViewSet(viewsets.ModelViewSet):
    queryset = ThreatOrigin.objects.all()
    serializer_class = ThreatOriginSerializer

class ThreatTypeViewSet(viewsets.ModelViewSet):
    queryset = ThreatType.objects.all()
    serializer_class = ThreatTypeSerializer
