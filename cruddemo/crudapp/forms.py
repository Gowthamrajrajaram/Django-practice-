from django import forms
from crudapp .models import Student


class studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
