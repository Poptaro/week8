from django.db import models
from django.utils import timezone
from car_app.models import Car


# Create your models here.
class Service(models.Model):
  date = models.DateField(default=timezone.now())
  reason = models.CharField()
  completed = models.BooleanField(default=False)
  place_of_service = models.CharField()
  notes = models.TextField()
  
  #foreign many to one
  vehicle = models.ForeignKey(Car, related_name="services", on_delete=models.CASCADE)

