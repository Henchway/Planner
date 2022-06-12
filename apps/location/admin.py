from django.contrib import admin

# Register your models here.
from apps.location.models import Location

admin.site.register(Location)