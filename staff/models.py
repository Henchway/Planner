from django.db import models

# Create your models here.
from django.urls import reverse


class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("staff:staff-detail", kwargs={"id": self.id})
