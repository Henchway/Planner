import datetime

from django.db import models
import pandas as pd

# Create your models here.
from django.db.models import CharField, DateField, ManyToManyField
from django.urls import reverse

from apps.day.models import Day

class Schedule(models.Model):
    start_date = DateField(null=True)
    end_date = DateField(null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            dates = pd.date_range(self.start_date, self.end_date, freq='D')
            [Day.objects.create(date=date, schedule=self) for date in dates]
        elif self.pk is not None:
            previous_days = list(Day.objects.filter(schedule=self.id))
            dates = pd.date_range(self.start_date, self.end_date, freq='D')
            for date in dates:
                try:
                    Day.objects.create(date=date, schedule=self)
                except Exception:
                    pass
            new_days = list(Day.objects.filter(date__gte=self.start_date, date__lte=self.end_date))
            if not previous_days == new_days:
                for day in previous_days:
                    if day not in new_days:
                        day.delete()
            super().save(*args, **kwargs)

    class Meta:
        unique_together = ['start_date', 'end_date', ]

    def __str__(self):
        return f"{self.start_date} - {self.end_date}"

    def get_absolute_url(self):
        return reverse("schedule:schedule-detail", kwargs={"id": self.id})

    @property
    def days(self):
        return Day.objects.filter(schedule=self.id)

# @receiver(post_save, sender=Schedule, dispatch_uid="create_and_link_days")
# def create_and_link_days(sender, instance, **kwargs):
#     if kwargs.get('created'):
#         dates = pd.date_range(instance.start_date, instance.end_date, freq='D')
#         day_objects = [Day.objects.create(date=date) for date in dates]
#         instance.days.add(*day_objects)
