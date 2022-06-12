import datetime

from django.db import models

# Create your models here.
from django.db.models import TimeField, IntegerField
from django.urls import reverse
from multiselectfield import MultiSelectField

from Planner.config import Weekdays


class Shift(models.Model):
    start_time = TimeField()
    end_time = TimeField()
    weekdays = MultiSelectField(choices=Weekdays, max_choices=7, max_length=300, null=True)
    staff_needed = IntegerField(default=1)

    class Meta:
        unique_together = ['start_time', 'end_time', 'weekdays']

    @property
    def duration(self):
        date = datetime.date(1, 1, 1)
        datetime1 = datetime.datetime.combine(date, self.start_time)
        datetime2 = datetime.datetime.combine(date, self.end_time)
        return datetime2 - datetime1

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

    def get_absolute_url(self):
        return reverse("shift:shift-detail", kwargs={"id": self.id})

    def update_day_shifts(self):
        from apps.day.models import Day
        days = Day.objects.all()
        for day in days:
            if day.weekday in self.weekdays:
                day.shifts.add(self)
                day.save()
            else:
                day.shifts.remove(self)
                day.save()

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            self.update_day_shifts()
        else:
            self.update_day_shifts()
            super().save(*args, **kwargs)
