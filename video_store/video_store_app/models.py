from django.db import models

# Create your models here.
class Client(models.Model):
  email = models.CharField(max_length=255)
  account_type = models.CharField(max_length=255)
  active = models.BooleanField(default=True)

class Store(models.Model):
  name = models.CharField(max_length=255)
  owner = models.CharField(max_length=255)
  number_of_employees = models.PositiveBigIntegerField()
  rating = models.FloatField()

class Video(models.Model):
  title = models.CharField(max_length=255)
  in_stock = models.PositiveBigIntegerField()
  rating = models.CharField(max_length=255)

class Address(models.Model):
  street = models.CharField(max_length=255)
  zipcode = models.BigIntegerField()
  state = models.CharField(max_length=255)
  appt_num = models.BigIntegerField()

class Person(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  middle_init = models.CharField(max_length=255)
  age = models.BigIntegerField()
