from django.urls import path
from .views import *

urlpatterns = [
    path("dogs/", All_Dogs.as_view()),
]
