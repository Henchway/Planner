from django.db import models
import json
# Create your models here.
from django.db.models import ManyToManyField
from django.urls import reverse
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from Planner.config import Weekdays
from apps.day.models import Day


class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    mail = models.EmailField(blank=True)
    phone = PhoneNumberField(blank=True)
    hours = models.FloatField(default=40)
    workdays = MultiSelectField(choices=Weekdays, max_choices=7, max_length=300, null=True)
    excluded_coworkers = ManyToManyField("self", blank=True)
    days_off = ManyToManyField(Day, blank=True)

    def get_absolute_url(self):
        return reverse("staff:staff-detail", kwargs={"id": self.id})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
