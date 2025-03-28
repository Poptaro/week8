from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dog
from .serializers import DogSerializer
# Create your views here.

class All_Dogs(APIView):
  def get(self, request):
    dogs = DogSerializer(Dog.objects.all()).data
    return Response(dogs)