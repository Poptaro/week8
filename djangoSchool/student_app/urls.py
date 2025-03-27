from django.urls import path
from .views import *

urlpatterns = [
  path('', All_Students.as_view(), name="All_Students"),
  path('<str:name>/', Single_Student.as_view(), name="Single_Student"),
]