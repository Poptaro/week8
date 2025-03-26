from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.

def rectangle_area(request, height, width):
  return HttpResponse(height*width)

def rectangle_perimeter(request, height, width):
  return HttpResponse(height*2 + width*2)