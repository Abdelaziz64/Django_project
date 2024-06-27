# blog/admin.py On enregistre ici tous nos models
from django.contrib import admin
from .models import Threat,ThreatType, ThreatOrigin
admin.site.register(Threat)
admin.site.register(ThreatType)
admin.site.register(ThreatOrigin)