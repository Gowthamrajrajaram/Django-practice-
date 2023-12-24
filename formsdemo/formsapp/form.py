from django import forms

class employeinfoform(forms.Form):
    name=forms.CharField()
    salary=forms.IntegerField()

