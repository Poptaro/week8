from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cat
from .serializers import CatSerializer
from dotenv import load_dotenv
import requests

load_dotenv()

class All_Cat(APIView):
  def get(self, request):
    dogs = CatSerializer(Cat.objects.all(), many=True).data
    return Response(dogs)
  
class Cat_Image(APIView):
  def get(self, request):
    r = requests.get("https://api.thecatapi.com/v1/images/search?api_key={CAT_API_KEY}")
    print(r.json())
    return Response(r.json()[0]['url'])