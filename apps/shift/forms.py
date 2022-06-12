from django.core.exceptions import ValidationError
from django.forms import ModelForm, TimeInput

from .models import Shift


class ShiftModelForm(ModelForm):
    class Meta:
        model = Shift
        fields = [
            'start_time',
            'end_time',
            'weekdays',
            'staff_needed'
        ]
        widgets = {
            "start_time": TimeInput(attrs={'type': 'time'}),
            "end_time": TimeInput(attrs={'type': 'time'}),
        }

    def clean_start_time(self):
        start_time = self.data.get('start_time')
        end_time = self.data.get('end_time')
        if start_time >= end_time:
            raise ValidationError("The end time must be greater than the start time.")
        return start_time

    def clean_end_time(self):
        start_time = self.data.get('start_time')
        end_time = self.data.get('end_time')
        if start_time >= end_time:
            raise ValidationError("The end time must be greater than the start time.")
        return end_time

    # def clean_first_name(self, *args, **kwargs):
    #     first_name = self.cleaned_data.get('first_name')
    #     if "Thomas" not in first_name:
    #         raise forms.ValidationError("This is not a valid first name.")
    #     return first_name
