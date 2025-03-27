from django.db import models

# Create your models here.
class Tire(models.Model):
  section_width = models.IntegerField()
  aspect_ratio = models.IntegerField()
  rim_size = models.IntegerField()
  