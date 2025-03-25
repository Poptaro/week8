from django.db import models
from django.core import validators as v
from .validator import validate_student_name, validate_student_email

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length=255, validators=[validate_student_name])
  student_email = models.EmailField(max_length=255, unique=True, validators=[validate_student_email])
  personal_email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
  locker_number = models.IntegerField(unique=True, default=110, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
  locker_combination = models.CharField(max_length=255, default="12-12-12" )
  good_student = models.BooleanField(default=True)

  def locker_reassignment(self, new_locker):
    self.locker_number = new_locker
    self.save()

  def student_status(self, boolean):
    self.good_student = boolean
    self.save()

  def __str__(self):
    return f"{self.name} - {self.student_email} - {self.locker_number}"
  