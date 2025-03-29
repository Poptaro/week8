from django.urls import path
from .views import *

urlpatterns = [
    path("cats/", All_Cat.as_view()),
    path("cats/image", Cat_Image.as_view()),
]
