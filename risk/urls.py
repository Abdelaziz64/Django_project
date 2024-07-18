# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThreatListView, ThreatViewSet, FamilyViewSet, ThreatCategoryViewSet, ThreatEventCategoryViewSet,ThreatEventViewSet

router = DefaultRouter()
router.register(r'threats', ThreatViewSet)
router.register(r'family', FamilyViewSet)
router.register(r'threat-categories', ThreatCategoryViewSet, basename='threat-category')
router.register(r'threat_event-categories', ThreatEventCategoryViewSet)
router.register(r'threat_event', ThreatEventViewSet, basename='threat-event')

urlpatterns = [
    path("", ThreatListView.as_view(), name="home"),
    path('api/v1/', include(router.urls)),
]
