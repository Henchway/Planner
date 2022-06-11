from django.forms import ModelForm

from day.models import Day


class DayModelForm(ModelForm):
    class Meta:
        model = Day
        fields = [
            'date',
            'shifts',
        ]