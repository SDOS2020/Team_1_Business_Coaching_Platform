from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from user.decorators import is_coach, is_coachee, requested_user_is_coach_or_connection
from user.models import Coach, Coachee, CustomUser, Connection
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets
from user.serializer import ConnectionSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
@login_required
def dashboard(request):
    if request.user.is_coach:
        return render(request, 'dashboard/coach_dashboard.html', {'profile' : request.user})
    elif request.user.is_coachee:
        return render(request, 'dashboard/coachee_dashboard.html', {'profile' : request.user})
    else:
        return redirect('home')