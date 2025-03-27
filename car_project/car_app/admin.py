from django.contrib import admin
from .models import Car
from engine_app.models import Engine
from tire_app.models import Tire
from owner_app.models import Owner

# Register your models here.
admin.site.register([Car, Engine, Tire, Owner])
