from django.views.generic import ListView
from .models import Threat

class ThreatListView(ListView):
    model = Threat
    template_name = "home.html"

from rest_framework.response import Response
from rest_framework.decorators import api_view
from risk.models import Threat
from .serializers import ThreatSerializer

@api_view(['GET'])
def getThreats(request):
    threat = Threat.objects.all()
    serializer = ThreatSerializer(threat, many=True)
    return Response(serializer.data)



 
