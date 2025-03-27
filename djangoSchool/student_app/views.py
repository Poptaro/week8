from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import *


class All_Students(APIView):

  def get(self, request):
    students = StudentAllSerializer(Student.objects.all(), many=True).data
    return Response(students)

class Single_Student(APIView):

  def get(self, request, name):
    student = StudentAllSerializer(Student.objects.get(name=name)).data
    return Response(student)