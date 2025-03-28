from django.urls import path
from views import *

urlpatterns = [
    path("", All_Dogs.as_view())
]
