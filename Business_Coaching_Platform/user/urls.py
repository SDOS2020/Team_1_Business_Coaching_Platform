from django.urls import path, include
from . import views as user_views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('connection', user_views.ConnectionViewSet, basename='connection')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('register_coach/', user_views.CoachRegisterView.as_view(), name='register_coach'),
    path('update_coach/<int:pk>/', user_views.CoachUpdateView.as_view(), name='update_coach'),
    path('update_coachee/<int:pk>/', user_views.CoacheeUpdateView.as_view(), name='update_coachee'),
    path('register_coachee/', user_views.CoacheeRegisterView.as_view(), name='register_coachee'),
    path('profile/<int:pk>/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]