from rest_framework import serializers
from .models import Tire

class TireSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tire
    fields = "__all__"
    