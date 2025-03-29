from django.urls import path
from .views import *

urlpatterns = [
    path('birds/', All_Birds.as_view())
]
