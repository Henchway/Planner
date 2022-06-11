import datetime

from django.db import models, transaction
import pandas as pd

# Create your models here.
from django.db.models import CharField, DateField, ManyToManyField
from django.db.models.signals import post_save
from django.dispatch import receiver

from day.models import Day


class Schedule(models.Model):
    name = CharField(max_length=80, default=datetime.datetime.now().strftime("%B"))
    start_date = DateField(null=True)
    end_date = DateField(null=True)
    days = ManyToManyField(Day, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            dates = pd.date_range(self.start_date, self.end_date, freq='D')
            day_objects = [Day.objects.create(date=date) for date in dates]
            self.days.add(*day_objects)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}, {self.start_date} - {self.end_date}"


# @receiver(post_save, sender=Schedule, dispatch_uid="create_and_link_days")
# def create_and_link_days(sender, instance, **kwargs):
#     if kwargs.get('created'):
#         dates = pd.date_range(instance.start_date, instance.end_date, freq='D')
#         day_objects = [Day.objects.create(date=date) for date in dates]
#         instance.days.add(*day_objects)
