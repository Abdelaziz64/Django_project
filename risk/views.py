from django.views.generic import ListView
from .models import Threat

class ThreatListView(ListView):
    model = Threat
    template_name = "home.html"

from rest_framework.response import Response
from rest_framework.decorators import api_view
from risk.models import Threat, ThreatOrigin, ThreatType
from .serializers import ThreatSerializer, ThreatOriginSerializer, ThreatTypeSerializer

@api_view(['GET'])
def getThreats(request):
    threat = Threat.objects.all()
    serializer = ThreatSerializer(threat, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addThreat(request):
    serializer = ThreatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getThreatOrigin(request):
    origin = ThreatOrigin.objects.all()
    serializer = ThreatOriginSerializer(origin, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addThreatOrigin(request):
    serializer = ThreatOriginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getThreatType(request):
    type = ThreatType.objects.all()
    serializer = ThreatTypeSerializer(type, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getThreatTypeDetail(request, pk):
    type = ThreatType.objects.get(id=pk)
    serializer = ThreatTypeSerializer(type, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addThreatType(request):
    serializer = ThreatTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateThreatType(request, pk):
    type = ThreatType.objects.get(id=pk)
    serializer = ThreatTypeSerializer(instance=type, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteThreatType(request, pk):
    type = ThreatType.objects.get(id=pk)
    type.delete()
    return Response('Type deleted.')

 
