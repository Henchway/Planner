from django.db import models

# Create your models here.
from django.db.models import CharField, ForeignKey
from django.urls import reverse


class Location(models.Model):
    name = CharField(max_length=200)
    address = CharField(max_length=300)

    # shifts = ForeignKey(Shift, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("location:location-detail", kwargs={"id": self.id})
