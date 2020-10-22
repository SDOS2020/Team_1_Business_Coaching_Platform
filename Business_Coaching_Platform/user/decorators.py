from django.shortcuts import render, redirect

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
