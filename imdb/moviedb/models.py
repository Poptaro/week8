from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.
class Actor(models.Model):
  name = models.CharField(default="no name")
  age = models.IntegerField(default=21)

  def __str__(self):
    return (f"{self.name} - {self.age}")


class Movie(models.Model):
  title = models.CharField(default="no title")
  release_year = models.IntegerField(default=2000)

  def __str__(self):
    return (f"{self.title} - {self.release_year}")


class Role(models.Model):
  actor = models.ForeignKey(Actor, related_name="roles", on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, related_name="roles", on_delete=models.CASCADE)

  class Meta:
    constraints = [
            UniqueConstraint(fields=["actor", "movie"], name="unique_actor_movie")
        ]