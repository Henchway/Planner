import datetime

from django.db import models

# Create your models here.
from django.db.models import TimeField
from django.urls import reverse


class Shift(models.Model):
    start_time = TimeField()
    end_time = TimeField()

    class Meta:
        unique_together = ['start_time', 'end_time', ]

    @property
    def duration(self):
        date = datetime.date(1, 1, 1)
        datetime1 = datetime.datetime.combine(date, self.start_time)
        datetime2 = datetime.datetime.combine(date, self.end_time)
        return datetime2 - datetime1

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

    # start_time_string = datetime.strptime(str(start_time), '%HH:%MM')
    # end_time_string = datetime.strptime(str(end_time), '%HH:%MM')
    # difference = end_time_string - start_time_string
    # start_min_time = datetime.min.replace(hour=start_time.hour, minute=start_time.minute, second=start_time.second)
    # end_min_time = datetime.min.replace(hour=end_time.hour, minute=end_time.minute, second=end_time.second)
    # duration = datetime.combine(date.min, end_min_time) - datetime.combine(date.min, end_min_time)

    def get_absolute_url(self):
        return reverse("shift:shift-detail", kwargs={"id": self.id})
