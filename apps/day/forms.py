from django.forms import ModelForm

from .models import Day


class DayModelForm(ModelForm):
    class Meta:
        model = Day
        fields = [
            'date',
            'shifts'
        ]
