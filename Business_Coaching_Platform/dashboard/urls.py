from django.urls import path, include
import user.views as user_views
import dashboard.views as dashboard_views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('connection', user_views.ConnectionViewSet, basename='connection')

urlpatterns = [
    path('dashboard', dashboard_views.dashboard, name='dashboard'),
]