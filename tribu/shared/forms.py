from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.SlugField(
        max_length=64,
        required=True,
    )
    password = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.PasswordInput,
    )


class SignupForm(forms.Form):
    class Meta:
        model = User
