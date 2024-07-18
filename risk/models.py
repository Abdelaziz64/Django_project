from django.db import models
from django.urls import reverse

class Family(models.Model):
    family = models.TextField()
    def __str__(self):
        return self.family
    
class Category(models.Model):
    category_name = models.TextField()
    description = models.TextField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.category_name
    

class ThreatEventCategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    event_category_name = models.TextField()
    def __str__(self):
        return self.event_category_name

class ThreatEvent(models.Model):
    event_category_name = models.ForeignKey(ThreatEventCategory, on_delete=models.CASCADE,null=True)
    event_name = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.event_name


class Threat(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name   






