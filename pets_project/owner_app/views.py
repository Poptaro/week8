from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Owner
from .serializers import OwnerSerializer, OwnerPetsSerializer

# Create your views here.

class All_Owners(APIView):
  def get(self, request):
    owners = OwnerSerializer(Owner.objects.all(), many=True).data
    return Response(owners)
  
class All_Owners_Pets(APIView):
  def get(self,request):
    owners_pets = OwnerPetsSerializer(Owner.objects.all(), many=True).data
    return Response(owners_pets)

class An_Owner(APIView):
  def get(self, request, id):
    owner = OwnerSerializer(Owner.objects.get(id=id)).data
    return Response(owner)

class An_Owner_Pet(APIView):
  def get(self, request, id):
    owner_pets = OwnerPetsSerializer(Owner.objects.get(id=id)).data
    return Response(owner_pets)