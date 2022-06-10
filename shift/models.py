from django.db import models

# Create your models here.
from django.db.models import TimeField
from django.urls import reverse


class Shift(models.Model):
    start = TimeField()
    end = TimeField()

    def get_absolute_url(self):
        return reverse("shift:shift-detail", kwargs={"id": self.id})
