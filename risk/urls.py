# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThreatListView, ThreatViewSet, ThreatOriginViewSet, ThreatTypeViewSet

router = DefaultRouter()
router.register(r'threats', ThreatViewSet)
router.register(r'threat-origins', ThreatOriginViewSet)
router.register(r'threat-types', ThreatTypeViewSet)

urlpatterns = [
    path("", ThreatListView.as_view(), name="home"),
    path('api/v1/', include(router.urls)),
]
