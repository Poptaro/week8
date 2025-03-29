from django.urls import path
from .views import *

urlpatterns = [
    path("owners/", All_Owners.as_view()),
    path("owners_pets/", All_Owners_Pets.as_view()),
    path("owner/<int:id>/", An_Owner.as_view()),
    path("owner_pet/<int:id>/", An_Owner_Pet.as_view())
]
