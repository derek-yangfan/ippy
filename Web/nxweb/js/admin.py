from django.contrib import admin
from .models import Country,City,Client

# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Client)