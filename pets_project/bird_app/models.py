from django.db import models
from owner_app.models import Owner

# Create your models here.

class Bird(models.Model):

  name = models.CharField(max_length=255)
  age = models.BigIntegerField()
  vaccinated = models.BooleanField()
  species = models.CharField(max_length=255)
  description = models.TextField()

  owner = models.ForeignKey(Owner, related_name="birds", on_delete=models.SET_NULL, null=True, blank=True)
