from django.contrib import admin
from .models import Client, Store, Person, Video, Address

# Register your models here.
admin.site.register(Client)
admin.site.register(Store)
admin.site.register(Person)
admin.site.register(Video)
admin.site.register(Address)