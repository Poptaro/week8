from django.db import models

# Create your models here.

class Owner(models.Model):
  name = models.CharField(max_length=255)
  age = models.BigIntegerField()
  
  @property
  def number_of_pets(self):
    return (self.dogs.count() + self.birds.count() + self.cats.count() + self.exotics.count())
  
  def __str__(self):
    return (f"{self.name} - {self.age}| Num Of Pets: {self.number_of_pets}")