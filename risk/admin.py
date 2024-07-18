# blog/admin.py On enregistre ici tous nos models
from django.contrib import admin
from .models import Threat,Family, Category,ThreatEvent,ThreatEventCategory
admin.site.register(Threat)
admin.site.register(Family)
admin.site.register(Category)
admin.site.register(ThreatEvent)
admin.site.register(ThreatEventCategory)