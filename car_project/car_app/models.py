from django.db import models
from owner_app.models import Owner
from engine_app.models import Engine
from tire_app.models import Tire

# Create your models here.
class Car(models.Model):
  make = models.CharField()
  model = models.CharField()
  year = models.CharField()  
  mileage = models.BigIntegerField(default=0)



  #One to One
  # tire
  tire = models.OneToOneField(Tire, related_name="car", on_delete=models.CASCADE)
  # engine
  engine = models.OneToOneField(Engine, related_name="car", on_delete=models.CASCADE)


  #Many to Many
  owners = models.ManyToManyField(Owner, related_name="cars")