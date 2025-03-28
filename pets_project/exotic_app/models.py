from django.db import models
from owner_app.models import Owner

# Create your models here.

class Exotic(models.Model):

  name = models.CharField(max_length=255)
  age = models.BigIntegerField()
  vaccinated = models.BooleanField()
  type_of_animal = models.CharField(max_length=255)
  region_of_origin = models.CharField(max_length=255)
  description = models.TextField()

  owner = models.ForeignKey(Owner, related_name="exotics", on_delete=models.SET_NULL, null=True, blank=True)
