from django.forms import ModelForm

from .models import Location


class LocationModelForm(ModelForm):
    class Meta:
        model = Location
        fields = [
            'name',
            'address'
        ]
