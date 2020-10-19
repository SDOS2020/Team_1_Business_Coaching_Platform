from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'home/home.html')

def registerCoach(request):
    return render(request, 'user/register-coach.html')

def registerCoachee(request):
    return render(request, 'user/register-coachee.html')

def login(request):
    return render(request, 'user/login.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')