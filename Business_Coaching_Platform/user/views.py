from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CoachRegisterForm


def register(request):
    if request.method == 'POST':
        form = CoachRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = CoachRegisterForm()
    return render(request, 'user/register.html', {'form': form})