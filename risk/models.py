from django.db import models
from django.urls import reverse

class ThreatType(models.Model):
    type = models.TextField()

    def __str__(self):
        return self.type

class ThreatOrigin(models.Model):
    origin = models.TextField()

    def __str__(self):
        return self.origin


class Threat(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    source = models.TextField(null=True)

    origin = models.ForeignKey(ThreatOrigin, on_delete=models.CASCADE,null=True)
    type = models.ForeignKey(ThreatType, on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("threat_detail", kwargs={"pk": self.pk})


