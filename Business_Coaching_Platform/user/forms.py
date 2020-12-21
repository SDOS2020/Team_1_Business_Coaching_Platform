from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.db import transaction
from .models import CustomUser, Coach, Coachee

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'age')

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.email = self.cleaned_data.get('email')
        user.age = self.cleaned_data.get('age')
        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'age')

class UserPasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = CustomUser
        fields = ('password')


class CoachCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 500)
    last_name = forms.CharField(max_length = 500)
    area_of_expertise = forms.CharField(max_length = 500)
    profile_photo = forms.ImageField()
    linkedin = forms.URLField(max_length = 100, required = False)

    class Meta:
        model = CustomUser
        fields = ('email', 'area_of_expertise', 'first_name', 'last_name', 'age', 'profile_photo', 'linkedin')
    
    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_coach = True
        user.is_coachee = False
        user.save()
        coach = Coach.objects.create(user = user)
        coach.area_of_expertise = self.cleaned_data.get('area_of_expertise')
        coach.first_name = self.cleaned_data.get('first_name')
        coach.last_name = self.cleaned_data.get('last_name')
        coach.profile_photo = self.cleaned_data.get('profile_photo')
        coach.linkedin = self.cleaned_data.get('linkedin')
        coach.save()
        return user


class CoacheeCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 500)
    last_name = forms.CharField(max_length = 500)
    profile_photo = forms.ImageField()
    linkedin = forms.URLField(max_length = 100, required = False)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'age', 'profile_photo', 'linkedin')
    
    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_coach = False
        user.is_coachee = True
        user.save()
        coachee = Coachee.objects.create(user = user)
        coachee.first_name = self.cleaned_data.get('first_name')
        coachee.last_name = self.cleaned_data.get('last_name')
        coachee.profile_photo = self.cleaned_data.get('profile_photo')
        coachee.linkedin = self.cleaned_data.get('linkedin')
        coachee.save()
        return user
