from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CoachCreationForm, CoacheeCreationForm
from .decorators import is_coach, is_coachee
from .models import Coach, Coachee, CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class CoachRegisterView(CreateView):
    form_class = CoachCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register_coach.html'


class CoacheeRegisterView(CreateView):
    form_class = CoacheeCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register_coachee.html'


class CoachUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    success_url = reverse_lazy('profile')
    template_name = 'user/update_coach.html'
    model = Coach    
    fields = ['first_name', 'last_name', 'description', 'profile_photo']

    def test_func(self):
        coach = self.get_object()
        if self.request.user.coach == coach:
            return True
        return False


class CoacheeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    success_url = reverse_lazy('profile')
    template_name = 'user/update_coachee.html'
    model = Coachee    
    fields = ['first_name', 'last_name', 'profile_photo']

    def test_func(self):
        coachee = self.get_object()
        if self.request.user.coachee == coachee:
            return True
        return False


@login_required
def profile(request):
    return render(request, 'user/profile.html')
