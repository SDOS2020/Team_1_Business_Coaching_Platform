from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CoachCreationForm, CoacheeCreationForm
from .decorators import is_coach, is_coachee


class CoachRegisterView(CreateView):
    form_class = CoachCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register-coach.html'


class CoacheeRegisterView(CreateView):
    form_class = CoacheeCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register-coachee.html'


def login(request):
    return render(request, 'user/login.html')



@login_required
@is_coach
def profile(request):
    return render(request, 'user/profile.html')