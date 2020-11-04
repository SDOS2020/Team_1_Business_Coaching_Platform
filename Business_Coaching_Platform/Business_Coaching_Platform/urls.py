from django.contrib import admin
from django.urls import include, path
from user import views as user_views
from enrolment import views as enrolment_views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('home.urls')),
    path('', include('user.urls')),
    path('', include('enrolment.urls')),
    path('admin/', admin.site.urls),
]