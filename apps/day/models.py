from django.db import models

# Create your models here.
from django.db.models import DateField, ForeignKey, ManyToManyField, CharField
from django.urls import reverse
from datetime import date
import calendar

from apps.shift.models import Shift


class Day(models.Model):
    date = DateField(null=True, unique=True)
    shifts = ManyToManyField("shift.Shift", blank=True)
    schedule = ForeignKey("schedule.Schedule", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.weekday}, {self.date}"

    def set_shifts(self):
        shifts = list(Shift.objects.all())
        for shift in shifts:
            if self.weekday in shift.weekdays:
                self.shifts.add(shift)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            self.set_shifts()
        else:
            super().save(*args, **kwargs)

    @property
    def weekday(self):
        return calendar.day_name[self.date.weekday()]

    @property
    def is_in_past(self):
        return date.today() > self.date

    def get_absolute_url(self):
        return reverse("day:day-detail", kwargs={"id": self.id})

# @receiver(post_save, sender=Schedule, dispatch_uid="create_and_link_days")
# def create_and_link_days(sender, instance, **kwargs):
#     if kwargs.get('created'):
#         dates = pd.date_range(instance.start_date, instance.end_date, freq='D')
#         day_objects = [Day.objects.create(date=date) for date in dates]
#         instance.days.add(*day_objects)
