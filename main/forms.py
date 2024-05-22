from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import  playlist_user

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = playlist_user
        fields = ['username', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = playlist_user
        fields = ['username', 'password']
