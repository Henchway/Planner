from django.db import models

# Create your models here.
from django.db.models import DateField, CharField, ForeignKey, ManyToManyField

from shift.models import Shift


class Day(models.Model):
    date = DateField(null=True, unique=True)
    shifts = ManyToManyField(Shift, blank=True)



    def __str__(self):
        return f"{self.date}"

    @property
    def weekday(self):
        return self.date.weekday()
