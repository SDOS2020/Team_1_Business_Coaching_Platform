from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'home/home.html')

def registerCoach(request):
    return render(request, 'user/register-coach.html')

def registerCoachee(request):
    return render(request, 'user/register-coachee.html')

def login(request):
    return render(request, 'user/login.html')