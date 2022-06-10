from django import forms

from staff.models import Staff


class StaffModelForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'first_name',
            'last_name',
            'active'
        ]

    # Validation clean_<field_name>
    # def clean_first_name(self, *args, **kwargs):
    #     first_name = self.cleaned_data.get('first_name')
    #     if "Thomas" not in first_name:
    #         raise forms.ValidationError("This is not a valid first name.")
    #     return first_name
