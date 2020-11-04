from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register-coach/', views.CoachRegisterView.as_view(), name='register_coach'),
    path('update_coach/<int:pk>/', views.CoachUpdateView.as_view(), name='update_coach'),
    path('update_coachee/<int:pk>/', views.CoacheeUpdateView.as_view(), name='update_coachee'),
    path('register_coachee/', views.CoacheeRegisterView.as_view(), name='register_coachee'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]