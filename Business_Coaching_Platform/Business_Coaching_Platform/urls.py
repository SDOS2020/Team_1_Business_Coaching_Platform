from django.contrib import admin
from django.urls import include, path
from user import views as user_views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from enrolment import views as enrolment_views


urlpatterns = [
    path('', include('home.urls')),
    path('register-coach', user_views.registerCoach, name='registerCoach'),
    path('register-coachee', user_views.registerCoachee, name='registerCoachee'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('find-coach/', enrolment_views.findCoach, name='findCoach'),
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
]
