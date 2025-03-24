from django.db import models

# Create your models here.
class Owner(models.Model):
  name = models.CharField(max_length=255)
  age = models.BigIntegerField()
  number_of_oets = models.BigIntegerField()



class Animal(models.Model):

  name = models.CharField(max_length=255)
  age = models.PositiveBigIntegerField()
  vaccinated = models.BooleanField(default=False)
  description = models.TextField(max_length=500)

  class Meta:
    abstract = True



class Cat(Animal):
  breed = models.CharField(max_length=255)

class Dog(Animal):
  breed = models.CharField(max_length=255)

class Bird(Animal):
  species = models.CharField(max_length=255)

class Exotic_Animal(Animal):
  region_of_origin = models.CharField(max_length=255)
  type_of_animal = models.CharField(max_length=255)
  description = None
