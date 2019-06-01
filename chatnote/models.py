from django.db import models
from django.utils import timezone

# Create your models here.
class Account(models.Model):
    place = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=5, decimal_places=0)
    created = models.DateTimeField(blank=True)
    modified = models.DateTimeField(null=True, blank=True)
