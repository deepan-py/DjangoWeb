from django import forms
from django.contrib.auth.models import User
from a_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfo(forms.ModelForm):
    class meta():
        models=UserProfileInfo
        fields = ('portfoloio_site','profile_pic')