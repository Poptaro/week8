from rest_framework import serializers
from .models import Owner
from dog_app.serializers import DogSerializer
from cat_app.serializers import CatSerializer
from bird_app.serializers import BirdSerializer
from exotic_app.serializers import ExoticSerializer


class OwnerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Owner
    fields = "__all__"

class OwnerPetsSerializer(serializers.ModelSerializer):

  dogs = serializers.SerializerMethodField()
  cats = serializers.SerializerMethodField()
  birds = serializers.SerializerMethodField()
  exotics = serializers.SerializerMethodField()


  class Meta:
    model = Owner
    fields = "__all__"

  def get_dogs(self, instance):
    dogs = instance.dogs.all()
    return DogSerializer(dogs, many=True).data
  
  def get_cats(self, instance):
    cats = instance.cats.all()
    return CatSerializer(cats, many=True).data
  
  def get_birds(self, instance):
    birds = instance.birds.all()
    return BirdSerializer(birds, many=True).data
  
  def get_exotics(self, instance):
    exotics = instance.exotics.all()
    return ExoticSerializer(exotics, many=True).data