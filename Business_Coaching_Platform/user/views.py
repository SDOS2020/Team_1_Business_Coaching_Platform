from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CoachRegisterForm, CoacheeRegisterForm


def registerCoach(request):
    if request.method == 'POST':
        form = CoachRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = CoachRegisterForm()
    return render(request, 'user/register-coach.html', {'form': form})

def registerCoachee(request):
    if request.method == 'POST':
        form = CoacheeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = CoacheeRegisterForm()
    return render(request, 'user/register-coachee.html', {'form': form})

def login(request):
    return render(request, 'user/login.html', {})

