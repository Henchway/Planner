from django.forms import ModelForm, DateInput

from .models import Schedule


class ScheduleModelForm(ModelForm):
    class Meta:
        model = Schedule
        fields = [
            'start_date',
            'end_date'
        ]
        widgets = {
            "start_date": DateInput(attrs={'type': 'date'}),
            "end_date": DateInput(attrs={'type': 'date'}),
        }
