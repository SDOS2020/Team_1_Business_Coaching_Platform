from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import CustomUser, Coach, Coachee


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'age')

    @transaction.atomic
    def save(self):
        user = super().save()
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.age = self.cleaned_data.get('age')
        return user


class CoachCreationForm(UserCreationForm):
    description = forms.CharField(max_length = 500)
    
    class Meta:
        model = Coach
        fields = ('username', 'email', 'description', 'first_name', 'last_name', 'age')
    
    @transaction.atomic
    def save(self):
        coach = super().save()
        coach.is_coach = True
        coach.is_coachee = False
        coach.save()
        return coach


class CoachUpdateForm(UserChangeForm):
    description = forms.CharField(max_length = 500)
    password = None

    class Meta:
        model = Coach
        fields = ('description', 'email', 'first_name', 'last_name', 'age')

    @transaction.atomic
    def save(self):
        coach = super().save()
        coach.save()
        return coach


class CoacheeCreationForm(UserCreationForm):
    
    class Meta:
        model = Coachee
        fields = ('username', 'email', 'first_name', 'last_name', 'age')
    
    @transaction.atomic
    def save(self):
        coachee = super().save()
        coachee.is_coach = False
        coachee.is_coachee = True
        coachee.save()
        return coachee


class CoacheeUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = Coachee
        fields = ('email', 'first_name', 'last_name', 'age')

    @transaction.atomic
    def save(self):
        coachee = super().save()
        return coachee