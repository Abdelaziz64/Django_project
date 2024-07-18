# views.py
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Threat,Family,ThreatEventCategory,ThreatEvent,Category
from .serializers import ThreatSerializer, ThreatEventSerializer, ThreatCategorySerializer,FamilySerializer,ThreatEventCategorySerializer

class ThreatListView(ListView):
    model = Threat
    template_name = "home.html"

class ThreatViewSet(viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class ThreatCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ThreatCategorySerializer
    @action(detail=False, methods=['get'])
    def get_by_family(self, request):
        family_id = request.query_params.get('family_id')
        if family_id is not None:
            categories = Category.objects.filter(family_id=family_id)
            serializer = self.get_serializer(categories, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "Family ID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

class ThreatEventViewSet(viewsets.ModelViewSet):
    queryset = ThreatEvent.objects.all()
    serializer_class = ThreatEventSerializer

    @action(detail=False, methods=['get'])
    def get_by_category(self, request):
        category_id = request.query_params.get('category_id')
        if category_id is not None:
            events = ThreatEvent.objects.filter(event_category_name__category_name_id=category_id)
            serializer = self.get_serializer(events, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "Category ID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_by_family(self, request):
        family_id = request.query_params.get('family_id')
        if family_id is not None:
            events = ThreatEvent.objects.filter(event_category_name__category_name__family_id=family_id)
            serializer = self.get_serializer(events, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "Family ID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
class ThreatEventCategoryViewSet(viewsets.ModelViewSet):
    queryset = ThreatEventCategory.objects.all()
    serializer_class = ThreatEventCategorySerializer
