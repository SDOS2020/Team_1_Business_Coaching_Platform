from django.contrib import admin
from django.urls import include, path
from user import views as user_views


urlpatterns = [
    path('', include('home.urls')),
    path('register-coach', user_views.registerCoach, name='registerCoach'),
    path('register-coachee', user_views.registerCoachee, name='registerCoachee'),
    path('login', user_views.login, name='login'),
    path('admin/', admin.site.urls),
]
