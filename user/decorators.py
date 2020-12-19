from django.shortcuts import render, redirect
from .models import CustomUser, Connection
from django.shortcuts import get_object_or_404


def is_coach(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_coach:
            return function(request, *args, **kwargs)
        else:
            return redirect('home')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def is_coachee(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_coachee:
            return function(request, *args, **kwargs)
        else:
            return redirect('home')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def requested_user_is_coach_or_connection(function):
    def wrap(request, *args, **kwargs):
        requested_user =  get_object_or_404( CustomUser, pk = kwargs['pk'])
        if requested_user == request.user:
            return function(request, *args, **kwargs)

        elif requested_user.is_coach:
            return function(request, *args, **kwargs)
        
        elif request.user.is_coach and Connection.objects.filter(coachee = requested_user.coachee, coach = request.user.coach, accepted = True).exists():
            return function(request, *args, **kwargs)
        
        return redirect('home')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
