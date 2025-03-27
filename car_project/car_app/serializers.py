from rest_framework import serializers
from .models import Car
from owner_app.serializers import OwnerSerializer
from service_app.serializers import ServiceAllSerializer
from engine_app.serializers import EngineSerializer
from tire_app.serializers import TireSerializer


class CarSerializer(serializers.ModelSerializer):

  owners = serializers.SerializerMethodField()
  services = serializers.SerializerMethodField()
  engine = serializers.SerializerMethodField()
  tire = serializers.SerializerMethodField()

  
  class Meta:
    model = Car
    fields = "__all__"

  def get_owners(self, instance):
    owners = instance.owners.all()
    return OwnerSerializer(owners, many=True).data
  
  def get_engine(self, instance):
    engine = instance.engine
    return EngineSerializer(engine).data

  def get_tire(self, instance):
    tire = instance.tire
    return TireSerializer(tire).data
  
  def get_services(self, instance):
    services = instance.services.all()
    return ServiceAllSerializer(services, many=True).data
  
  