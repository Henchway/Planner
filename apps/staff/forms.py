from django import forms

from .models import Staff


class StaffModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StaffModelForm, self).__init__(*args, **kwargs)
        self.fields['excluded_coworkers'].queryset = Staff.objects.exclude(id=self.instance.id)

    class Meta:
        model = Staff
        fields = [
            'first_name',
            'last_name',
            'mail',
            'phone',
            'hours',
            'workdays',
            "excluded_coworkers",
            'active',
        ]


class StaffDaysOffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'days_off'
        ]

    # Validation clean_<field_name>
    # def clean_first_name(self, *args, **kwargs):
    #     first_name = self.cleaned_data.get('first_name')
    #     if "Thomas" not in first_name:
    #         raise forms.ValidationError("This is not a valid first name.")
    #     return first_name
