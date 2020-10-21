from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register-coach', views.CoachRegisterView.as_view(), name='register_coach'),
    path('register-coachee', views.CoacheeRegisterView.as_view(), name='register_coachee'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]