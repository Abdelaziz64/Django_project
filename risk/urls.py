from django.urls import path
from . views import ThreatListView, getThreats
from . import views
urlpatterns = [
    path("", ThreatListView.as_view(), name="home"),
    path('api/v1/threats', getThreats, name='get_threats'),

    path('api/v1/addThreat/', views.addThreat),
    path('api/v1/addThreatOrigin/', views.addThreatOrigin),
    path('api/v1/addThreatType/', views.addThreatType),

    path('api/v1/getThreatType/', views.getThreatType),
    path('api/v1/getThreatTypeDetail/<str:pk>', views.getThreatTypeDetail),
    path('api/v1/getThreatOrigin/', views.getThreatOrigin),

    path('api/v1/updateThreatType/<str:pk>', views.updateThreatType),
    path('api/v1/deleteThreatType/<str:pk>', views.deleteThreatType),

]
