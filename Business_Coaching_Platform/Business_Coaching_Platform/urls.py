from django.contrib import admin
from django.urls import include, path
from user import views as user_views


urlpatterns = [
    path('', include('home.urls')),
    path('register', user_views.register, name='register'),
    path('admin/', admin.site.urls),
]
