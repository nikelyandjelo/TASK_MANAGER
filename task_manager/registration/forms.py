from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from registration.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = {'username', 'first_name', 'email', 'profile_pic'}

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields = {'username', 'first_name', 'email', 'profile_pic'}

class CustomUserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)