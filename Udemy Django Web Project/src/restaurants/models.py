from django.db import models
from django.db.models import Model
# Create your models here.

class Restaraunt(Model):
    name = models.CharField(max_length=120)
    
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
