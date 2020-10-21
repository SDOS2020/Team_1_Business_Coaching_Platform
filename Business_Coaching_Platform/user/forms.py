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
        model = CustomUser
        fields = ('username', 'email', 'description', 'first_name', 'last_name', 'age')
    
    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_coach = True
        user.is_coachee = False
        user.save()
        coach = Coach.objects.create(user = user, description = self.cleaned_data.get('description'))
        coach.save()
        return user


class CoacheeCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'age')
    
    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_coach = False
        user.is_coachee = True
        user.save()
        coachee = Coachee.objects.create(user = user)
        coachee.save()
        return user