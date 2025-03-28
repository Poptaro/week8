from rest_framework import serializers
from .models import Exotic


class ExoticSerializer(serializers.ModelSerializer):

  class Meta:
    model = Exotic
    fields = ["name", "age", "type_of_animal"]