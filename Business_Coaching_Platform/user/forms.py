from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import CustomUser, Coach, Coachee


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'age')

    @transaction.atomic
    def save(self):
        user = super().save()
        user.email = self.cleaned_data.get('email')
        user.age = self.cleaned_data.get('age')
        return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'age')


class CoachCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 500)
    last_name = forms.CharField(max_length = 500)
    description = forms.CharField(max_length = 500)
    profile_photo = forms.ImageField()

    class Meta:
        model = CustomUser
        fields = ('email', 'description', 'first_name', 'last_name', 'age', 'profile_photo')
    
    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_coach = True
        user.is_coachee = False
        user.save()
        coach = Coach.objects.create(user = user)
        coach.description = self.cleaned_data.get('description')
        coach.first_name = self.cleaned_data.get('first_name')
        coach.last_name = self.cleaned_data.get('last_name')
        coach.profile_photo = self.cleaned_data.get('profile_photo')
        coach.save()
        return user


class CoachUpdateForm(UserChangeForm):
    first_name = forms.CharField(max_length = 500)
    last_name = forms.CharField(max_length = 500)
    description = forms.CharField(max_length = 500)
    profile_photo = forms.ImageField()
    password = None

    class Meta:
        model = CustomUser
        fields = ('description', 'email', 'first_name', 'last_name', 'age', 'profile_photo')

    @transaction.atomic
    def save(self):
        user = super().save()
        user.age = self.cleaned_data.get('age')
        user.save()
        coach = Coach.objects.get(user = user)
        coach.description = self.cleaned_data.get('description')
        coach.first_name = self.cleaned_data.get('first_name')
        coach.last_name = self.cleaned_data.get('last_name')
        coach.profile_photo = self.cleaned_data.get('profile_photo')
        coach.save()
        return user


class CoacheeCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 500)
    last_name = forms.CharField(max_length = 500)
    profile_photo = forms.ImageField()

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'age', 'profile_photo')
    
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
        coachee.save()
        return user


class CoacheeUpdateForm(UserChangeForm):
    first_name = forms.CharField(max_length = 500)
    last_name = forms.CharField(max_length = 500)
    profile_photo = forms.ImageField()
    password = None

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'age', 'profile_photo')

    @transaction.atomic
    def save(self):
        user = super().save()
        user.age = self.cleaned_data.get('age')
        user.save()
        coachee = Coachee.objects.get(user = user)
        coachee.first_name = self.cleaned_data.get('first_name')
        coachee.last_name = self.cleaned_data.get('last_name')
        coachee.profile_photo = self.cleaned_data.get('profile_photo')
        coachee.save()
        return user
