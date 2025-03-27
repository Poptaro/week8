from django.db import models

# Create your models here.

class Engine(models.Model):
  size = models.CharField()
  custom = models.BooleanField()
