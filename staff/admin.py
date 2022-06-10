from django.contrib import admin

from shift.models import Shift
from .models import Staff

# Register your models here.

admin.site.register(Staff)
admin.site.register(Shift)