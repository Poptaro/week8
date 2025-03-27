from django.db import models

# Create your models here.
class Owner(models.Model):

  name = models.CharField()
  age = models.IntegerField()
  number_of_vehicles = models.IntegerField()
  address = models.CharField()
  