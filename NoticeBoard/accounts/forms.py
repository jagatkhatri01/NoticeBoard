from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')