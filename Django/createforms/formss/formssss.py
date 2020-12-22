from django.db.models.fields import CharField
from django import forms
from .models import formsApp


class FormApp(forms.ModelForm):
    class Meta():
        model = formsApp
        fields = '__all__'
        widgets = {
            'email_Id': forms.TextInput(attrs={'placeholder':'Enter Email'}),
            'DateOfBirth': forms.TextInput(attrs={'type':'date','placeholder':'yyyy-mm-dd'}),
            'gender_radio':forms.RadioSelect(),

        }
