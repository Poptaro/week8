from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cat
from .serializers import CatSerializer
# Create your views here.

class All_Cat(APIView):
  def get(self, request):
    dogs = CatSerializer(Cat.objects.all(), many=True).data
    return Response(dogs)