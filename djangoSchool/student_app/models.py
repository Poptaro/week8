from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length=255)
  student_email = models.EmailField(max_length=255, unique=True)
  personal_email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
  locker_number = models.IntegerField(unique=True, default=110)
  locker_combination = models.CharField(max_length=255, default="12-12-12")
  good_student = models.BooleanField(default=True)

  def locker_reassignment(self, new_locker):
    self.locker_number = new_locker
    self.save()

  def student_status(self, boolean):
    self.good_student = boolean
    self.save()

  def __str__(self):
    return f"{self.name} - {self.student_email} - {self.locker_number}"
  