from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'home/home.html')