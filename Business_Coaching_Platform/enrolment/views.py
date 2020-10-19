from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def findCoach(request):
    return HttpResponse("Hello, world. You're at the find coach page.")

