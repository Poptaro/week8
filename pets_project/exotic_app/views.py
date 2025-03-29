from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Exotic
from .serializers import ExoticSerializer
# Create your views here.

class All_Exotics(APIView):
  def get(self, request):
    Exotics = ExoticSerializer(Exotic.objects.all(), many=True).data
    return Response(Exotics)