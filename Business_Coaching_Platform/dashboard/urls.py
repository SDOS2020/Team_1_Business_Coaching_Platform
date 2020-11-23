from django.urls import path, include
import dashboard.views as dashboard_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard', dashboard_views.dashboard, name='dashboard'),
]