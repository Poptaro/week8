from django.urls import path
from .views import *

urlpatterns = [
    path("exotics/", All_Exotics.as_view())
]
