from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bird
from .serializers import BirdSerializer
# Create your views here.

class All_Birds(APIView):
  def get(self, request):
    birds = BirdSerializer(Bird.objects.all(), many=True).data
    return Response(birds)