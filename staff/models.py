from django.db import models

# Create your models here.
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    mail = models.EmailField(blank=True)
    phone = PhoneNumberField(blank=True)
    hours = models.FloatField(default=40)

    def get_absolute_url(self):
        return reverse("staff:staff-detail", kwargs={"id": self.id})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"