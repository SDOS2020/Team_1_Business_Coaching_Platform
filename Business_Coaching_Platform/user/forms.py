from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CoachRegisterForm(UserCreationForm):
    email = forms.EmailField()
    user_type = 'Coach'
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CoacheeRegisterForm(UserCreationForm):
    email = forms.EmailField()
    user_type = 'Coachee'
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']