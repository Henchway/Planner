from django.forms import ModelForm

from shift.models import Shift


class ShiftModelForm(ModelForm):
    class Meta:
        model = Shift
        fields = [
            'start_time',
            'end_time'
        ]
