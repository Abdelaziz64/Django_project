from django.urls import path
from .views import ThreatListView, getThreats
urlpatterns = [
path("", ThreatListView.as_view(), name="home"),
path('api/v1/threats', getThreats)
]
